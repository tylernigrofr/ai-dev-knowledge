---
title: TDD is non-negotiable for AFK work
type: principle
phase: [implementation]
tags: [tdd, red-green-refactor, afk, test-cheating, horizontal-slicing]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Any task delegated to an unattended agent must follow strict red-green-refactor (write failing test → make it pass → refactor) — agents that write the implementation first will rewrite or weaken the tests to make them pass.

## Why it matters
LLMs love post-hoc tests because they're trained on examples where tests confirm code that already works. Left alone, an agent will: write the implementation, write a test, see the test fail for an unrelated reason, "fix" the test by loosening assertions, and report success. The bug is shipped and the test is now load-bearing for the wrong invariant. TDD's *only* enforcement mechanism here is ordering: the test must exist and fail before any implementation token is written.

**Anti-pattern: horizontal slicing.** The other failure mode is treating RED as "write all the tests" and GREEN as "write all the code." This produces *crap tests* — written in bulk against *imagined* behavior, asserting on data shapes and signatures rather than user-facing outcomes, and insensitive to real changes. The agent outruns its headlights, committing to test structure before it knows what the implementation needs. Vertical slicing — one test → one implementation → repeat — keeps each test responsive to what the previous cycle taught.

## How to apply
- Use a `red-green-refactor` skill that gates each phase explicitly. The agent cannot enter green until the test demonstrably fails for the right reason.
- One test at a time. Only enough code to pass *this* test. Don't anticipate future tests.
- Forbid editing the test once it's written, except in an explicit refactor step.
- **Never refactor while RED.** Get to GREEN first.
- Require the agent to print the failing test output before starting implementation.
- After GREEN, scan for refactor candidates: duplication → extract; long methods → private helpers (keep tests on the public interface); shallow modules → deepen; feature envy → move logic to where data lives; primitive obsession → value objects.
- Pair with a clean-context reviewer that checks: did the test exist in commit N before the implementation in commit N+1?
- Bake this into the Ralph loop prompt — every AFK issue runs through it.

## Caveats
- Pure refactors (no behavior change) are exempt; existing tests cover them.
- Exploratory prototypes (see `three-route-prototype`) skip TDD by design — they're throwaway.

## Related
- [ralph-loop](ralph-loop.md) — where TDD is enforced for AFK runs
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — why fast/clean tests determine quality
- [clean-context-reviewer](clean-context-reviewer.md) — the gate that catches test-cheating
