---
title: Push vs pull context
type: principle
phase: [implementation, review]
tags: [context-management, skills, system-prompt]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/anthropic-context-engineering.md
  - sources/articles/anthropic-claude-code-best-practices.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Push context = always-on instructions sent every turn (CLAUDE.md, system prompt). Pull context = on-demand fetched by the agent (skills with description headers). Push for reviewer, pull for implementer.

## Why it matters
Push tokens are spent every turn whether or not they're relevant — cheap when always-needed, wasteful otherwise. Pull tokens are spent only when the agent decides they're needed — efficient on average but only useful if the agent actually pulls. Reviewers want every relevant standard *every time* (push). Implementers want a clean working context plus the option to pull skills as needed (pull).

## How to apply
- Reviewer system prompt: concatenate everything in `push/` (coding standards, `CONTEXT.md`, ADRs, module map) ordered by priority; truncate from the bottom if over budget.
- Implementer system prompt: minimal — task description + tool to discover and pull from `skills/`.
- Skills used in pull mode must have a clear `description:` header so the agent's discovery step knows when to pull them.
- Anything pushed should justify being pushed every turn; otherwise demote to pull.
- A third mode: **just-in-time via tools** — agent maintains lightweight identifiers (file paths, stored queries, web links) and loads data at runtime only when needed. Better than pull for large datasets or volatile content that would waste tokens if pre-loaded. Claude Code's database analysis pattern is the canonical example: write a targeted query, run it, process the result — don't load the full dataset.

### CLAUDE.md bloat is the canonical push anti-pattern

A CLAUDE.md that is too long defeats itself: important rules get lost in the noise and Claude ignores them. Symptoms: Claude keeps doing the thing the file tells it not to, or asks questions the file already answers.

Pruning heuristic (from Anthropic's own guidance): *"Would removing this line cause Claude to make mistakes?"* If no, cut it. What belongs in CLAUDE.md (push):
- Bash commands Claude can't guess from code
- Code style rules that differ from language defaults
- Non-obvious env-var requirements, repo etiquette, known gotchas

What doesn't belong:
- Things Claude can figure out by reading the codebase
- Standard language conventions Claude already knows
- Detailed API docs (link instead)
- Frequently-changing information
- File-by-file codebase descriptions

Check CLAUDE.md into git; treat it like code — review when Claude's behavior goes wrong, prune on a schedule.

## Caveats
- An implementer that fails to pull a relevant skill is worse than one with the skill pushed. Monitor pull behavior; if a skill is missed often, consider pushing it.
- CLAUDE.md can import other files via `@path/to/file` syntax, which helps modularize push context without duplicating it.

## Related
- [clean-context-reviewer](clean-context-reviewer.md) — the canonical push consumer
- [ralph-loop](ralph-loop.md) — where push/pull discipline applies
