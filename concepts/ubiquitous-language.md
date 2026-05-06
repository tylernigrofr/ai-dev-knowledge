---
title: Ubiquitous language (CONTEXT.md / DDD)
type: principle
phase: [planning, decomposition, implementation, review]
tags: [ddd, evans, glossary, context-md]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Maintain a `CONTEXT.md` in every project that defines the domain's shared language — every term that means something specific in this codebase has a definition there, and grilling sessions keep it current.

## Why it matters
From Eric Evans's *Domain-Driven Design*. When a codebase, a PRD, and an agent all use slightly different words for the same concept (or the same word for different concepts), every conversation has friction. A `CONTEXT.md` removes the ambiguity and gives the agent a deterministic place to look up jargon. It's also the cheapest possible "module map" — the names of modules and the names of concepts converge.

## How to apply
- One `CONTEXT.md` at the repo root. No nesting.
- One section per term: term name + 1–3 sentence definition + (optional) examples + (optional) related terms.
- Updated by `/grill-with-docs` whenever a grilling session reveals a term that wasn't defined or was used inconsistently.
- Pushed to reviewers (always-on) so reviews catch terminology drift.

## Caveats
- Don't define terms that are universal (e.g. "function", "class"). Only project-specific or overloaded terms.
- A CONTEXT.md that grows past a few hundred terms suggests the codebase needs decomposition more than the doc needs editing.

## Related
- [doc-rot](doc-rot.md) — what happens when CONTEXT.md isn't kept current
- [deep-modules](deep-modules.md) — module names should match CONTEXT terms
