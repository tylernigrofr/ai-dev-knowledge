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

### Recommended: install as a Claude Code plugin

This repo ships a `.claude-plugin/plugin.json` so Claude Code can load it globally.

1. Set `AI_KB_PATH` to this repo's absolute path (so the skills can locate the KB content):
   ```powershell
   [Environment]::SetEnvironmentVariable("AI_KB_PATH", "$env:USERPROFILE\OneDrive\Documents\GitHub\ai-dev-knowledge", "User")
   ```
2. In Claude Code, install the plugin from this local path (or the GitHub URL):
   ```
   /plugin install <path-to-this-repo>
   ```
3. Add 1–2 lines to your global `~/.claude/CLAUDE.md`:
   > AI dev best practices KB is installed as a plugin. Before non-trivial planning or context-heavy work, call `kb-search` to find relevant concepts/playbooks, then `kb-pull` for full content. Pull on demand — don't preload.

You'll get the `kb-search` / `kb-pull` skills (auto-invoked when relevant) plus `/kb-search`, `/kb-pull`, `/triage-inbox`, `/add-source`, `/distill-concept`, `/build-index` slash commands available in every project.

Context cost is negligible — only skill names + descriptions load upfront; concept/playbook bodies are pulled on demand.

### Alternative: manual symlink

If you don't want the plugin: symlink `skills/kb-search.md` and `skills/kb-pull.md` into `~/.claude/skills/` and add the same global CLAUDE.md pointer.

## Spec & design

- [Design spec](docs/superpowers/specs/2026-05-06-ai-dev-knowledge-base-design.md)
- [Phase 1+2 implementation plan](docs/superpowers/plans/2026-05-06-ai-dev-knowledge-base-phase-1-and-2.md)

## Curation philosophy

Lean over comprehensive. Default to refining existing concepts, not creating new ones. Every concept cites a source. Periodic audit (`/review-staleness`, future) prunes bloat. See `CONTEXT.md` for the full rules.
