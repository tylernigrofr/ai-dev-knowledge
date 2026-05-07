---
title: Zoom out for unfamiliar code
type: technique
phase: [planning, implementation, review]
tags: [exploration, abstraction, mental-map, domain-glossary]
sources: [sources/repos/pocock-skills.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:just-in-time-docs
  - concept:systems-thinking-three-questions
audience: [planner, implementer]
activate_when: "Entering an unfamiliar area of code and need a map first."
cluster: context-management
---

## Summary
When you don't know an area of code, ask the agent to go up a layer of abstraction and return a map of relevant modules and callers using the project's domain-glossary vocabulary — instead of jumping straight into the file under your cursor.

## Why it matters
Agents (and engineers) default to depth-first exploration: open the file, follow the import, follow that import, lose the plot. By the time you're four hops deep you've burned context and still don't know how the area fits in. A deliberate zoom-out forces breadth-first orientation: which modules participate, what calls what, what does it look like in the language of the domain. The map is cheap and re-orients fast.

## How to apply
- Invoke `/zoom-out` (Pocock's skill is one line: "Go up a layer of abstraction. Give me a map of all relevant modules and callers, using the project's domain glossary vocabulary").
- Make it user-invoked, not auto-triggered (the skill is `disable-model-invocation: true`).
- Require domain-language naming. "The Order intake module" not "the FooBarHandler."
- Reach for it before grilling, before debugging an unfamiliar area, and before reviewing a PR that touches code you don't routinely work in.

## Caveats
- Only as good as the domain glossary. With no `CONTEXT.md`, you get generic module names and the technique loses most of its value.
- For tiny codebases, zoom-out is overkill — depth-first is fine when the whole map fits in your head.

## Related
- [ubiquitous-language](ubiquitous-language.md) — the vocabulary zoom-out uses
- [subagents-as-delegation](subagents-as-delegation.md) — a natural delegation target for the map-building work
