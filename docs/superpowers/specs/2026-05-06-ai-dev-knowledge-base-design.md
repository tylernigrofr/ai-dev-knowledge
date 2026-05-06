# AI Dev Knowledge Base — Design Spec

**Date:** 2026-05-06
**Status:** Approved (pending user review of this written spec)
**Owner:** tylernigrofr

## Purpose

A lean, curated, constantly-updated knowledge base of state-of-the-art AI-driven development practices combined with proven software engineering fundamentals — best practices, tools, frameworks, mental models, workflows, architecture patterns, and anti-patterns.

**Primary consumers:** AI agents (Claude Code, OpenCode, etc.) pulling relevant context on demand.
**Secondary consumer:** the user, browsing as a wiki / future static site.

The KB is the source of truth. Everything else (static site, RAG chat, agent skills) is a derived view.

## Non-goals (out of scope)

- Replacing existing skills libraries (e.g. `mattpocock/skills`). The KB references and complements them, not duplicates.
- General programming tutorials. Scope is AI-driven development + the proven engineering fundamentals it leans on.
- Hosting a public community contribution platform in v1. Single-curator model first.
- Implementing the full Pocock-style orchestration stack (sandcastle, dashboard). That's a *consumer* of this KB, not part of it.
- Auto-context-clearing or token-budget enforcement. Discipline lives in conventions + skills, not enforcement infra.

## Architecture

### Repo shape

```
ai-dev-knowledge/
├── README.md              # entry point: what this is, how to use it (human + agent)
├── INDEX.md               # auto-generated multi-axis index (by type, phase, tag, status)
├── CONTEXT.md             # ubiquitous-language doc + curation rules + frontmatter schemas
├── sources/
│   ├── youtube/           # one .md per video: metadata + transcript + extracted insights
│   ├── articles/
│   ├── papers/
│   ├── repos/             # notable OSS, what's worth stealing, install notes
│   └── social/            # tweets / LinkedIn / forum posts captured as sources
├── concepts/              # flat, atomic, one idea per file. Frontmatter-tagged.
├── playbooks/             # flat, workflow-shaped. End-to-end recipes citing concepts.
├── _inbox/
│   ├── urls.md            # lightweight queue: just URLs, one per line
│   ├── drops/             # one file per messy drop (YYYY-MM-DD-slug.md)
│   └── _processed/        # archived drops by month, with routing header appended
├── skills/                # custom skills that operate on this KB
│   ├── triage-inbox.md
│   ├── add-source.md
│   ├── distill-concept.md
│   ├── update-playbook.md
│   ├── review-staleness.md
│   ├── build-index.md
│   ├── kb-search.md
│   └── kb-pull.md
├── .schemas/              # JSON Schemas for source/concept/playbook frontmatter
└── .claude/
    └── settings.json      # permissions for the skills above
```

Directories are flat under `concepts/` and `playbooks/` — better for grep/agent retrieval, link stability, and frontmatter-based multi-axis filtering.

### Frontmatter schemas

**`sources/<type>/<slug>.md`:**
```yaml
title: "..."
type: youtube              # youtube | article | paper | repo | social | other
url: https://...
author: ...
published: YYYY-MM-DD
captured: YYYY-MM-DD
status: extracted          # raw | extracted | superseded
concepts_seeded: [slug, slug, ...]
```
Body = transcript / archived text + an "Extracted insights" section, each bullet linking to the concept(s) it informs.

**`concepts/<slug>.md`:**
```yaml
title: ...
type: mental-model         # mental-model | principle | technique | tool | framework | anti-pattern | workflow
phase: [planning, decomposition, implementation, review, qa]
tags: [...]
sources: [sources/youtube/...md, ...]
status: stable             # draft | stable | contested | deprecated
superseded_by: null        # slug if deprecated
last_reviewed: YYYY-MM-DD
```
Body sections:
- One-sentence summary (the claim, copy-pasteable)
- Why it matters (~3 sentences)
- How to apply (concrete, ideally with snippet or rule)
- Caveats / when it doesn't apply
- Related (linked concepts, opposing concepts, anti-patterns)

