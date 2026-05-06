---
title: Grilling for alignment (instead of spec-then-code)
type: technique
phase: [planning]
tags: [prd, alignment, brooks, design-of-design]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Reach a shared design concept by having the AI interview you relentlessly — one question at a time with a recommended answer — until 40–100 questions deep; the conversation is the alignment artifact, not the PRD that follows.

## Why it matters
Specs-to-code regeneration loops fail because the code is the battleground and you need eyes on it. What you actually need (per Brooks, *The Design of Design*) is a shared design concept between you and the model. Grilling produces it; reading a generated PRD does not. The PRD is just a summary — testing it tests nothing.

## How to apply
- Use a `/grill-me` skill (or `/grill-with-docs` for engineering work that should update `CONTEXT.md` and ADRs inline).
- Constrain to one question at a time, each with a recommended answer.
- Stop when novelty dies (three consecutive low-novelty questions) or you hit ~40 questions.
- Summarize into a PRD with a `/to-prd` skill — but **do not review the PRD afterward**. You already aligned.
- Include an out-of-scope section in the PRD to capture negative decisions (the definition of done).
- Pull in domain experts when grilling hits a question only they can answer.

## Caveats
- Grilling is permanently human-in-the-loop. You can't Ralph-loop alignment.
- For trivial tasks, a quick discussion beats a full grilling session.

## Related
- [doc-rot](doc-rot.md) — why PRDs in the repo become dangerous over time
- [ubiquitous-language](ubiquitous-language.md) — what gets updated during grilling
