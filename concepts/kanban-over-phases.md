---
title: Kanban (DAG) over multi-phase plans
type: principle
phase: [decomposition]
tags: [planning, parallelization, dependencies]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/repos/pocock-skills.md
  - sources/repos/owner-practice-2026.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
referenced_by:
  - concept:orchestrator-worker-dispatch
  - concept:sand-castle-parallelization
  - concept:triage-state-machine
  - playbook:idea-to-tickets
  - playbook:orchestrated-issue-waves
audience: [planner]
activate_when: "Decomposing a PRD into work for one or many agents."
cluster: decomposition
---

## Summary
Decompose a PRD into a kanban board with explicit blocking relationships (a DAG) rather than a sequential phase-1/phase-2/phase-3 plan, so multiple agents can grab independent issues in parallel.

## Why it matters
Phase plans serialize work — only one agent can act at a time, even when most tasks are independent. A DAG of issues with `blocks`/`blocked-by` edges exposes parallelism explicitly: any node with no unmet dependencies is grabbable right now. This is the structural prerequisite for the night-shift / Sand Castle pattern; without it, parallelization has nothing to chew on.

## How to apply
- After grilling produces a spec, run `/to-tickets` (formerly `/to-issues`) to break it into tracer-bullet tickets, each sized for one fresh context window.
- Each ticket declares its **blocking edges**. On GitHub, publish blockers first and use native issue dependencies / sub-issues, not just prose. The board, not a numbered phase, defines order.
- Work the **frontier**: every ticket whose blockers are all closed.
- **Wide refactors are the exception to vertical slicing.** Sequence them as expand (add the new form beside the old) → migrate call sites in batches, each its own ticket → contract (delete the old form once no caller remains).
- Tag every issue as AFK or HITL (see `afk-vs-hitl`).
- The orchestrator reads the board and dispatches the frontier in dependency-aware waves (see [orchestrator-worker-dispatch](orchestrator-worker-dispatch.md)).
- QA results feed *back* onto the board as new issues — the kanban is alive throughout the project, not generated once.

## Caveats
- Some work genuinely is sequential (DB migration must precede the API that reads it). The DAG captures this honestly; phases just hide it.
- Tiny projects don't need a board. Kanban discipline pays off once you have ≥5 issues or ≥2 agents.

## Related
- [vertical-slices](vertical-slices.md) — what a good kanban node looks like
- [afk-vs-hitl](afk-vs-hitl.md) — how to tag nodes
- [ralph-loop](ralph-loop.md) — what consumes the board
- [orchestrator-worker-dispatch](orchestrator-worker-dispatch.md): the parallel topology over the board
