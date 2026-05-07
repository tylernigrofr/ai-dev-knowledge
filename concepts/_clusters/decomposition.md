---
name: decomposition
description: Slicing work so each unit is small, end-to-end, and shippable — the antidote to horizontal phase plans.
type: cluster
members:
  - vertical-slices
  - kanban-over-phases
  - three-route-prototype
  - grilling-alignment
  - prd-discipline
last_reviewed: 2026-05-07
---

## Seam

The shared concern: agents (and humans) work best on a single thin end-to-end slice with a clear definition of done. These concepts cover **how to frame and cut the work** — tracer bullets, DAG-style flow over phase gantt charts, throwaway prototypes to flush out unknowns, and the alignment/PRD rituals that scope the slice before code starts.

## Members

- **vertical-slices** — tracer-bullet end-to-end slices over horizontal layer-by-layer builds.
- **kanban-over-phases** — DAG of independently-grabbable issues, not a multi-phase plan.
- **three-route-prototype** — disposable prototype that splits state-machine logic from UI exploration.
- **grilling-alignment** — interview-driven alignment instead of spec-then-code; resolve branches before implementation.
- **prd-discipline** — short, scoped PRDs with explicit out-of-scope; no over-polish.
