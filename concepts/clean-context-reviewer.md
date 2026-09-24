---
title: Clean-context reviewer
type: principle
phase: [review]
tags: [review, context-isolation, quality-gate]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/anthropic-claude-code-best-practices.md
  - sources/repos/pocock-skills.md
  - sources/repos/owner-practice-2026.md
  - sources/articles/claude-code-orchestration-docs-2026.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
referenced_by:
  - concept:compacting-vs-clearing
  - concept:llm-not-a-trustworthy-abstraction
  - concept:orchestrator-worker-dispatch
  - concept:push-vs-pull-context
  - concept:ralph-loop
  - concept:sand-castle-parallelization
  - concept:smart-zone-vs-dumb-zone
  - concept:subagents-as-delegation
  - concept:tdd-for-afk
  - playbook:afk-night-shift
  - playbook:orchestrated-issue-waves
audience: [reviewer, planner]
activate_when: "Setting up review for agent-produced changes."
cluster: review-gates
---

## Summary
Every implementation must be reviewed by a fresh agent in a clean context that has not seen the implementation work — self-review happens in the dumb zone and catches almost nothing.

## Why it matters
An implementer that has been in-session has built justifications for its choices that survive into self-review. A clean reviewer has no such bias and judges the diff against the spec and standards alone. This is the most cost-effective single quality gate for AI-generated code.

## How to apply
- After each implementation commit, spawn a separate subprocess / session with no prior context.
- Feed the reviewer: the diff, the linked issue, push-style coding standards (`CONTEXT.md`, `ADR`s, `STANDARDS.md`).
- Use at least as strong a model for review as for implementation. (Pocock's 2025 split was Opus to review, Sonnet to implement. By late 2026 the owner runs one strong model for every role, because it proved efficient enough.)
- Output is structured pass/fail + findings. Gate merging on review pass.

### Anthropic's Writer/Reviewer pattern

Anthropic officially recommends the same principle via parallel sessions: Session A implements, Session B reviews with `@file` reference and no prior context. "A fresh context improves code review since Claude won't be biased toward code it just wrote." Can also split test-writing from implementation: have one session write tests, another write code to pass them.

### Subagents as lightweight reviewers

Use `"use a subagent to review this code for edge cases"` to get a clean-context review inline without fully switching sessions. Subagents run in a separate context window and report findings as a summary, preserving main session context.

### Two axes, and findings that must be actionable
- Pocock's `/code-review` (2026) splits review into two parallel subagents: **Standards** (does the diff follow the repo's documented standards, plus a Fowler smell baseline?) and **Spec** (does it do what the originating issue asked?). Neither pollutes the other's context.
- Claude Code's built-in `/code-review` runs as a background subagent with effort levels (`low`…`max`, `ultra` for a multi-agent cloud review). Managed review adds a verification pass that filters false positives.
- The owner's practice: each finding must name **a reachable failure, the code location, the consequence, and a way to verify it**. No speculative style churn. **An AI review alone is not a correctness gate**; tests and static checks are the evidence. After a wave of merges, review the *combined* diff across module boundaries, not just each branch.

## Caveats
- The reviewer's effectiveness is bounded by the standards it pushes. Vague standards → vague reviews.
- For trivial changes (typos, doc edits) the review overhead may exceed the value. Make the gate skippable, but default to on.

## Related
- [push-vs-pull-context](push-vs-pull-context.md) — what to push to the reviewer
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — why fresh context matters
- [ralph-loop](ralph-loop.md) — where this fits in the AFK loop
