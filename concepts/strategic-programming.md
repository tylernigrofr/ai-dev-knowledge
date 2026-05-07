---
title: Strategic programming over tactical programming
type: principle
phase: [planning, implementation, review]
tags: [ousterhout, complexity, technical-debt, design-investment]
sources:
  - sources/articles/gemini-ousterhout-for-ai.md
  - sources/youtube/pocock-vibe-engineering-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-05-07
referenced_by:
  - concept:deep-modules
  - concept:define-errors-out-of-existence
audience: [implementer, reviewer]
activate_when: "Tempted to ship the first thing that works without design investment."
cluster: pre-ai-foundations
---

## Summary
Spend 10–20% of every task on design investment (alternatives, naming, dependency reduction) instead of just making it work — because complexity is incremental and the "tactical tornado" who ships fast leaves a wake that drowns AI agents and humans alike.

## Why it matters
Ousterhout's central operational claim in *A Philosophy of Software Design*: complexity never arrives in one bad decision; it accumulates through hundreds of harmless-looking tactical compromises. Tactical programming optimises for "make it work, refactor later" — and the refactor never comes. Strategic programming treats every change as an investment and pays the design tax up front.

The dynamic compounds under AI. An agent reasoning about a tactically-built codebase has to load every kludge, pass-through, and obscure dependency into its smart zone before it can act. The "tactical tornado" — Ousterhout's term for the prolific developer who outputs features at 3× speed by ignoring design — was already a net negative in human-only teams. With AI agents in the loop, the cleanup cost arrives faster: the tornado's code is the code agents trip on first.

## How to apply

- **Budget 10–20% of every change for design.** Not "occasional refactoring sprints" — every PR, every task. Refine names, kill an emerging dependency, write the docstring that makes the next caller's life easier.
- **Treat working code as necessary but not sufficient.** A passing test is the floor, not the ceiling. The question is whether the next person (or agent) reading this can reason about it without holding the rest of the file in their head.
- **Watch for the tornado pattern in agent output.** AFK agents are tactical by default — they optimise for "tests green, task done." Without explicit design pressure (skills like `improve-codebase-architecture`, periodic deepening passes), they will rapidly accumulate the same wake a human tactical tornado would.
- **Make zero-tolerance the cultural default.** Ousterhout's argument is that *every* developer must hold the line — one strategic developer surrounded by tactical ones loses. In AI-augmented teams, that means the harness, the review skills, and the project's `CLAUDE.md` / `AGENTS.md` all have to encode strategic-programming pressure.
- **Notice when "I'll fix it later" is the explanation.** That phrase is the tell. If the design fix is small, do it now; if it's big, write an ADR or an issue so it isn't silently absorbed.

## Caveats
- Ousterhout uses this framing to attack Agile and TDD as actively encouraging tactical thinking. The KB takes a softer line — TDD as an agent oracle (see [tdd-for-afk](tdd-for-afk.md)) is genuinely useful even if a strict TDD culture in human-only settings can drift toward tactical short-term focus.
- The 10–20% number is a heuristic, not a measurement. The point is "non-zero and continuous," not "exactly 15%."
- For genuine throwaway prototypes ([three-route-prototype](three-route-prototype.md)), tactical mode is correct — the design investment goes into deciding which prototype survives, not polishing the discards.

## Related
- [deep-modules](deep-modules.md) — the primary artefact strategic programming produces
- [doc-rot](doc-rot.md) — what tactical comments and stale docs look like at scale
- [pre-ai-fundamentals](pre-ai-fundamentals.md) — Ousterhout sits on this reading list
- [improve-codebase-architecture](../skills/) (skill) — periodic strategic-programming pass on an existing codebase
- [tdd-for-afk](tdd-for-afk.md) — KB's nuanced stance vs. Ousterhout's TDD critique
