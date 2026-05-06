---
title: Deep modules over shallow modules
type: principle
phase: [planning, implementation]
tags: [architecture, ousterhout, testability, module-design]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Prefer deep modules (small interface, lots of functionality inside) over shallow modules (lots of tiny files with sprawled dependencies); deep modules let you draw clean test boundaries around real functionality.

## Why it matters
From Ousterhout's *A Philosophy of Software Design*. Shallow modules force you into mocking hell or testing nothing meaningful — and AI agents amplify the cost because they reason worse about scattered, tightly-coupled code. Deep modules give you a stable interface to test against, a small surface for the AI to reason about, and the ability to refactor internals without consumer changes.

## How to apply
- For each cluster of related code, identify the smallest reasonable public interface and hide everything else.
- Run something like `/improve-codebase-architecture` periodically to detect shallow-module clusters and propose consolidations.
- Maintain a canonical interface doc (e.g. `MODULES.md` or a section of `CONTEXT.md`) and treat divergence as a bug.
- Design module interfaces yourself; delegate the implementation. This keeps your mental map intact.

## Caveats
- "Deep" is not "huge." A 5000-line file is rarely a good module. The metric is interface narrowness vs. internal richness, not raw size.
- Forced consolidation across genuinely independent concerns creates worse coupling than the shallow case it replaces.

## Related
- [ubiquitous-language](ubiquitous-language.md) — what module names should match
- [push-vs-pull-context](push-vs-pull-context.md) — module map is canonical push content
