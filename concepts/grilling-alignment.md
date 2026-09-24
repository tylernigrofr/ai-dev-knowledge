---
title: Grilling for alignment (instead of spec-then-code)
type: technique
phase: [planning]
tags: [prd, alignment, brooks, design-of-design]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
referenced_by:
  - concept:adr-discipline
  - concept:agent-brief-format
  - concept:design-interfaces-delegate-implementation
  - concept:doc-rot
  - concept:prd-discipline
  - concept:pre-ai-fundamentals
  - concept:systems-thinking-three-questions
  - concept:three-route-prototype
  - concept:triage-state-machine
  - playbook:idea-to-tickets
audience: [planner]
activate_when: "Starting a new feature and need to align on design before writing a PRD."
cluster: decomposition
---

## Summary
Reach a shared design concept by having the AI interview you relentlessly — one question at a time with a recommended answer — until 40–100 questions deep; the conversation is the alignment artifact, not the PRD that follows.

## Why it matters
Specs-to-code regeneration loops fail because the code is the battleground and you need eyes on it. What you actually need (per Brooks, *The Design of Design*) is a shared design concept between you and the model. Grilling produces it; reading a generated PRD does not. The PRD is just a summary — testing it tests nothing.

## How to apply
- Use a `/grill-me` skill (or `/grill-with-docs` for engineering work that should update `CONTEXT.md` and ADRs inline).
- **Ask in rounds over the design tree's frontier, each question with a recommended answer.** A round is every decision whose prerequisites are already settled, numbered. Wait for answers, recompute the frontier, and ask the next round. A question that depends on another open question waits for a later round. (Pocock's 2026 `grilling` primitive. It replaced "one question at a time".)
- **Facts are the agent's job; decisions are the user's.** If a question needs a fact from the environment, dispatch a subagent to find it rather than asking. Keep asking the rest of the frontier while it runs.
- **Challenge user terms against `CONTEXT.md` in real time.** "Your glossary defines X as A, but you seem to mean B — which is it?"
- **Sharpen fuzzy or overloaded terms.** Propose a precise canonical name when the user says "account" but means Customer-vs-User.
- **Stress-test relationships with concrete scenarios.** Invent edge cases that probe the boundary between concepts and force precision.
- **Cross-reference with code.** If the user states how something works and the code disagrees, surface the contradiction.
- **Update `CONTEXT.md` inline** as terms resolve — don't batch.
- **Offer ADRs sparingly** — only when all three apply: hard to reverse, surprising without context, real trade-off (see [adr-discipline](adr-discipline.md)).
- Done when the frontier is empty: every branch visited, nothing silently assumed, and the user confirms shared understanding.
- Summarize into a spec with `/to-spec` (formerly `/to-prd`), then `/to-tickets`. Keep grill → spec → tickets in one unbroken context, and **don't review the spec afterward**: you already aligned.
- Include an out-of-scope section in the PRD to capture negative decisions (the definition of done).
- Pull in domain experts when grilling hits a question only they can answer.

## Caveats
- Grilling is permanently human-in-the-loop. You can't Ralph-loop alignment.
- For trivial tasks, a quick discussion beats a full grilling session.

## Related
- [doc-rot](doc-rot.md) — why PRDs in the repo become dangerous over time
- [ubiquitous-language](ubiquitous-language.md) — what gets updated during grilling
- [adr-discipline](adr-discipline.md) — when grilling produces an ADR
- [prd-discipline](prd-discipline.md) — what happens to the PRD afterward
- [triage-state-machine](triage-state-machine.md) — grilling is also invoked during triage
