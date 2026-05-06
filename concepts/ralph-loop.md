---
title: Ralph loop (AFK implementation)
type: workflow
phase: [implementation]
tags: [automation, agents, tdd]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
A simple bash loop that picks the next unblocked AFK-tagged issue, runs an agent with accept-edits permissions and a TDD-enforced prompt, commits, and repeats — turning issue queue into night-shift output.

## Why it matters
Once issues are vertically sliced and AFK-tagged, implementation becomes a delegation problem. The Ralph loop is the simplest pattern that delegates safely: bounded agent invocations, TDD as a quality gate, fresh-context reviewer between, no infinite-running daemons. It is also the substrate that more sophisticated parallel patterns (Pocock's sandcastle) wrap.

## How to apply
- Read all open AFK-tagged issues into a variable; grab the last N commits as context.
- Invoke the agent with `--permission-mode accept-edits`, a prompt that says: pick next unblocked AFK task → use TDD (red-green-refactor skill) → run feedback loops → commit → output a summary.
- After commit, fire a reviewer in a clean context (Opus recommended) that pushes coding standards and pulls only diffs/issue.
- On review pass: merge. On fail: kick to fix loop with max retries before flagging human-in-loop.
- Keep the implementer in Sonnet (or equivalent) and the reviewer in Opus for the cost-quality split.

## Caveats
- Cost scales with parallelism. Set per-issue and per-day budgets.
- Feedback-loop quality is the ceiling — slow tests, flaky assertions, or weak type errors directly cap output quality.

## Related
- [vertical-slices](vertical-slices.md) — what feeds the loop
- [clean-context-reviewer](clean-context-reviewer.md) — the review half
- [push-vs-pull-context](push-vs-pull-context.md) — context discipline within the loop
