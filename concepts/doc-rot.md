---
title: Doc rot in the repo
type: anti-pattern
phase: [planning, implementation]
tags: [prd, documentation, drift]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/pocock-aihero-articles.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:adr-discipline
  - concept:generate-over-depend
  - concept:grilling-alignment
  - concept:handoff-docs
  - concept:just-in-time-docs
  - concept:out-of-scope-knowledge-base
  - concept:prd-discipline
  - concept:strategic-programming
  - concept:three-route-prototype
  - concept:ubiquitous-language
  - playbook:afk-night-shift
audience: [planner, reviewer]
activate_when: "About to commit markdown docs into the repo."
counter_to: just-in-time-docs
cluster: kb-curation
---

## Summary
Closed PRDs left in the repo get found by future agents and used as authoritative even after the code has diverged; treat in-repo docs as living source-of-truth or remove them.

## Why it matters
Agents grep aggressively. Anything they find with a confident voice and matching keywords gets weighted as truth. A stale PRD describing a deprecated approach can override the actual code, especially when the code has no contradicting documentation. The bug surfaces as agents making "obvious" mistakes that come straight from the rotted doc. Pocock's framing: *outdated docs are worse than missing docs* — the LLM can't tell which to trust when grep returns five overlapping markdown files written months apart.

## How to apply
- Don't keep closed PRDs as markdown in the repo. Close them in your issue tracker and let the tracker hold the history.
- Living docs (`CONTEXT.md`, ADRs, MODULES.md, playbooks) must have a clear update lifecycle and a `last_reviewed` field.
- Auto-archive docs whose linked issues have all closed (e.g. `prds/active/` → `prds/archived/`).
- Periodic audit (`/review-staleness`) for orphaned or drift-prone docs.

## Caveats
- Aggressive deletion loses useful context. The pattern is "move out of agent grep range," not "destroy."

## Related
- [grilling-alignment](grilling-alignment.md) — why PRDs exist in the first place
- [ubiquitous-language](ubiquitous-language.md) — the canonical living-doc example
- [just-in-time-docs](just-in-time-docs.md) — the positive prescription: regenerate from code, don't commit
- [adr-discipline](adr-discipline.md) — the small set of docs that genuinely belong in the repo