**`playbooks/<slug>.md`:**
```yaml
title: ...
phase: [...]
tags: [...]
concepts_used: [slug, slug, ...]
tools: [sandcastle, opencode, claude-code, ...]
status: stable
last_reviewed: YYYY-MM-DD
```
Body = step-by-step recipe: prerequisites → setup → loop → verification → failure modes. Each step cites the concept(s) that justify it.

### Curation rules (encoded in `CONTEXT.md`)

1. One idea per concept file. Can't summarize in one sentence → split.
2. Soft cap: 200 lines / ~1500 words per concept. Audit flags overruns.
3. New concept files require justification — default action on a new insight is *refine an existing concept*, not create.
4. Every concept must cite ≥1 source. No uncited claims.
5. Deprecated concepts stay (link stability) but are hidden from default `INDEX.md`.
6. Playbooks must link to their underlying concepts. Playbooks without concept references are suspect.
7. `last_reviewed` updates on any non-trivial edit.

### Inbox lifecycle

- Drop a URL into `_inbox/urls.md` (one per line) — low-friction queue.
- Drop messier content (social posts, snippets, your own thoughts) into `_inbox/drops/YYYY-MM-DD-<slug>.md` — no structure required up front.
- `/triage-inbox` processes both. For each item, routes to one of three outcomes via `/distill-concept`:
  1. **Source** (article snippet, social post, transcript, repo notes) → migrate to `sources/<type>/<slug>.md` with frontmatter, then update/create affected concepts.
  2. **Seed** (your half-formed thought, snippet that informs an existing concept) → distill into the relevant concepts, archive the drop.
  3. **Junk / superseded** → delete.
- After processing, the drop file moves to `_inbox/_processed/YYYY-MM/` with a one-line routing header appended (e.g. `→ concepts/smart-zone.md, sources/youtube/pocock-2025.md`). `_processed/` can be purged at any time.

### Curation gate (`/distill-concept`)

For every new insight, the skill picks one:
- **Refine in place** — small clarification / better phrasing / new example. Edit existing concept.
- **Replace section** — new info clearly improves one part. Edit that section, note the source.
- **Supersede** — new idea materially better. Mark old `status: deprecated`, add `superseded_by`. Old file stays for link integrity.
- **Reject** — duplicate or weaker. Drop it, log why in triage report.
- **Create** (last resort) — only when no existing concept can reasonably absorb the idea.

### Periodic audit (`/review-staleness`)

Runs on demand or scheduled. Sweeps `concepts/` for:
- Concepts not reviewed in >N months (configurable, default 6)
- Concepts whose sources are all >12 months old → flag for re-validation
- Concepts marked `status: contested` needing resolution
- Bloat: any concept file over the soft cap → flag for split
- Orphaned concepts (no inbound links from playbooks or other concepts)
- Detected contradictions via cross-reference

Output is a triage report with proposed edits queued for user review.

## Skills

| Skill | Purpose |
|---|---|
| `/triage-inbox` | Batch-process `_inbox/`. Pulls YouTube transcripts via Supadata MCP, summarizes articles, runs each drop through `/distill-concept`, archives to `_processed/`. |
| `/add-source` | One-shot add: paste URL or text, skip inbox, go straight to `sources/` + concept distillation. |
| `/distill-concept` | The curation gate (Refine / Replace / Supersede / Reject / Create). Called by triage and add-source. |
| `/update-playbook` | When concepts change, find playbooks that link to them and propose diffs. |
| `/review-staleness` | Periodic audit per the rules above. |
| `/build-index` | Regenerate `INDEX.md` from frontmatter (by type, phase, tag, status). |
| `/kb-search` | Query KB by tag/type/phase/freetext. **Main agent-facing retrieval verb.** |
| `/kb-pull` | Given a slug, return full concept/playbook content. Convenience wrapper. |

## Cross-project consumption

