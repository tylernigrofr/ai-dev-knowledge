---
title: Disciplined diagnosis loop (six phases)
type: workflow
phase: [implementation, qa]
tags: [debugging, feedback-loops, hypothesis-testing, regression-tests]
sources: [sources/repos/pocock-skills.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:deep-modules
  - concept:error-compounding-in-agents
  - concept:integration-testing-bias
audience: [implementer]
activate_when: "Stuck on a hard bug or performance regression."
cluster: review-gates
---

## Summary
Hard bugs and performance regressions follow a six-phase loop — build feedback loop → reproduce → ranked hypotheses → instrument → fix + regression test → cleanup + post-mortem — and Phase 1 (the feedback loop) is the entire skill; everything after it is mechanical.

## Why it matters
Most debugging effort is wasted because the engineer (or agent) starts hypothesizing before they have a fast deterministic signal. Without a loop, hypothesis-testing devolves into staring at code; with a sharp loop, bisection and instrumentation drain the bug almost automatically. Pocock's discipline makes "build the loop" the gate before any other phase, which forces investment where the leverage actually lives.

## How to apply
**Phase 1 — build the feedback loop.** Try in roughly this order: failing test → curl/HTTP script → CLI invocation with fixture → headless browser → replay captured trace → throwaway harness → property/fuzz loop → bisection harness → differential loop → HITL bash script (last resort). Iterate on the loop itself: faster, sharper signal, more deterministic. A 2-second deterministic loop is a debugging superpower; a 30-second flaky loop is barely better than none. For non-deterministic bugs, raise the *reproduction rate* (loop 100×, parallelise, stress) until debuggable. If you genuinely cannot build a loop, stop and say so — list what you tried, request access / artifact / instrumentation. Don't proceed without one.

**Phase 2 — reproduce.** Confirm the loop fires on the *user's* failure mode (not a nearby one), reproduces across runs, and captures the exact symptom.

**Phase 3 — hypothesise.** Generate **3–5 ranked falsifiable hypotheses** before testing any. Each must state a prediction ("if X is the cause, changing Y makes it disappear"). Show the ranked list to the user — they often re-rank instantly.

**Phase 4 — instrument.** Each probe maps to one Phase-3 prediction. Change one variable at a time. Prefer debugger/REPL over logs. Tag every log with a unique prefix like `[DEBUG-a4f2]` so cleanup is one grep. For perf regressions, measure before fixing.

**Phase 5 — fix + regression test.** Write the regression test before the fix, *if* there's a correct seam. If not, that absence is itself the architectural finding — flag it for `/improve-codebase-architecture`.

**Phase 6 — cleanup + post-mortem.** Re-run Phase 1 against the original (un-minimised) scenario. Strip all `[DEBUG-...]` logs. State the correct hypothesis in the commit/PR message. Ask "what would have prevented this?" — if structural, hand off to architecture skill *after* the fix.

## Caveats
- For trivial bugs, the full loop is overkill. Skip phases only when explicitly justified.
- Phase 5 regression tests at a wrong seam give false confidence — better to document the gap than ship a misleading test.

## Related
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — why Phase 1 dominates
- [tdd-for-afk](tdd-for-afk.md) — adjacent red-green discipline
- [deep-modules](deep-modules.md) — the architectural surface diagnose-loop hands off to
