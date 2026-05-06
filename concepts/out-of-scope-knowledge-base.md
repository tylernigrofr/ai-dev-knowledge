---
title: Out-of-scope knowledge base (.out-of-scope/)
type: technique
phase: [decomposition, qa]
tags: [triage, wontfix, institutional-memory, deduplication]
sources:
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Keep a `.out-of-scope/` directory in the repo with one file per *concept* (not per issue) explaining why a feature was rejected, the reasoning, and a list of all prior issues that requested it — so future triage can spot duplicates and surface the prior decision instead of re-litigating it.

## Why it matters
Closing an enhancement as `wontfix` loses the reasoning. Six months later the same request comes in worded slightly differently, the maintainer has forgotten the prior discussion, and the whole conversation happens again. A persistent file solves both halves of the problem: institutional memory (the *why*, written when it's fresh) and deduplication (a place for the triage skill to grep before grilling). One file per concept means three different "dark mode" issues collapse into one record with a `Prior requests` list.

## How to apply
- **One file per concept**, kebab-case names: `dark-mode.md`, `plugin-system.md`, `graphql-api.md`.
- **Format**: short design-doc style — `# Concept Name`, `## Why this is out of scope` (substantive paragraphs, optional code samples), `## Prior requests` with issue links.
- **Substantive reasons only.** Reference project scope/philosophy, technical constraints, or strategic decisions — never "we're too busy right now" (that's a deferral, not a rejection).
- **Triage flow:**
  1. During Step 1 of triage, read every file in `.out-of-scope/`.
  2. Match new issues by *concept similarity*, not keyword — "night theme" matches `dark-mode.md`.
  3. On match, surface to maintainer: *"This is similar to `.out-of-scope/dark-mode.md` — we rejected this before because [reason]. Do you still feel the same way?"*
  4. Maintainer **confirms** → append to Prior requests, close. **Reconsiders** → delete/update the file, proceed with normal triage. **Disagrees** → distinct issue, normal triage.
- **Only enhancements** go here, never bugs.
- If the maintainer changes their mind, delete the file. Don't reopen old issues — they're historical records.

## Caveats
- Concept-similarity matching is human-confirmed, not automated. The skill surfaces candidates; the maintainer judges.
- The directory should *not* be a graveyard of every closed issue. Only enhancements with durable, reusable rationale belong.

## Related
- [triage-state-machine](triage-state-machine.md) — `wontfix` for enhancements writes here
- [adr-discipline](adr-discipline.md) — sister institution for *included* decisions
- [doc-rot](doc-rot.md) — why decision-bearing docs belong in the repo, ephemeral PRDs don't
