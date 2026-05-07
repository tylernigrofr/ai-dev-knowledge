---
name: context-management
description: Treating the model's context window as a managed resource — what to push, what to pull, when to reset.
type: cluster
members:
  - push-vs-pull-context
  - smart-zone-vs-dumb-zone
  - handoff-docs
  - compacting-vs-clearing
  - subagents-as-delegation
last_reviewed: 2026-05-07
---

## Seam

The shared concern: context is finite, attention degrades before tokens run out, and naive filling/compacting silently corrupts agent reasoning. These concepts together describe **a budget discipline** — what enters context (push vs pull), how full it can get before quality drops (smart/dumb zone), and how to reset cleanly (handoff, clear over compact, delegate to subagents).

## Members

- **push-vs-pull-context** — the input axis: what to inject up-front vs let the agent fetch on demand.
- **smart-zone-vs-dumb-zone** — the capacity axis: usable window is much smaller than max tokens; degrades gradually.
- **handoff-docs** — the reset protocol: write a durable brief before clearing so work survives context boundaries.
- **compacting-vs-clearing** — bias toward `/clear` + handoff over lossy auto-compact for substantive work.
- **subagents-as-delegation** — keep raw exploration material out of the parent context by delegating to a fresh agent.
