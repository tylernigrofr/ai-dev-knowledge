---
title: Generate over depend (prefer generated code over fast-moving dependencies)
type: principle
phase: [planning, implementation]
tags: [dependencies, stability, codegen, agent-context]
sources:
  - sources/articles/ronacher-agentic-coding-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by: []
audience: [implementer]
activate_when: "Considering adding a fast-moving or poorly-documented dependency."
cluster: tooling-aci
---

## Summary
When a dependency is fast-moving or poorly documented, generating the equivalent code yourself can produce better agent outcomes than adding the dependency — you and the agent both understand exactly what the code does, and stale breadcrumbs from the old API version can't mislead future runs.

## Why it matters
Every dependency the agent uses has to be in the model's training data or in context. Fast-moving libraries cause agents to generate calls against an older API version — then leave "tried X, switched to Y" comments that become stale the next library update. Generated code has no version to drift. The agent wrote it (or you did in collaboration); it's precisely what exists in the codebase. This is the inverse of the usual "don't reinvent the wheel" heuristic — it applies when the wheel changes shape every quarter.

## How to apply
- Before adding a dependency, ask: Is this library stable over 1-2 year horizons? If yes (Go stdlib, Flask, SQLite), add it. If no (fast-changing UI libraries, AI SDK du jour, young infrastructure tooling), evaluate generating instead.
- When generating: keep the generated code in a clearly named file with a comment explaining its provenance (`// generated alternative to <library> because <reason>`).
- Prefer plain SQL over ORMs for agent-generated queries — agents can read their own SQL in logs and match it to the code directly.
- Apply the same logic to glue code: a 50-line integration file that does exactly one thing beats a dependency that does 500 things and changes its API twice a year.

## Caveats
- **This is not "avoid all dependencies."** Stable, well-documented libraries (standard libraries, mature frameworks) are better than generated equivalents — the point is *churn*, not dependency count.
- **Security footguns.** Generated crypto, auth, or parsing code is almost always worse than a mature library. Never generate security-critical components.
- **Maintenance burden shifts to you.** Generated code grows stale differently — not through API drift, but through functional drift (new requirements the library would handle automatically). Be honest about total cost of ownership.
- Contested by mainstream practice: most engineers default to "use a library." This principle applies at the margin (high-churn / poorly-documented / AI-unfriendly libraries), not as a general rule.

## Related
- [doc-rot](doc-rot.md) — stale dependency docs are a special case of doc rot
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — agent confusion from outdated API breadcrumbs is a feedback degradation
- [pre-ai-fundamentals](pre-ai-fundamentals.md) — "avoid magic" has always been a principle; AI makes the cost of magic higher
