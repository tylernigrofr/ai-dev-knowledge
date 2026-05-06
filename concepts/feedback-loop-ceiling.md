---
title: Feedback-loop quality is the ceiling on AI output
type: principle
phase: [implementation]
tags: [feedback-loops, tests, type-errors, dx]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/pocock-aihero-articles.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
An AI agent's output quality is hard-capped by the quality of the signals it receives — slow tests, vague type errors, flaky assertions, and noisy linters all directly degrade what the agent can produce, regardless of model size.

## Why it matters
Agents iterate by reading feedback and adjusting. If the type error says "Type 'X' is not assignable to type 'Y'" with no context, the agent guesses. If tests take 90s, the agent runs fewer iterations. If a linter screams about unrelated lines, the agent "fixes" them and creates churn. Every gap in your feedback loop is a gap in the agent's reasoning. Investing in DX is now investing in agent quality — they're the same thing.

## How to apply
- Audit feedback loops before pointing agents at a codebase: test runtime, type-error clarity, lint signal-to-noise, error message specificity.
- Prefer fast (<5s) focused tests over slow (>30s) suite-wide ones. The agent will run them more often.
- Use libraries / tooling that produce specific, actionable error messages.
- Eliminate flakes ruthlessly. A flaky test trains the agent to retry rather than diagnose.
- Treat any "I don't understand this error" moment in your own work as an agent-quality bug.
- **Friction is desirable.** Pre-commit hooks, CI, and strong types are not obstacles — they're the signal density the agent needs. Every AI change should trigger them all. The more immediate the feedback, the better decisions the agent can make.

## Caveats
- Some feedback (production telemetry, user reports) can't be made instant. For these, build the smallest reproducer the agent can iterate on locally.
- Over-investing in DX before product-market-fit is still wrong. The ceiling matters once you're shipping fast.

## Related
- [tdd-for-afk](tdd-for-afk.md) — TDD only works if tests are fast and clear
- [deep-modules](deep-modules.md) — better module shape produces better test boundaries
- [ralph-loop](ralph-loop.md) — the loop that consumes feedback
