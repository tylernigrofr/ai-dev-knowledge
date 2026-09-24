---
title: Zoom out for unfamiliar code
type: technique
phase: [planning, implementation, review]
tags: [exploration, abstraction, mental-map, domain-glossary]
sources: [sources/repos/pocock-skills.md]
status: stable
superseded_by: null
last_reviewed: 2026-09-24
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
- Pocock removed `/zoom-out` from his skills in 2026 because it "went unused in practice" — the move is now usually a subagent exploration or the survey step of `/improve-codebase-architecture`. The idea still holds; the dedicated command doesn't earn its slot.
- For tiny codebases, zoom-out is overkill — depth-first is fine when the whole map fits in your head.

## Related
- [ubiquitous-language](ubiquitous-language.md) — the vocabulary zoom-out uses
- [subagents-as-delegation](subagents-as-delegation.md) — a natural delegation target for the map-building work
