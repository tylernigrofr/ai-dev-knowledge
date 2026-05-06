---
title: Sand Castle parallelization pattern
type: workflow
phase: [implementation, review, qa]
tags: [parallelization, worktrees, sandboxing, kanban]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Run a planner, implementers, reviewers, and a merger as separate agents over a live kanban board — each implementer works in its own Docker-sandboxed git worktree, reviews gate every branch, the merger resolves conflicts, and concurrent QA feeds new issues back onto the board.

## Why it matters
Sequential AFK loops process one issue at a time even when ten are unblocked. Sand Castle (Pocock's `sand-castle` library) extracts the parallelism the kanban already exposes: independent implementers run simultaneously in isolated environments, and the rest of the system — review, merge, QA — runs as concurrent specialized roles. This turns a kanban board into a continuously-draining queue rather than a serial todo list.

## How to apply
Topology:

1. **Planner agent** reads the kanban board, identifies unblocked AFK-tagged issues, dispatches one per available worker.
2. **Implementer agent** runs in a sandboxed Docker container with a dedicated git worktree. Executes the Ralph loop locally. Commits to its branch.
3. **Reviewer agent** spawned per branch in a clean context, with push-style coding standards. Gates merge.
4. **Merger agent** merges approved branches, resolves type/test conflicts. Re-runs full feedback loop.
5. **QA** (human or agent) runs concurrently against the merged main; new bugs become new kanban issues — board stays alive.

Operational notes:

- One issue → one worktree → one container → one branch. Cleanup automatic on merge.
- Reviewers and implementers should use different model tiers (Opus review, Sonnet implement).
- Limit concurrency to what your CI/test infra can sustain. The merger is the bottleneck.

## Caveats
- High infra setup cost. Don't reach for this until kanban discipline + Ralph loop are working solo.
- Conflict resolution at the merger stage can still need human intervention for non-trivial overlaps.
- Sandboxing matters: agents that see each other's worktrees will hallucinate dependencies between issues.

## Related
- [ralph-loop](ralph-loop.md) — what runs inside each implementer
- [kanban-over-phases](kanban-over-phases.md) — the queue Sand Castle drains
- [clean-context-reviewer](clean-context-reviewer.md) — the review gate
- [afk-vs-hitl](afk-vs-hitl.md) — only AFK issues are eligible
