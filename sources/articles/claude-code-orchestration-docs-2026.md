---
title: "Claude Code docs — subagents, worktree isolation, workflows, agent teams, code review, routines (2026-09 snapshot)"
type: article
url: https://code.claude.com/docs/en/agents
author: Anthropic
published: 2026-09-24
captured: 2026-09-24
status: extracted
concepts_seeded:
  - orchestrator-worker-dispatch
  - clean-context-reviewer
  - ralph-loop
---

# Claude Code orchestration features (as of 2026-09-24)

Captured by a research subagent from the docs; the third-party changelog items are flagged.

- **Subagents** (https://code.claude.com/docs/en/sub-agents): background by default; `isolation: worktree` per agent file or per call (branches from the default branch; auto-cleaned if unchanged, the GC hazard documented in `sources/repos/owner-practice-2026.md`). New frontmatter includes `memory:`, `skills:` (preloaded), `maxTurns`, `effort`, `background`, `omitClaudeMd`. Nesting up to 3 levels, ~20 concurrent. `SendMessage` resumes a subagent by name/id.
- **Dynamic workflows** (https://code.claude.com/docs/en/workflows, research preview ~2026-06): Claude writes a JS script using `agent()` / `pipeline()` / `parallel()`; the *script* holds the loop and intermediate results instead of the orchestrator's context, and runs are resumable. 16 concurrent agents by default; saved scripts in `.claude/workflows/` run as `/<name>`. Recommended for audits, migrations, cross-checked research. Orchestrator context hygiene is the stated reason: "many subagents returning detailed results" floods the parent.
- **Agent teams** (https://code.claude.com/docs/en/agent-teams, experimental): start with 3–5 teammates; teammates do *not* get separate worktrees, so split work by file; `TaskCompleted` / `TeammateIdle` hooks as quality gates.
- **`/batch`**: bundled skill that splits one large change across 5–30 worktree-isolated subagents, each opening its own PR.
- **`/code-review`** (https://code.claude.com/docs/en/code-review): runs as a background subagent with effort `low`…`max`, plus `ultra` (multi-agent cloud review); `--fix`, `--comment`. Managed Code Review adds a verification pass to filter false positives and reads `REVIEW.md`; its check run is neutral (never blocks merge).
- **Routines** (https://code.claude.com/docs/en/routines): cloud sessions triggered by schedule, API, or GitHub events; `/schedule`. Documented uses: nightly backlog grooming, PR review.
- AGENTS.md is read as a fallback to CLAUDE.md (per third-party changelog, https://www.gradually.ai/en/changelogs/claude-code/).
- Anthropic session guidance (https://claude.com/blog/using-claude-code-session-management-and-1m-context, 2026-04-15): talks about "context rot" rather than a fixed number; new session per task; prefer `/rewind` over stacking corrections; "the model is at its least intelligent point when compacting."
