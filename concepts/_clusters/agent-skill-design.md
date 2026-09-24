---
name: agent-skill-design
description: Designing skills/verbs an agent can pull on demand — deep modules, progressive disclosure, frontmatter conventions.
type: cluster
members:
  - deep-modules
  - design-interfaces-delegate-implementation
  - design-it-twice
  - strategic-programming
  - dependency-categories
  - agent-loop-simplicity
  - workflow-before-agents
last_reviewed: 2026-09-24
---

## Seam

The shared concern: a skill (or any agent-facing module) is a **deep module** with a small interface and rich behavior, pulled into context only when needed. These concepts give the design vocabulary — depth, interface-vs-implementation, designing twice, strategic investment — and the dependency taxonomy that determines what a skill can safely abstract over.

## Members

- **deep-modules** — small interface, large implementation; the core unit of agent-friendly design.
- **design-interfaces-delegate-implementation** — you own the seams; delegate the body to the agent or a subagent.
- **design-it-twice** — sketch two interface variants in parallel before committing.
- **strategic-programming** — invest in design instead of patching tactically; applies hard to skill libraries that compound.
- **dependency-categories** — in-process / local-substitutable / remote-owned / true-external; the seams a skill can hide.
- **agent-loop-simplicity** — The entire architecture of a capable LLM agent is a ~9-line loop: call the model, print output, handle tool calls, feed results back — with .
- **workflow-before-agents** — Reach for autonomous agents only after simpler workflow patterns fail — each step up the complexity ladder (single prompt → chaining → routi.
