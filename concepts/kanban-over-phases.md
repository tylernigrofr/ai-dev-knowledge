---
title: Kanban (DAG) over multi-phase plans
type: principle
phase: [decomposition]
tags: [planning, parallelization, dependencies]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:sand-castle-parallelization
  - concept:triage-state-machine
audience: [planner]
activate_when: "Decomposing a PRD into work for one or many agents."
cluster: decomposition
---

## Summary
Decompose a PRD into a kanban board with explicit blocking relationships (a DAG) rather than a sequential phase-1/phase-2/phase-3 plan, so multiple agents can grab independent issues in parallel.

## Why it matters
Phase plans serialize work — only one agent can act at a time, even when most tasks are independent. A DAG of issues with `blocks`/`blocked-by` edges exposes parallelism explicitly: any node with no unmet dependencies is grabbable right now. This is the structural prerequisite for the night-shift / Sand Castle pattern; without it, parallelization has nothing to chew on.

## How to apply
- After grilling produces a PRD, run `/to-issues` to break it into independently-grabbable tickets.
- Each issue declares its dependencies. The board, not a numbered phase, defines order.
- Tag every issue as AFK or HITL (see `afk-vs-hitl`).
- The planner agent in a parallel run reads the board, picks unblocked AFK issues, dispatches them.
- QA results feed *back* onto the board as new issues — the kanban is alive throughout the project, not generated once.

## Caveats
- Some work genuinely is sequential (DB migration must precede the API that reads it). The DAG captures this honestly; phases just hide it.
- Tiny projects don't need a board. Kanban discipline pays off once you have ≥5 issues or ≥2 agents.

## Related
- [vertical-slices](vertical-slices.md) — what a good kanban node looks like
- [afk-vs-hitl](afk-vs-hitl.md) — how to tag nodes
- [ralph-loop](ralph-loop.md) — what consumes the board
- [sand-castle-parallelization](sand-castle-parallelization.md) — full parallel topology over the board
