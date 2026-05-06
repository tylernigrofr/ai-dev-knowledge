---
title: Integration testing bias for AI work
type: principle
phase: [implementation, qa]
tags: [testing, integration-tests, grey-box, test-boundaries]
sources: [sources/articles/pocock-aihero-articles.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Test at the *outer* boundary of grey-box modules, not at unit-level inside them — when the AI controls the implementation, integration tests against the deep-module interface are the contract that lets you stop caring about internals.

## Why it matters
Unit tests written by the AI tempt the AI to test the implementation it just wrote, which proves nothing. They also fragment the test suite: 200 tightly-coupled small tests slow iteration without catching the bugs that actually matter (those happen at integration seams). When deep modules are in place, the *interface* is the test surface — testing through it exercises the real bug surface, locks down behaviour the AI can't quietly change, and lets you delegate the inside without anxiety. Pocock's example: rewriting a CLI tool's manual-QA flow into an end-to-end suite (with a temporary-Git-env utility) so the AI could run the full suite on every change.

## How to apply
- Identify the grey-box modules (see [deep-modules](deep-modules.md)). Test through their interfaces.
- Prefer end-to-end / integration tests that exercise the real bug pattern. If the AI can't tell which call site triggered the bug, the test is at the wrong level.
- Build the harnesses that make integration tests feasible: temporary databases, scratch filesystems, ephemeral Git environments, fixture replay. Treat the harness as part of the codebase.
- Run the full integration suite on every AI change. Anything less than that and the agent is operating with stale signal.
- Unit tests are fine for genuinely pure leaf functions; don't fight the AI when it writes them — but don't lean on them as the quality gate.

## Caveats
- Slow integration tests cap iteration speed (see [feedback-loop-ceiling](feedback-loop-ceiling.md)). Invest in speed: parallel runs, scoped subsets, deterministic setup.
- Some bugs are easier to localise with a unit test once integration has caught them. Integration is the gate; unit is a debugging tool.

## Related
- [deep-modules](deep-modules.md) — the structural prerequisite (grey boxes have testable interfaces)
- [tdd-for-afk](tdd-for-afk.md) — red-green discipline applied at the right boundary
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — why test speed matters
- [diagnose-loop](diagnose-loop.md) — where missing seams become explicit findings