1. KB lives at a stable local path (e.g. `C:\Users\tnigr\OneDrive\Documents\GitHub\ai-dev-knowledge`).
2. Path exposed as `AI_KB_PATH` env var in shell profile.
3. Each consuming project's `CLAUDE.md` (or `AGENTS.md`) includes a stanza:
   > AI dev best practices live at `$AI_KB_PATH/`. Search `concepts/` and `playbooks/` by frontmatter tag/type/phase. Use the `kb-search` skill if installed.
4. Optionally install `kb-search` and `kb-pull` as per-project skills (symlink or copy from KB's `skills/`).
5. **Future:** publish as a skills bundle installable via `npx skills add tylernigrofr/ai-dev-knowledge`. Defer until shape is proven.

## Static-site byproduct (deferred)

When content justifies (≥30 concepts, ≥3 playbooks):

- **Astro Starlight** in `site/` subdir. Reads `../concepts/`, `../playbooks/`, `../sources/` as the source of truth.
- Sidebar grouped by `playbooks/` and `concepts/`, with concepts faceted by `type` and `phase`.
- Tag pages auto-generated from frontmatter.
- Source pages browsable but de-emphasized.
- Deprecated concepts hidden by default, toggleable.
- Search via Pagefind (client-side, zero infra).
- One-click "copy raw markdown" button per concept and playbook page.
- CI builds + deploys on push to `main` (Cloudflare Pages or Vercel).

## Future enhancements (deferred)

- **Embedded RAG chat** for custom architecture synthesis — hosted on Cloudflare Worker, indexes the same KB content, answers "what's the best pattern for X" with cited synthesis.
- **Scheduled inbox sweepers** — cron-style routine pulling new videos from a watchlist of channels (AI Engineer, etc.) into `_inbox/urls.md` automatically.
- **AST-based module-map drift detection** — bigger project; heuristic version is in scope for v1 audit.
- **Plugin packaging** — `npx skills add tylernigrofr/ai-dev-knowledge` for portable install.

## Build order

**Phase 1 — Skeleton + seed content**
1. Create directory tree, `README.md`, `CONTEXT.md` (with curation rules + frontmatter schemas), empty `INDEX.md`.
2. Write JSON Schemas in `.schemas/` for source/concept/playbook frontmatter.
3. Hand-seed from the Pocock conversation in the brainstorming context: one source file, ~8–12 starter concepts (smart-zone-vs-dumb-zone, grilling-alignment, vertical-slices, ralph-loop, push-vs-pull-context, deep-modules, clean-context-reviewer, afk-vs-hitl, doc-rot, compacting-vs-clearing, three-route-prototype, ubiquitous-language), one playbook stub (`afk-night-shift.md`).
4. Set `AI_KB_PATH` in shell profile.
5. Commit.

**Phase 2 — Core skills**
6. `/kb-search` and `/kb-pull` — most-used, build first.
7. `/add-source` — single-source ingestion (calls Supadata MCP for YouTube).
8. `/distill-concept` — the curation gate.
9. `/triage-inbox` — batch processor.
10. `/build-index`.
11. Commit. KB is now usable.

**Phase 3 — Maintenance skills** (after volume justifies)
12. `/update-playbook`.
13. `/review-staleness`.

**Phase 4 — Static site** (deferred)
14. `site/` Astro Starlight project + CI deploy.
15. One-click copy-markdown buttons.

**Phase 5 — Future affordances**
16. Embedded RAG chat.
17. Scheduled inbox sweepers.
18. Plugin packaging.

## What's actually hard

- **The curation gate**. Getting `/distill-concept` to consistently choose Refine over Create is the difference between a lean KB and a bloated one. Plan to iterate on the skill prompt for weeks based on observed behavior.
- **Frontmatter discipline**. If `last_reviewed` and `sources` aren't kept current, audit becomes useless. Validation in `/build-index` (warn on missing fields) helps.
- **Avoiding doc rot**. Same problem Pocock flagged: archived sources keep getting pulled in as authoritative. The `status: superseded` field on sources is the main mitigation; periodic audit is the fallback.

## Open questions

None blocking. Plugin packaging shape, RAG indexing strategy, and watchlist-puller config are all deferred and will be designed when their phase begins.
