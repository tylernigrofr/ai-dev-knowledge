# CLAUDE.md — ai-dev-knowledge

This is a curated knowledge base of AI-driven development practices, optimized for agents pulling context on demand. **Read [CONTEXT.md](CONTEXT.md) first** — it's the ubiquitous-language doc, curation rules, and frontmatter schemas.

## What lives where
- `sources/<type>/` — raw captures (youtube, articles, papers, repos, social).
- `concepts/` — atomic notes, one idea per file, every concept cites ≥1 source.
- `concepts/_clusters/` — deep-module index files bundling related concepts; pull a cluster to discover its concepts, then pull individual concepts as needed.
- `playbooks/` — workflow recipes citing concepts.
- `_inbox/` — drop zone; resolve via `/triage-inbox`.
- `skills/<name>/SKILL.md` — agent verbs (`kb-search`, `kb-pull`, `add-source`, `distill-concept`, `triage-inbox`, `rebuild-frontmatter`). When this repo is installed as a Claude Code plugin, each skill is also invocable as a slash command (`/kb-search`, etc.) — there is no separate `commands/` directory.
- `.schemas/` — JSON schemas for source/concept/playbook frontmatter.

## Curation rules (the short version)
1. **One idea per concept.** Can't summarize in one sentence → split.
2. **Soft cap 200 lines / ~1500 words.**
3. **Default to refine, not create.** New concept files require justification.
4. **Every concept cites ≥1 source.** No uncited claims.
5. **Deprecated concepts stay** with `status: deprecated` + `superseded_by`.
6. **Playbooks must list `concepts_used:`.**
7. **Bump `last_reviewed:`** on any non-trivial edit.

## Curation gate
For every new insight, pick exactly one: **Refine | Replace section | Supersede | Reject | Create**. See CONTEXT.md → "Curation gate" for definitions.

## Working in this repo
- Adding material: drop URLs in `_inbox/urls.md` or files in `_inbox/drops/`, then `/triage-inbox`.
- Distilling: `/distill-concept` applies the curation gate. Bias hard against Create.
- Searching: use the `kb-search` skill (or `/kb-search` if installed as a plugin) rather than ad-hoc grep — it knows the frontmatter conventions.
- Pulling full content: `kb-pull` skill (or `/kb-pull`).

## Don't
- Don't write architecture overviews or "how the X system works" walkthroughs as committed markdown — that's doc rot. Use `/zoom-out` or a subagent on demand. (See `concepts/just-in-time-docs.md`.)
- Don't bloat concepts with examples that belong in playbooks, or vice versa.
- Don't create a new concept file when an existing one can absorb the idea.
