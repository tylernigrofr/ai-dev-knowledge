---
title: AFK night-shift implementation loop
phase: [implementation]
tags: [parallelization, ralph-loop, sandcastle]
concepts_used:
  - ralph-loop
  - vertical-slices
  - afk-vs-hitl
  - clean-context-reviewer
  - push-vs-pull-context
  - smart-zone-vs-dumb-zone
tools: [sandcastle, opencode, claude-code]
status: draft
last_reviewed: 2026-05-06
---

## Prerequisites

- A backlog of issues that have been [vertically sliced](../concepts/vertical-slices.md) and tagged [AFK or HITL](../concepts/afk-vs-hitl.md).
- A `STANDARDS.md` (or equivalent) plus `CONTEXT.md` and any ADRs in a `docs/adr/` directory — these will be pushed to the reviewer.
- A working harness with sandboxed worktree support (e.g. Pocock's [sandcastle](https://github.com/mattpocock/sandcastle)) and per-task git worktrees.
- A red-green-refactor TDD skill installed (e.g. from `mattpocock/skills`).
- Per-issue and per-day cost budgets configured.

## Setup

1. Set up the sandcastle parallel-planner template (or equivalent harness):
   - Implementer prompt template at `.sandcastle/implement.md` referencing the TDD skill, accepting `{{ISSUE_NUMBER}}`, model = `claude-sonnet-4-6`, accept-edits permission.
   - Reviewer prompt template at `.sandcastle/review.md` that begins with `` !`cat CONTEXT.md` `` and `` !`cat docs/adr/*.md` `` and `` !`cat STANDARDS.md` ``, accepts `{{COMMIT_SHA}}`, model = `claude-opus-4-6`, read-only.
2. Wire up a logging hook so each agent invocation writes structured events to `.sandcastle/logs/` (consumed by the dashboard if present).
3. Confirm the issue tracker exposes "open AFK-tagged unblocked issues" via a single query (GitHub label query or local file scan).

## Loop

Per cycle (cron, manual, or watch-mode):

1. Query for unblocked `mode: afk` issues. If none, exit.
2. Pick the next N (default 3 for parallel; 1 for sequential).
3. For each issue, in its own git worktree + container:
   1. Run the implementer with `{{ISSUE_NUMBER}}` substituted. Use [TDD](../concepts/ralph-loop.md) — write failing test first.
   2. On commit, fire the reviewer in a [clean context](../concepts/clean-context-reviewer.md) against the diff.
   3. On review pass: merge into main; mark issue done.
   4. On review fail: kick to fix loop; max 2 retries before flagging human-in-loop.
4. Concurrently, run a QA-scout subagent that produces new issues against merged work — these land back on the kanban.
5. Repeat.

## Verification

- Successful cycle: open issue closed, commit on main, review report archived.
- Cost check: per-cycle cost within budget; if not, downgrade reviewer to Sonnet for low-risk slices.
- Drift check: `CONTEXT.md` and ADRs unchanged unless an issue explicitly touched them; flag silent drift.

## Failure modes

- **Implementer cheats the test.** Cause: TDD skill not pulled or weak. Fix: enforce skill via push, not pull, until trust is built.
- **Reviewer rubber-stamps.** Cause: standards too vague or push budget exhausted. Fix: tighten standards; trim non-load-bearing push content.
- **Cost runaway.** Cause: parallel Opus reviewers on big diffs. Fix: per-issue caps + downgrade reviewer to Sonnet on low-risk slices.
- **Merge conflicts pile up.** Cause: too many parallel implementers on related code. Fix: dependency-aware scheduling; the planner respects `blocked_by`.
- **Doc rot.** Cause: PRDs left in repo after issues close. Fix: see [doc-rot](../concepts/doc-rot.md).
