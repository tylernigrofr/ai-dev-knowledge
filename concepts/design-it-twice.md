---
title: Design it twice (parallel sub-agent interface design)
type: technique
phase: [planning, implementation]
tags: [ousterhout, interface-design, subagents, architecture]
sources:
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:dependency-categories
audience: [planner, implementer]
activate_when: "Designing a non-trivial interface before implementation."
cluster: decomposition
---

## Summary
For any non-trivial interface, spawn 3+ sub-agents in parallel — each with a deliberately different design constraint — and compare their outputs before picking one (or hybridizing). Your first interface idea is rarely the best, and parallel sub-agents make "design it twice" cheap.

## Why it matters
Ousterhout's *A Philosophy of Software Design* recommends drafting two genuinely different designs before implementing because the second one almost always reveals constraints the first missed. The cost used to be human time; now it's a few minutes of parallel sub-agent work. The trick is to give each sub-agent a *different* explicit constraint so they don't converge on the same shape — and to brief each one with the architecture vocabulary ([deep-modules](deep-modules.md)) and the project's domain language ([ubiquitous-language](ubiquitous-language.md)) so the comparison is on substance, not naming.

## How to apply
- Frame the problem space first: constraints, dependency categories ([dependency-categories](dependency-categories.md)), an illustrative code sketch (not a proposal). Show this to the user; they read while sub-agents work.
- Spawn 3+ sub-agents *in parallel* with separate technical briefs and divergent constraints:
  - Agent 1: minimize the interface (1–3 entry points; max leverage per entry).
  - Agent 2: maximize flexibility and extension.
  - Agent 3: optimize the most common caller (default case is trivial).
  - Agent 4 (if cross-seam): ports & adapters around external dependencies.
- Each sub-agent outputs: (1) interface with invariants/ordering/errors, (2) usage example, (3) what's hidden behind the seam, (4) dependency strategy/adapters, (5) trade-offs.
- Present designs sequentially, then compare in prose along three axes: **depth** (leverage at the interface), **locality** (where change concentrates), **seam placement**.
- Be opinionated. End with a recommendation — or a hybrid combining the strongest elements. The user wants a strong read, not a menu.

## Caveats
- Don't run this for trivial interfaces. The setup overhead exceeds the benefit when there's only one obvious shape.
- If two sub-agents produce near-identical designs, the briefs weren't divergent enough — re-prompt with sharper constraints.

## Related
- [subagents-as-delegation](subagents-as-delegation.md) — the underlying mechanism
- [deep-modules](deep-modules.md) — vocabulary and depth metric used to compare designs
- [dependency-categories](dependency-categories.md) — what each sub-agent must reason about for cross-seam deps
- [pre-ai-fundamentals](pre-ai-fundamentals.md) — Ousterhout source
