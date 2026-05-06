---
title: Vertical slices (tracer bullets) over horizontal layers
type: principle
phase: [decomposition, implementation]
tags: [decomposition, tracer-bullets, feedback-loops]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Decompose work into thin end-to-end slices that exercise the full stack, not into horizontal layers (DB → API → frontend) that defer feedback.

## Why it matters
AI agents — and humans — gravitate toward horizontal decomposition because it's locally tidy. The cost is that you don't see anything *work* until phase 3, by which time mistakes in phase 1 have compounded. Vertical slices give you a working flow on day one and continuous feedback. They also map naturally onto independently-grabbable kanban issues for parallel agent work.

## How to apply
- Every issue declares a "user-observable outcome" or is tagged `internal` / `infra` / `refactor` (and that's the explicit exception).
- Reject decompositions where issues are layer-shaped ("create user table", "build user API"). Re-shape into slices ("user can sign up and see their dashboard with placeholder data").
- The first slice should be the thinnest possible end-to-end demo. Subsequent slices add features, not layers.
- Build a small eval set of "good vs bad decompositions" to tune the `/decompose` skill over time.

## Caveats
- Some genuine cross-cutting work (auth, infrastructure, build pipeline) is layer-shaped by nature. Tag it explicitly so it doesn't pollute the rest of the board.

## Related
- [ralph-loop](ralph-loop.md) — what the slices feed into
- [afk-vs-hitl](afk-vs-hitl.md) — tagging slices for delegation
