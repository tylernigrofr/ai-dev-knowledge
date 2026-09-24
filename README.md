# AI Dev Knowledge Base

A lean, curated knowledge base of agentic software-development practice, and of the engineering fundamentals it leans on. It's built for **agents pulling context on demand**, and readable as a wiki. It's also a Claude Code plugin.

It holds the *why* behind a workflow. The *how* lives in executable skills (e.g. [`mattpocock-skills`](https://github.com/mattpocock/skills)). Concepts explain and cross-reference the ideas; they don't restate skill procedures.

## Layout

| Path | What |
|---|---|
| `concepts/` | Atomic notes, one idea each, every one citing a source |
| `concepts/_clusters/` | Thin indexes bundling related concepts (context-management, afk-loops, decomposition…) |
| `playbooks/` | Workflow recipes that cite concepts: [orchestrated issue waves](playbooks/orchestrated-issue-waves.md), [idea → tickets](playbooks/idea-to-tickets.md), [architecture audit](playbooks/architecture-audit.md) |
| `sources/` | Raw captures (articles, repos, videos) |
| `_inbox/` | Drop zone; process with `/triage-inbox` |
| `skills/` | Plugin skills: `kb-search`, `kb-pull`, `add-source`, `distill-concept`, `triage-inbox`, `build-index`, `rebuild-frontmatter` |
| `scripts/kb.py` | Deterministic search / lint / refs / index (stdlib Python) |
| `CONTEXT.md` | Vocabulary, curation rules, frontmatter schemas. **Read first.** |
| `INDEX.md` | Generated. Don't edit. |

## Use from any project

The repo is its own marketplace:

```
/plugin marketplace add tylernigrofr/ai-dev-knowledge
/plugin install ai-dev-knowledge@ai-dev-knowledge
```

After pushing changes here, run `/plugin update ai-dev-knowledge` in Claude Code. The installed copy is a snapshot, not a live link.

Retrieval skills resolve the KB as `$AI_KB_PATH` if set, and otherwise the plugin's own directory. Maintenance skills (`add-source`, `distill-concept`, `triage-inbox`, `build-index`) write only to the live repo, so run them from inside it or set `AI_KB_PATH`.

Suggested line for `~/.claude/CLAUDE.md`:

> AI dev practices KB is installed as a plugin. Before non-trivial planning, call `kb-search`, then `kb-pull` the one or two relevant entries. Pull on demand; don't preload.

## Maintain

```bash
python3 scripts/kb.py search orchestrator worktree   # find
python3 scripts/kb.py refs                           # recompute referenced_by back-citations
python3 scripts/kb.py lint                           # frontmatter, citations, links, clusters, size cap
python3 scripts/kb.py index                          # regenerate INDEX.md
```

Add material with `/add-source <url>`, or drop URLs into `_inbox/urls.md` and run `/triage-inbox`. Every insight goes through the curation gate (Refine / Replace section / Supersede / Reject / Create). The default is Refine.
