---
title: Pre-AI software engineering books map onto AI workflows
type: mental-model
phase: [planning, implementation, review]
tags: [reading-list, fundamentals, modularity, refactoring]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Old software engineering books on modularity, tracer bullets, refactoring, and pragmatic programming describe exactly what AI agents need to do good work — buy the classics rather than chasing AI-specific blog posts.

## Why it matters
Every "AI engineering best practice" Pocock surfaces — deep modules, vertical slices, ubiquitous language, clean interfaces, fast feedback loops — was already named and explored decades ago by engineers solving the same underlying problem: how do you make a codebase that humans (or now agents) of bounded context can reason about? AI didn't change the fundamentals; it just made the cost of *not* applying them explicit. Reading the originals gives you the mental models in their cleanest form, plus the vocabulary to recognize when an "AI problem" is really an old, solved problem.

## How to apply
Recommended reading list (load-bearing for this KB):

- **John Ousterhout — *A Philosophy of Software Design***. Deep modules vs. shallow modules. Foundational for [deep-modules](deep-modules.md).
- **Andy Hunt & Dave Thomas — *The Pragmatic Programmer***. Tracer bullets — direct ancestor of [vertical-slices](vertical-slices.md).
- **Eric Evans — *Domain-Driven Design***. Ubiquitous language — basis for [ubiquitous-language](ubiquitous-language.md).
- **Frederick Brooks — *The Design of Design***. Shared design concept — what [grilling-alignment](grilling-alignment.md) produces.
- **Martin Fowler — *Refactoring***. The vocabulary for the cleanup pass after AI generation.
- **Kent Beck — *Test-Driven Development: By Example***. Red-green-refactor — basis for [tdd-for-afk](tdd-for-afk.md).

## Caveats
- The books predate LLMs; you have to do the translation. The mappings are obvious once you start, but don't expect chapter-by-chapter applicability.
- Some advice (e.g. heavy upfront design docs) needs adapting for AI's fast iteration loop.

## Related
- [deep-modules](deep-modules.md), [vertical-slices](vertical-slices.md), [ubiquitous-language](ubiquitous-language.md), [grilling-alignment](grilling-alignment.md), [tdd-for-afk](tdd-for-afk.md)
