---
title: Orchestrated issue waves (one orchestrator session, parallel worktree workers)
phase: [decomposition, implementation, review, qa]
tags: [orchestration, parallelization, github-issues, worktrees, subagents]
concepts_used:
  - orchestrator-worker-dispatch
  - kanban-over-phases
  - agent-sandbox-isolation
  - clean-context-reviewer
  - rules-to-checks
  - phase-boundary-decisions
  - triage-state-machine
  - tdd-for-afk
tools: [claude-code, gh, mattpocock-skills]
status: stable
superseded_by: null
last_reviewed: 2026-09-24
---

Drain a GitHub issue graph from one supervised orchestrator session. Dispatch the frontier to background worktree subagents in waves, merge each branch one at a time through a scripted gate, and review the combined diff at the end of each wave.

## Prerequisites
- The repo is configured once with `/setup-matt-pocock-skills`: GitHub as the tracker, triage labels, and domain docs at `CONTEXT.md` + `docs/adr/`.
- Work exists as GitHub issues with **blocking edges**, from `/to-tickets` (see [idea-to-tickets](idea-to-tickets.md)) or from `/triage` for incoming reports.
- `CLAUDE.md` is an entry pointer. It links to `docs/agents/orchestration.md`, `worktrees.md` and `testing.md`, so briefs can *point* at rules instead of restating them.
- A **merge-guard script** exists (rebase → lint → required tests → merge, refusing on any failure), and so does a fast test layer the orchestrator can run per branch.

## Setup (per batch)
1. Pick or create a parent/batch issue. Put a **wave table** in its body with these columns: issue, worker, worktree/branch, base SHA, dependencies, status, validation, landed SHA.
2. Compute the **frontier**: open issues whose blockers are all closed. For each one, read the issue *and its comments*, check `git log` and the code for already-landed work, and check siblings for overlap (same files, same migration numbers, same schema).
3. Size the wave to real concurrency: 3–5 workers is a sane default, and fewer if they touch neighbouring modules.

## Loop
1. **Dispatch.** One background subagent per frontier issue, with `isolation: worktree`. Each gets a compact brief of *pointers*, not history:
   - the issue number and its acceptance criteria;
   - the allowed scope;
   - the base SHA;
   - the worktree path;
   - relevant `CONTEXT.md` terms and ADRs;
   - the testing rule for this repo (by name);
   - stop conditions;
   - the exact report shape: SHA, files, behavior change, tests written and what each pins, risks.
2. **Worker first moves.** Verify the worktree (toplevel, branch, and that the base contains its dependencies), copy in gitignored files, then implement. Use `/tdd` at agreed seams, or write-only tests if that's the repo's ruling. Commit only its own work.
3. **Integrate as reports land,** one branch at a time:
   - skim the diff against the acceptance criteria and ADRs;
   - run the merge guard with targeted tests;
   - on conflict, `/resolving-merge-conflicts` (resolve by intent);
   - revalidate, then close the issue with the landed SHA;
   - update the wave table.
4. **Refill.** If a merge unblocked new tickets, dispatch them into the running wave. Don't wait for the whole wave.
5. **End of wave:**
   - run the full suite;
   - run `/code-review` (Standards + Spec) over the combined diff since the wave's base;
   - file actionable findings as new issues, deduplicated, with blockers marked;
   - clean up merged worktrees.
6. **Orchestrator hygiene at the boundary.** Record state in the parent issue, then apply [phase-boundary-decisions](../concepts/phase-boundary-decisions.md). A fresh orchestrator can resume from the issue thread alone.

## Verification
- Every closed issue names a landed commit and the validation that ran.
- The wave table matches `git log` and `gh issue list`: no "done" without a SHA.
- The full suite is green on `main` after the wave. Nothing was skipped because a fixture or env file was missing.
- The orchestrator's context stayed in the smart zone. If worker reports flooded it, tighten the report shape or move the fan-out into a scripted workflow.

## Failure modes
- **Worker edited `main`.** Its worktree was GC'd and it didn't verify. Fix: make `pwd`/toplevel verification the first line of every brief, and reject reports without a branch SHA.
- **Green but wrong.** It built on a stale base, or tests were skipped. Fix: land dependencies before cutting worktrees, and make missing fixtures fail loudly.
- **Merge conflicts pile up.** The wave was too wide on coupled code. Fix: add blocking edges or shrink the wave, and coordinate shared schema centrally.
- **Rework loops.** The brief was underspecified. After two failed attempts, stop and re-grill the ticket rather than re-dispatching.
- **Same mistake twice.** Turn it into a check (see [rules-to-checks](../concepts/rules-to-checks.md)), not another CLAUDE.md line.
- **Already built.** The issue was stale. Always check comments and `git log` before dispatching.
