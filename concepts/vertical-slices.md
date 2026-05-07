---
title: Vertical slices (tracer bullets) over horizontal layers
type: principle
phase: [decomposition, implementation]
tags: [decomposition, tracer-bullets, feedback-loops]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/pocock-aihero-articles.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:afk-vs-hitl
  - concept:code-first-automation
  - concept:kanban-over-phases
  - concept:prd-discipline
  - concept:pre-ai-fundamentals
  - concept:ralph-loop
  - concept:workflow-before-agents
  - playbook:afk-night-shift
audience: [planner]
activate_when: "Decomposing work into deliverable units for an agent or team."
cluster: decomposition
---

## Summary
Decompose work into thin end-to-end slices that exercise the full stack, not into horizontal layers (DB → API → frontend) that defer feedback.

## Why it matters
AI agents — and humans — gravitate toward horizontal decomposition because it's locally tidy. The cost is that you don't see anything *work* until phase 3, by which time mistakes in phase 1 have compounded. Vertical slices give you a working flow on day one and continuous feedback. They also map naturally onto independently-grabbable kanban issues for parallel agent work.

**The deeper failure mode: AI sycophancy.** Agents are trained to please, which manifests as one-shot completeness — they'd rather produce all the CRUD endpoints, request/response models, error middleware, auth, rate limiting, and logging in a single leap than build the smallest thing that proves the connection works. The Pragmatic Programmer calls this *outrunning your headlights*: building too much in the dark, without feedback to validate assumptions. Tracer bullets are the explicit antidote — force the AI to produce one tiny end-to-end slice, get feedback, *then* expand.

## How to apply
- Every issue declares a "user-observable outcome" or is tagged `internal` / `infra` / `refactor` (and that's the explicit exception).
- Reject decompositions where issues are layer-shaped ("create user table", "build user API"). Re-shape into slices ("user can sign up and see their dashboard with placeholder data").
- The first slice should be the thinnest possible end-to-end demo. Subsequent slices add features, not layers.
- Build a small eval set of "good vs bad decompositions" to tune the `/decompose` skill over time.
- Add an explicit `## Tracer Bullets` block to your Ralph-loop / build-feature prompt: "When building features, build a tiny, end-to-end slice of the feature first, seek feedback, then expand out from there." Pocock found a one-paragraph instruction was enough to flip the AI's default.

## Caveats
- Some genuine cross-cutting work (auth, infrastructure, build pipeline) is layer-shaped by nature. Tag it explicitly so it doesn't pollute the rest of the board.

## Related
- [ralph-loop](ralph-loop.md) — what the slices feed into
- [afk-vs-hitl](afk-vs-hitl.md) — tagging slices for delegation
