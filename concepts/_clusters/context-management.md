---
name: context-management
description: Treating the model's context window as a managed resource — what to push, what to pull, when to reset.
type: cluster
members:
  - push-vs-pull-context
  - smart-zone-vs-dumb-zone
  - handoff-docs
  - phase-boundary-decisions
  - subagents-as-delegation
  - zoom-out
last_reviewed: 2026-09-24
---

## Seam

The shared concern: context is finite, attention degrades before tokens run out, and naive filling/compacting silently corrupts agent reasoning. These concepts together describe **a budget discipline** — what enters context (push vs pull), how full it can get before quality drops (smart/dumb zone), and how to reset cleanly (handoff, clear over compact, delegate to subagents).

## Members

- **push-vs-pull-context** — the input axis: what to inject up-front vs let the agent fetch on demand.
- **smart-zone-vs-dumb-zone** — the capacity axis: usable window is much smaller than max tokens; degrades gradually.
- **handoff-docs** — the reset protocol: write a durable brief before clearing so work survives context boundaries.
- **phase-boundary-decisions** — at each phase boundary: continue → `/clear` → handoff → subagent → `/compact` (supersedes compacting-vs-clearing).
- **subagents-as-delegation** — keep raw exploration material out of the parent context by delegating to a fresh agent.
- **zoom-out** — When you don't know an area of code, ask the agent to go up a layer of abstraction and return a map of relevant modules and callers using th.
