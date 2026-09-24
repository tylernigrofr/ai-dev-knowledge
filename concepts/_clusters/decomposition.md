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
  - deep-modules
  - define-errors-out-of-existence
  - dependency-categories
  - design-interfaces-delegate-implementation
  - design-it-twice
last_reviewed: 2026-09-24
---

## Seam

The shared concern: agents (and humans) work best on a single thin end-to-end slice with a clear definition of done. These concepts cover **how to frame and cut the work** — tracer bullets, DAG-style flow over phase gantt charts, throwaway prototypes to flush out unknowns, and the alignment/PRD rituals that scope the slice before code starts.

## Members

- **vertical-slices** — tracer-bullet end-to-end slices over horizontal layer-by-layer builds.
- **kanban-over-phases** — DAG of independently-grabbable issues, not a multi-phase plan.
- **three-route-prototype** — disposable prototype that splits state-machine logic from UI exploration.
- **grilling-alignment** — interview-driven alignment instead of spec-then-code; resolve branches before implementation.
- **prd-discipline** — short, scoped PRDs with explicit out-of-scope; no over-polish.
- **deep-modules** — Prefer deep modules (small interface, lots of functionality inside) over shallow modules (interface nearly as complex as the implementation).
- **define-errors-out-of-existence** — The best way to handle an error is to architect the system so the error condition is no longer exceptional — absorb it inside the module ins.
- **dependency-categories** — Before deepening a cluster of shallow modules, classify each dependency into one of four categories — in-process, local-substitutable, remot.
- **design-interfaces-delegate-implementation** — Stay personally responsible for the shape of every module's public interface — its name, signatures, and contracts — but delegate everything.
- **design-it-twice** — For any non-trivial interface, spawn 3+ sub-agents in parallel — each with a deliberately different design constraint — and compare their ou.
