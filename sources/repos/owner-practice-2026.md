---
title: "Owner's practice — orchestrated agent development on a production repo"
type: repo
url: null   # private repo; generalized lessons only
author: Tyler Nigro
published: 2026-09-24
captured: 2026-09-24
status: extracted
concepts_seeded:
  - orchestrator-worker-dispatch
  - agent-sandbox-isolation
  - rules-to-checks
  - clean-context-reviewer
  - push-vs-pull-context
  - adr-discipline
  - tdd-for-afk
---

# Owner's practice (as of 2026-09)

First-party source: the KB owner's full-time production project, a high-volume issue-driven repo. Every rule below is recorded in the repo as a dated **owner ruling** after something went wrong. Private repo: capture the transferable practice only.

## Layout of agent instructions
- `CLAUDE.md` is an **entry pointer**: one short paragraph per topic (orchestration, issue tracker, triage labels, testing, worktrees, spend, performance…), each ending "See `docs/agents/<topic>.md`". `AGENTS.md` points Codex at the same files, so Claude and Codex share one set of instructions.
- `docs/agents/*.md` hold the detail, pulled on demand. Durable behavioral preferences live there; **changing task state lives in GitHub issues**, "so Claude and Codex do not depend on private conversation memory."
- `CONTEXT.md` + `docs/adr/` single-context domain docs. ADR titles are the decision stated as a sentence, so the directory listing reads as a rule index.

## Orchestrator and workers (`docs/agents/orchestration.md`)
- Main session = orchestrator: clarify outcomes, choose bounded work, dispatch workers, review evidence, manage dependencies, integrate. Its checkout stays on `main`.
- GitHub Issues are the authoritative queue. Before dispatching: read the issue *and its comments*, check landed code and commits (is it already built?), and check sibling work for overlap. Closing the issue is part of the change that lands it.
- The orchestrator keeps a compact **wave table** in the batch/parent issue: issue, worker/model, scope, worktree/branch, base SHA, dependencies, status, validation, landed SHA.
- Run large queues in **dependency-aware waves** sized to real concurrency and CPU, "not a promised number of simultaneous agents". Land dependencies before starting their consumers; coordinate migration numbers and shared schema centrally.
- **Worker brief contract:** issue + acceptance criteria, allowed scope, dependencies + base SHA, absolute worktree path, relevant docs, model, required checks, stop conditions, requested report. **Report contract:** commit SHA, changed files, behavior change, exact validation + results, risks and remaining work. Workers commit only their own work; the orchestrator owns integration and push.
- Skip delegation for trivial work. Send a compact brief, not session history. Prefer a focused rescue over restarting; stop repeated unproductive attempts and reassess the brief.
- Model routing by difficulty (later simplified to one strong model for every worker once it proved efficient enough). The goal is conserving subscription **usage limits**, not dollars. Never switch to paid, metered API execution just to get around a subscription limit.

## Testing ownership (owner ruling 2026-09-17, carve-out 2026-09-21)
- **Workers write tests but never run them**; syntax checks only. They name each test they wrote and what it pins. The orchestrator runs targeted tests at integration (one branch at a time) and full sweeps after a substantial batch. Rationale: saves wall-clock, since the orchestrator will run them anyway.
- Carve-out: a worker whose deliverable *is* a measurement (profiling, reproducing a flake) may run tests.

## Integration
- Integrate one change at a time through a single **merge-guard script** (rebase onto `main` and refuse on conflict → lint → always-run test set + targeted tests → read verdict from exit codes/JUnit, not console text → refuse on dirty main → `--no-ff` merge → push only with a flag). "Never a hand-run `pytest && git merge && git push` chain."
- Revalidate affected behavior after conflict resolution. Never discard another session's work, force-push `main`, or remove active/dirty/unmerged worktrees.

## Worktree hazards — "silently green" (`docs/agents/worktrees.md`)
Three failures where the run looks clean but the work didn't happen or happened in the wrong place:
1. **Worktree GC'd.** Unchanged worktrees are auto-removed; a resumed agent's shell falls back to the shared checkout on `main` while the harness still says "isolated". Check `pwd` / `git rev-parse --show-toplevel` and the branch against the assignment; `cd` explicitly in every command.
2. **Stale base.** A worktree is cut from `main` at creation; a dependency landed later is missing and the tests that would catch it aren't wired. Verify with `git merge-base --is-ancestor <commit> HEAD`. Fix upstream: land dependencies before cutting dependent worktrees.
3. **Gitignored files absent** (local paths config, `.env`): the suite skips ~91 tests and reports success. Copy them in; make the suite fail loudly when they're missing.
4. Code run by path may import an *installed* copy of the package instead of the worktree's edits. Tell: a fix that demonstrably changed code produced no change in the measurement.

## Review and QC
- Review each implementation diff against acceptance criteria, domain invariants and ADRs before integration, using a separate bounded reviewer for substantive changes.
- Review findings must name **a reachable failure, code location, consequence, and useful verification**. No speculative style churn.
- "An AI review alone is not a correctness gate": tests and static checks are the evidence.
- At the end of a wave, inspect the combined diff across module boundaries; file deduplicated findings as issues, separating blockers from follow-ups.

## Architecture passes (`docs/architecture-pass-2026-08.md`)
- Six read-only explorer subagents walked the tree against a target-state doc, scoring each area on **current friction × future load**. Output: a ranked candidate list ("each candidate is a grilling conversation waiting to happen"), a mechanical housekeeping tier needing no grilling, live defects found in passing (filed as bugs immediately), ratified rulings, and **"what is already right — do not touch."**
- Start with one bounded subsystem; a review request alone does not authorize a broad rewrite. File proposals as issues.

## Rules become mechanisms
- Policies get pinned by tests or scripts rather than prose: a test pins the *absence* of a CI PR gate; the manual is pinned to the CLI by a test; a pre-commit hook refuses gitignored paths and secrets; the merge guard is "the only sanctioned way to merge".
- "Profile before optimising — no exceptions, including for whoever is most confident." Workers that refute the orchestrator's premise by measuring are doing expected work.
- Fixture snapshot drift: investigate every delta before regenerating; "+1 entry" treated as routine repeatedly hid regressions.
- ADR-0030: the harness owns **invariants** (what must be true of an answer); the model owns **procedures** (how to get there). Procedures are perishable; invariants are few and permanent.
- **Metered spend** (scope matters, see **Metered spend** in `CONTEXT.md`): the permission rule covers only **pay-per-token API calls billed in dollars**, e.g. OpenRouter or a direct provider API key used by the product's own pipelines. Never start a metered run costing more than a few dollars without permission; price it first and report the estimate as a range, not a point. The provider key's limit is the hard cap.
  - It does **not** cover work done on a flat-rate subscription: Claude Code, Codex, a Z AI coding plan, and so on. Dispatching subagents, running reviews, or doing long sessions on a subscription needs no spend permission and no pre-run estimate. The only concern there is conserving the plan's usage limits (capacity, not money), handled by sizing waves sensibly.
