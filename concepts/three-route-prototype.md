---
title: Three-route throwaway prototype (front-end)
type: technique
phase: [planning, implementation]
tags: [frontend, prototyping, multimodal-blindness]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
For UI work in mature codebases, don't try to one-shot a polished design — scaffold three throwaway routes with variant designs, click between them, pick what works, then grill the real implementation.

## Why it matters
AI is multimodal-blind on visual judgment. It can produce plausible UI code but cannot tell you which of three options actually feels right. The throwaway-routes pattern moves the visual judgment to a human (you), where it belongs, while still letting the AI generate the variants. Picking from three concrete options is dramatically more productive than describing what you want in words.

## How to apply
- Ask for three variants at routes like `/proto-a`, `/proto-b`, `/proto-c`.
- Make them genuinely different in approach (layout, density, interaction model), not minor color/spacing variations.
- Click through, pick the winner, screenshot if useful.
- Feed the chosen variant into a `/grill-with-docs` session for the real implementation. Discard the other two.

## Caveats
- For greenfield UIs without an existing codebase, more iterations may be valuable; the pattern is specifically for mature codebases where a polished one-shot is unlikely to fit existing conventions.

## Related
- [grilling-alignment](grilling-alignment.md) — what happens after you pick
