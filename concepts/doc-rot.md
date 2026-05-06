---
title: Doc rot in the repo
type: anti-pattern
phase: [planning, implementation]
tags: [prd, documentation, drift]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Closed PRDs left in the repo get found by future agents and used as authoritative even after the code has diverged; treat in-repo docs as living source-of-truth or remove them.

## Why it matters
Agents grep aggressively. Anything they find with a confident voice and matching keywords gets weighted as truth. A stale PRD describing a deprecated approach can override the actual code, especially when the code has no contradicting documentation. The bug surfaces as agents making "obvious" mistakes that come straight from the rotted doc.

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
