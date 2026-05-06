# AI Dev Knowledge Base

Curated, lean knowledge base of state-of-the-art AI-driven development practices and the proven software-engineering fundamentals they lean on. Optimized for **AI agents pulling context on demand**, browsable as a wiki as a free byproduct.

## What's in here

- **`sources/`** — raw captures (YouTube transcripts, articles, papers, repos, social posts).
- **`concepts/`** — atomic notes, one idea per file, citing sources.
- **`playbooks/`** — workflow-shaped recipes citing concepts.
- **`_inbox/`** — drop zone for unprocessed material; `/triage-inbox` resolves it.
- **`skills/`** — agent-facing verbs (`kb-search`, `kb-pull`, `add-source`, `distill-concept`, `triage-inbox`, `build-index`).
- **`CONTEXT.md`** — ubiquitous-language doc + curation rules + frontmatter schemas. **Read this first.**
- **`INDEX.md`** — auto-generated index. Regenerate with `/build-index`.

## How to use it (human)

- Browse `concepts/` and `playbooks/` directly, or open `INDEX.md`.
- Add new material by dropping URLs in `_inbox/urls.md` or files in `_inbox/drops/`. Then run `/triage-inbox`.

## How to use it (agent, from another project)

1. Ensure `AI_KB_PATH` is set in your shell to this repo's absolute path.
2. In your project's `CLAUDE.md`, add:
   > AI dev best practices live at `$AI_KB_PATH/`. Search `concepts/` and `playbooks/` by frontmatter tag/type/phase. Use the `kb-search` skill if installed.
3. Optionally copy or symlink `skills/kb-search.md` and `skills/kb-pull.md` into your project's `.claude/skills/`.

## Spec & design

- [Design spec](docs/superpowers/specs/2026-05-06-ai-dev-knowledge-base-design.md)
- [Phase 1+2 implementation plan](docs/superpowers/plans/2026-05-06-ai-dev-knowledge-base-phase-1-and-2.md)

## Curation philosophy

Lean over comprehensive. Default to refining existing concepts, not creating new ones. Every concept cites a source. Periodic audit (`/review-staleness`, future) prunes bloat. See `CONTEXT.md` for the full rules.
