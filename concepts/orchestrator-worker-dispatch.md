---
title: Orchestrator–worker dispatch over an issue graph
type: workflow
phase: [decomposition, implementation, review]
tags: [parallelization, orchestration, worktrees, subagents, github-issues, kanban]
sources:
  - sources/repos/owner-practice-2026.md
  - sources/repos/pocock-skills.md
  - sources/articles/claude-code-orchestration-docs-2026.md
  - sources/articles/anthropic-multi-agent-research-system.md
  - sources/youtube/pocock-vibe-engineering-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
referenced_by:
  - concept:kanban-over-phases
  - concept:ralph-loop
  - concept:sand-castle-parallelization
  - concept:subagents-as-delegation
  - playbook:orchestrated-issue-waves
audience: [planner]
activate_when: "Several unblocked issues exist and one session will dispatch parallel workers to implement them."
cluster: afk-loops
---

## Summary
One long-lived orchestrator session owns the queue, integration and validation. It dispatches bounded worker subagents, each on one issue in its own verified worktree, in dependency-aware waves over the issue graph's frontier, and it merges their branches one at a time through a scripted gate.

## Why it matters
An issue graph with blocking edges exposes parallelism, and a single session can drain it without a separate harness. Claude Code now has native background subagents with `isolation: worktree`, plus scripted workflows. The failure modes are coordination failures rather than model failures: workers that silently edit `main`, build on a stale base, collide on shared schema, or flood the orchestrator's context with long reports. Splitting the roles cleanly prevents most of them. Workers produce commits and evidence. The orchestrator alone decides what lands.

## How to apply
**Orchestrator:**
- Its checkout stays on `main`, and it doesn't implement.
- Before dispatching, read each issue *and its comments*, check whether the work has already landed, and check sibling issues for overlap.
- Dispatch the **frontier** (issues whose blockers are all closed) in **waves** sized to real concurrency and CPU. 3–5 workers is the common default, and more only when the test infrastructure keeps up.
- Land dependencies on `main` before cutting the worktrees that need them. Coordinate migration numbers and shared schema centrally.
- Keep a compact **wave table** in the parent issue: issue, worker, worktree/branch, base SHA, dependencies, status, validation, landed SHA. Task state lives in GitHub, not in the orchestrator's memory.

**Worker brief** (a compact contract with *context pointers*, not session history):
- the issue number and its acceptance criteria;
- the allowed scope;
- the base SHA and dependencies;
- the absolute worktree path, and relevant `CONTEXT.md` terms and ADRs;
- required checks and stop conditions;
- the exact report shape: commit SHA, changed files, behavior change, validation run, risks and remaining work.

**Worker:** verify isolation first (see [agent-sandbox-isolation](agent-sandbox-isolation.md)). Commit only its own work, then report briefly.

**Integration:**
- Merge **one branch at a time** through a single merge-guard script: rebase → lint → targeted tests → merge. Don't use a hand-typed chain of commands.
- Re-check `main` for sibling changes, resolve conflicts by intent, and revalidate.
- Close the issue as part of the change that lands it, naming the commit.
- After a wave, the orchestrator runs the full suite and reviews the combined diff across module boundaries. Findings go back onto the board as issues.

**Variants:**
- *PR-per-spec*: Pocock's `implement-spec`. A draft PR closes the spec's tickets, a merger subagent merges each worker branch into the PR branch, and `/code-review` runs once at the end.
- *Scripted fan-out*: Claude Code dynamic workflows, when intermediate results would swamp the orchestrator's context.
- *Harness-driven*: e.g. Pocock's Sandcastle, with Docker-sandboxed implementers for fully AFK runs.

## Caveats
- **Test ownership has two styles.** One lets each worker run its own TDD loop. The other (the owner's current ruling) has workers *write* tests but never run them, and the orchestrator runs validation at integration. That saves wall-clock but means a worker's first green is the orchestrator's. Choose one explicitly and put it in every brief.
- Skip delegation for trivial work, since the brief costs more than the edit.
- Agent-team teammates don't get separate worktrees, so split their work by file.
- The orchestrator is the bottleneck. When integration queues up, shrink the wave rather than adding workers.

## Related
- [kanban-over-phases](kanban-over-phases.md): the graph being drained
- [clean-context-reviewer](clean-context-reviewer.md): the review gate
- [subagents-as-delegation](subagents-as-delegation.md): why workers get their own context
- [ralph-loop](ralph-loop.md): the single-threaded, unattended ancestor
- [sand-castle-parallelization](sand-castle-parallelization.md): the harness-specific version this generalizes
