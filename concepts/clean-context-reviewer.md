---
title: Clean-context reviewer
type: principle
phase: [review]
tags: [review, context-isolation, quality-gate]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/anthropic-claude-code-best-practices.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Every implementation must be reviewed by a fresh agent in a clean context that has not seen the implementation work — self-review happens in the dumb zone and catches almost nothing.

## Why it matters
An implementer that has been in-session has built justifications for its choices that survive into self-review. A clean reviewer has no such bias and judges the diff against the spec and standards alone. This is the most cost-effective single quality gate for AI-generated code.

## How to apply
- After each implementation commit, spawn a separate subprocess / session with no prior context.
- Feed the reviewer: the diff, the linked issue, push-style coding standards (`CONTEXT.md`, `ADR`s, `STANDARDS.md`).
- Use a smarter model for review than implementation — Pocock uses Opus for review and Sonnet for implementation.
- Output is structured pass/fail + findings. Gate merging on review pass.

### Anthropic's Writer/Reviewer pattern

Anthropic officially recommends the same principle via parallel sessions: Session A implements, Session B reviews with `@file` reference and no prior context. "A fresh context improves code review since Claude won't be biased toward code it just wrote." Can also split test-writing from implementation: have one session write tests, another write code to pass them.

### Subagents as lightweight reviewers

Use `"use a subagent to review this code for edge cases"` to get a clean-context review inline without fully switching sessions. Subagents run in a separate context window and report findings as a summary, preserving main session context.

## Caveats
- The reviewer's effectiveness is bounded by the standards it pushes. Vague standards → vague reviews.
- For trivial changes (typos, doc edits) the review overhead may exceed the value. Make the gate skippable, but default to on.

## Related
- [push-vs-pull-context](push-vs-pull-context.md) — what to push to the reviewer
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — why fresh context matters
- [ralph-loop](ralph-loop.md) — where this fits in the AFK loop
