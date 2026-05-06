---
title: AFK vs human-in-the-loop tagging
type: technique
phase: [decomposition]
tags: [delegation, tagging, kanban]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/willison-designing-agentic-loops.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Tag every issue as either AFK (delegate-able to an agent unsupervised) or human-in-the-loop (needs your judgment); the AFK queue feeds the night shift, HITL stays on your desk.

## Why it matters
Without explicit tagging, you either over-delegate (agents make decisions that need human judgment) or under-delegate (you stay in the loop on issues you don't need to be). Explicit tagging at decomposition time forces the question "can this be done unsupervised?" and produces a board where the night shift knows what it's allowed to grab.

## How to apply
- Add `mode: afk | human-in-loop` to every issue's frontmatter.
- Default to HITL; require justification to mark AFK (clear acceptance criteria, no ambiguous design questions, well-bounded scope).
- **Variation-heavy signal (Willison):** if your gut reaction to a task is "ugh, I'm going to have to try a lot of variations here" — debugging, perf tuning, dependency upgrades — that's a strong AFK indicator. Repetitive iteration with automated feedback = agent's home turf.
- The Ralph loop only picks issues with `mode: afk`.
- Re-tag freely as you learn — issues that the night shift keeps tripping over should be flipped to HITL.

## Caveats
- Some issues are partially delegate-able. Either split them, or tag conservatively as HITL.

## Related
- [vertical-slices](vertical-slices.md) — what's being tagged
- [ralph-loop](ralph-loop.md) — the AFK consumer
