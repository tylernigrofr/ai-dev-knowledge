---
title: Just-in-time AI-generated docs (over committed markdown)
type: principle
phase: [planning, implementation, review]
tags: [documentation, doc-rot, exploration]
sources: [sources/articles/pocock-aihero-articles.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:doc-rot
audience: [planner, reviewer]
activate_when: "Tempted to commit an architecture overview as markdown."
cluster: kb-curation
---

## Summary
Instead of stuffing a repo with markdown that drifts out of sync, let the AI generate exploration docs on demand during each session — the docs are derived freshly from the current code so they can't go stale, and only the small set of decision-bearing artifacts (`CONTEXT.md`, ADRs, agent briefs) are kept committed.

## Why it matters
Outdated docs are worse than missing docs because the LLM can't tell which to trust. When grep returns five overlapping markdown files written months apart, the agent picks one — often the most authoritative-sounding, regardless of currentness — and proceeds confidently down the wrong path. Just-in-time docs sidestep the problem: the agent reads the *code* and writes a fresh map for *this* session, then discards it. The artifacts that *do* live in the repo are the ones whose value is precisely their permanence: glossary, decisions, scope boundaries.

## How to apply
- Keep committed: `CONTEXT.md` (glossary), `docs/adr/` (decisions), agent briefs on tracker issues, scope boundaries (`.out-of-scope/`).
- Don't keep committed: architecture overviews, "how the X system works" walkthroughs, status snapshots, retrospectives, planning docs from finished work.
- When the agent needs a map of an area, invoke `/zoom-out` or a subagent — let it read the code and produce a fresh summary in-context.
- For PRDs: write them on the issue tracker (where they get closed), not as repo markdown that lingers.
- When you do find old docs, evaluate: is this load-bearing, or could it be regenerated? If regeneratable, delete.

## Caveats
- New contributors (human or agent) benefit from at least *some* committed orientation. `README.md` and `CONTEXT.md` are not "doc rot."
- Just-in-time docs are session-local — if a fresh agent will need the same map, *they* re-derive it. Pay the small cost; avoid the staleness tax.
- For genuinely complex systems, an ADR explaining "why this architecture" is worth keeping (see [adr-discipline](adr-discipline.md)).

## Related
- [doc-rot](doc-rot.md) — the antipattern this prevents
- [zoom-out](zoom-out.md) — the on-demand mapping move
- [adr-discipline](adr-discipline.md) — the durable artifacts that *do* belong in the repo
- [ubiquitous-language](ubiquitous-language.md) — `CONTEXT.md` is the other durable artifact
