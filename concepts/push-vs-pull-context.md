---
title: Push vs pull context
type: principle
phase: [implementation, review]
tags: [context-management, skills, system-prompt]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
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

## Caveats
- An implementer that fails to pull a relevant skill is worse than one with the skill pushed. Monitor pull behavior; if a skill is missed often, consider pushing it.

## Related
- [clean-context-reviewer](clean-context-reviewer.md) — the canonical push consumer
- [ralph-loop](ralph-loop.md) — where push/pull discipline applies
