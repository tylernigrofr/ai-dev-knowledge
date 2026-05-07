---
title: The three systems-thinking questions (state, feedback, blast radius)
type: technique
phase: [planning, review]
tags: [systems-thinking, design, review-checklist, theory-building]
sources: [sources/youtube/hak-only-skill-left-2026.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-07
audience: [planner, implementer, reviewer]
activate_when: "Reviewing AI-generated code or a vibe-coded feature before it ships, or sketching a system before prompting."
counter_to: null
cluster: null
referenced_by:
  - concept:llm-not-a-trustworthy-abstraction
---

## Summary
Three questions you should be able to answer about any system *without running the code*: where does state live, where does feedback live, and what breaks if you delete this. Failing any one of them means you don't yet have the theory of the program — only its shadow.

## Why it matters
Hak's audits of AI-built apps (e.g. a Lovable product live with paying customers, ~7,000-line single file, empty logs, no rate limiting) showed every catastrophic failure mode was a *systems-thinking* failure, not a coding one. The pattern: state was duplicated across components with no single owner, nothing surfaced when things went wrong, and nobody could trace what depended on what. AI generated each piece competently while the whole was incoherent. These three questions catch the failure mode before customers do.

## How to apply
For each meaningful component or feature, force an answer:

1. **Where does state live?** Who owns the truth? If two pieces each think they own it, that's a bug not yet triggered. Name the owner explicitly.
2. **Where does feedback live?** What tells you it's working — logs, metrics, errors, traces? If nothing surfaces, the system is *pretending* to work, and you'll learn it's broken from a customer.
3. **What breaks if I delete this?** Trace the blast radius in your head before touching. "I don't know" is the answer that becomes your study list.

Use them as:
- A pre-prompt sketch (boxes for components, arrows for data flow, mark state and failure surfaces).
- A code-review checklist for any AI-generated PR.
- A spec-writing prompt — answer all three before writing the spec.

## Caveats
- For genuine throwaway prototypes the bar is lower — but if a non-technical founder is shipping to paying customers, the bar is the same as for senior-built software.
- The questions don't substitute for domain expertise. They surface *whether* a theory exists, not whether it's correct.

## Related
- [llm-not-a-trustworthy-abstraction](llm-not-a-trustworthy-abstraction.md) — why this discipline can't be skipped.
- [deep-modules](deep-modules.md) — designing components whose blast radius is small.
- [grilling-alignment](grilling-alignment.md) — surfacing the theory through interrogation before coding.
- [zoom-out](zoom-out.md) — on-demand structural map when an answer is "I don't know."
