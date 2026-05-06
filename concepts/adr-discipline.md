---
title: ADR discipline (offer sparingly)
type: principle
phase: [planning, decomposition]
tags: [adr, documentation, decisions, doc-rot]
sources: [sources/repos/pocock-skills.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Only write an Architecture Decision Record when **all three** are true: the decision is hard to reverse, it's surprising without context, and it's the result of a genuine trade-off — otherwise the ADR is noise that future agents will dutifully cite as authoritative.

## Why it matters
ADRs are the long-lived "why" memory of a codebase. Future agents and engineers will read them and treat the rationale as binding. That's the value — and the risk. An ADR that records a non-decision ("we picked Postgres") or an ephemeral preference ("we used React because the team knew it") pollutes the record and trains future readers to ignore ADRs entirely. Strict criteria keep the file count low and the signal high. Pair this with deletion of obsolete ADRs (or supersession links) to avoid doc-rot.

## How to apply
**Write an ADR only when all three apply:**

1. **Hard to reverse** — cost of changing your mind later is meaningful.
2. **Surprising without context** — a future reader will wonder "why did they do this?"
3. **Real trade-off** — there were genuine alternatives and you picked one for specific reasons.

Operational rules:

- Offer ADRs sparingly during grilling (`/grill-with-docs`). Don't produce one per session.
- Co-locate: `docs/adr/` at the root for system-wide decisions; per-context `docs/adr/` directories when a `CONTEXT-MAP.md` exists.
- Create the directory lazily — only when the first ADR is needed.
- When `/improve-codebase-architecture` surfaces a refactor that contradicts an ADR, the ADR gets surfaced explicitly and revisited only if the friction is real.
- When the user rejects an architectural candidate with a load-bearing reason, that's an ADR moment — record it so the same suggestion doesn't recur.

## Caveats
- ADRs can rot too. If a decision is reversed, supersede the old ADR rather than deleting it (link forward).
- Some teams prefer issue-tracker decisions or commit-message rationale. ADRs are the strongest form, but not the only one.

## Related
- [grilling-alignment](grilling-alignment.md) — ADR offers happen during grilling
- [ubiquitous-language](ubiquitous-language.md) — `CONTEXT.md` and ADRs are the two complementary doc artifacts
- [doc-rot](doc-rot.md) — what bad ADRs become
