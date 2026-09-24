#!/usr/bin/env python3
"""Deterministic KB tooling. Stdlib only.

  kb.py search [QUERY...] [--tag T] [--type T] [--phase P] [--kind concept|playbook|source] [--all]
  kb.py index            regenerate INDEX.md
  kb.py lint             validate frontmatter, links, citations, size caps

KB root: $AI_KB_PATH if set, else the repo this script lives in.
"""
import argparse
import os
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(os.environ.get("AI_KB_PATH") or Path(__file__).resolve().parent.parent)

CONCEPT_TYPES = ["mental-model", "principle", "technique", "tool", "framework", "anti-pattern", "workflow"]
PHASES = ["planning", "decomposition", "implementation", "review", "qa"]
STATUSES = ["draft", "stable", "contested", "deprecated"]
REQUIRED = {
    "concept": ["title", "type", "phase", "tags", "sources", "status", "last_reviewed"],
    "playbook": ["title", "phase", "tags", "concepts_used", "status", "last_reviewed"],
    "source": ["title", "type", "captured", "status"],
}
LINE_CAP = 200


# ---------- parsing ----------

def _scalar(v):
    v = v.strip()
    if not v.startswith(("'", '"')):
        v = re.sub(r"\s+#.*$", "", v)
    if v in ("null", "~", ""):
        return None
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        return [_scalar(x) for x in v[1:-1].split(",") if x.strip()]
    return v


def parse(path):
    text = path.read_text(encoding="utf-8")
    fm, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if m:
        body = m.group(2)
        key = None
        for line in m.group(1).splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            item = re.match(r"^\s+-\s+(.*)$", line)
            if item and key:
                if not isinstance(fm.get(key), list):
                    fm[key] = []
                fm[key].append(_scalar(item.group(1)))
                continue
            kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
            if kv:
                key = kv.group(1)
                fm[key] = _scalar(kv.group(2))
    return fm, body, text


def summary(body):
    m = re.search(r"^## Summary\s*\n+(.+?)(?:\n\n|\n##|\Z)", body, re.S | re.M)
    if m:
        return " ".join(m.group(1).split())
    for para in body.split("\n\n"):
        p = para.strip()
        if p and not p.startswith("#"):
            return " ".join(p.split())
    return ""


def load(kinds=("concept", "playbook", "source")):
    docs = []
    globs = {"concept": "concepts/*.md", "playbook": "playbooks/*.md", "source": "sources/*/*.md"}
    for kind in kinds:
        for p in sorted(ROOT.glob(globs[kind])):
            fm, body, text = parse(p)
            docs.append({"kind": kind, "path": p.relative_to(ROOT).as_posix(), "slug": p.stem,
                         "fm": fm, "body": body, "lines": text.count("\n") + 1,
                         "summary": summary(body)})
    return docs


def as_list(v):
    return v if isinstance(v, list) else ([] if v is None else [v])


# ---------- search ----------

def cmd_search(a):
    kinds = [a.kind] if a.kind else ["concept", "playbook"]
    terms = [t.lower() for t in a.query]
    hits = []
    for d in load(kinds):
        fm = d["fm"]
        if fm.get("status") == "deprecated" and not a.all:
            continue
        if a.tag and a.tag not in as_list(fm.get("tags")):
            continue
        if a.type and fm.get("type") != a.type:
            continue
        if a.phase and a.phase not in as_list(fm.get("phase")):
            continue
        score = 0
        title = str(fm.get("title", "")).lower()
        tags = " ".join(map(str, as_list(fm.get("tags")))).lower()
        summ = d["summary"].lower()
        body = d["body"].lower()
        for t in terms:
            score += 5 * (t in title) + 4 * (t in d["slug"]) + 3 * (t in tags) + 2 * (t in summ) + min(body.count(t), 3)
        if terms and score == 0:
            continue
        hits.append((score, d))
    hits.sort(key=lambda x: (-x[0], x[1]["path"]))
    print(f"## kb-search results ({len(hits)} matches)\n")
    for i, (_, d) in enumerate(hits[: a.limit], 1):
        fm = d["fm"]
        chips = " · ".join(filter(None, [str(fm.get("type") or d["kind"]),
                                         ",".join(map(str, as_list(fm.get("phase")))),
                                         str(fm.get("status") or "")]))
        print(f"{i}. [{fm.get('title', d['slug'])}]({d['path']}) — {d['summary'][:220]}\n   `{chips}`")


# ---------- index ----------

