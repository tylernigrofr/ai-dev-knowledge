---
title: PRD discipline (out-of-scope, no self-review, no over-polish)
type: principle
phase: [planning, decomposition]
tags: [prd, alignment, definition-of-done]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:agent-brief-format
  - concept:grilling-alignment
audience: [planner]
activate_when: "Writing or reviewing a post-grilling PRD."
cluster: decomposition
---

## Summary
A post-grilling PRD exists to be decomposed, not admired: include an explicit out-of-scope section as the definition of done, do not review the summary you just had the AI generate, and stop polishing once it's actionable — the juice is in QA, not PRD perfection.

## Why it matters
Alignment happens during grilling, not during PRD reading. Re-reading the AI's summary tests nothing because LLMs are excellent summarizers — you'd just be checking for fluency. Meanwhile, the negative decisions (what you chose *not* to build) are the only durable definition of done; without them, scope creeps silently as agents discover "obvious" extensions. And every extra hour spent rewording a PRD is an hour stolen from QA, where actual quality is set.

## How to apply
- Always include an **Out of scope** section listing the negative decisions made during grilling. This is the definition of done.
- After `/to-prd` generates the doc, **do not read it for correctness** — go straight to decomposition (`/to-issues`).
- Skim only to confirm it loaded the conversation; spelling/structure don't matter.
- Stop polishing at "actionable." More PRD effort has diminishing returns.
- If the PRD feels wrong, the grilling was wrong — restart grilling, don't edit the PRD.

## Caveats
- Stakeholder-facing PRDs (legal, exec sign-off) need the polish pass. This rule is for internal engineering PRDs.
- Out-of-scope sections rot too — see `doc-rot`. Close the issue once shipped rather than keeping the PRD as a living document.

## Related
- [grilling-alignment](grilling-alignment.md) — where the real alignment happens
- [doc-rot](doc-rot.md) — why old PRDs become dangerous
- [vertical-slices](vertical-slices.md) — what the PRD decomposes into