def cmd_index(a):
    docs = load()
    concepts = [d for d in docs if d["kind"] == "concept"]
    live = [d for d in concepts if d["fm"].get("status") != "deprecated"]
    dep = [d for d in concepts if d["fm"].get("status") == "deprecated"]
    playbooks = [d for d in docs if d["kind"] == "playbook"]
    sources = [d for d in docs if d["kind"] == "source"]

    def t(d):
        return d["fm"].get("title", d["slug"])

    def link(d):
        return f"[{t(d)}]({d['path']})"

    out = ["# Index", "", f"_Generated by `scripts/kb.py index` on {date.today().isoformat()}. Do not edit by hand._", ""]
    out += ["## Playbooks", ""]
    for d in sorted(playbooks, key=t):
        out.append(f"- {link(d)} — `{d['fm'].get('status')}` — {d['summary'][:160]}")
    out += ["", "## Concepts by type", ""]
    by_type = defaultdict(list)
    for d in live:
        by_type[d["fm"].get("type")].append(d)
    for ty in CONCEPT_TYPES:
        if by_type.get(ty):
            out += [f"### {ty}", ""] + [f"- {link(d)}" for d in sorted(by_type[ty], key=t)] + [""]
    out += ["## Concepts by phase", ""]
    for ph in PHASES:
        items = [d for d in live if ph in as_list(d["fm"].get("phase"))]
        if items:
            out += [f"**{ph}:** " + ", ".join(f"[{d['slug']}]({d['path']})" for d in sorted(items, key=lambda d: d["slug"])), ""]
    out += ["## Tags", ""]
    by_tag = defaultdict(list)
    for d in live:
        for tg in as_list(d["fm"].get("tags")):
            by_tag[tg].append(d["slug"])
    for tg in sorted(by_tag, key=lambda k: (-len(by_tag[k]), k)):
        if len(by_tag[tg]) > 1:
            out.append(f"- **{tg}** ({len(by_tag[tg])}): " + ", ".join(sorted(by_tag[tg])))
    out += ["", "## Sources", ""]
    for d in sorted(sources, key=lambda d: d["path"]):
        out.append(f"- {link(d)}")
    if dep:
        out += ["", f"<details><summary>Deprecated ({len(dep)})</summary>", ""]
        out += [f"- {link(d)} → {d['fm'].get('superseded_by')}" for d in dep]
        out += ["", "</details>"]
    problems = lint(docs)
    if problems:
        out += ["", "<details><summary>Lint warnings</summary>", ""] + [f"- {p}" for p in problems] + ["", "</details>"]
    (ROOT / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote INDEX.md: {len(live)} concepts, {len(playbooks)} playbooks, {len(sources)} sources, {len(problems)} warnings")


# ---------- lint ----------

def lint(docs):
    problems = []
    slugs = {d["slug"] for d in docs if d["kind"] == "concept"}
    for d in docs:
        fm, p = d["fm"], d["path"]
        for k in REQUIRED[d["kind"]]:
            if fm.get(k) in (None, [], ""):
                problems.append(f"{p}: missing `{k}`")
        if d["kind"] == "concept":
            if fm.get("type") not in CONCEPT_TYPES:
                problems.append(f"{p}: bad type `{fm.get('type')}`")
            if fm.get("status") not in STATUSES:
                problems.append(f"{p}: bad status `{fm.get('status')}`")
            for s in as_list(fm.get("sources")):
                if s and not s.startswith("http") and not (ROOT / s).exists():
                    problems.append(f"{p}: cites missing source `{s}`")
            if fm.get("status") == "deprecated" and fm.get("superseded_by") not in slugs:
                problems.append(f"{p}: deprecated without valid superseded_by")
            if d["lines"] > LINE_CAP:
                problems.append(f"{p}: {d['lines']} lines (cap {LINE_CAP})")
        if d["kind"] == "playbook":
            for c in as_list(fm.get("concepts_used")):
                if c not in slugs:
                    problems.append(f"{p}: concepts_used references unknown `{c}`")
        for ph in as_list(fm.get("phase")):
            if ph not in PHASES:
                problems.append(f"{p}: bad phase `{ph}`")
        for target in re.findall(r"\]\(([^)#\s]+\.md)\)", d["body"]):
            if not target.startswith("http") and not (ROOT / p).parent.joinpath(target).resolve().exists():
                problems.append(f"{p}: broken link `{target}`")
    return problems


def cmd_lint(a):
    problems = lint(load())
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query", nargs="*")
    s.add_argument("--tag")
    s.add_argument("--type", choices=CONCEPT_TYPES)
    s.add_argument("--phase", choices=PHASES)
    s.add_argument("--kind", choices=["concept", "playbook", "source"])
    s.add_argument("--all", action="store_true", help="include deprecated")
    s.add_argument("--limit", type=int, default=10)
    s.set_defaults(fn=cmd_search)
    sub.add_parser("index").set_defaults(fn=cmd_index)
    sub.add_parser("lint").set_defaults(fn=cmd_lint)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
