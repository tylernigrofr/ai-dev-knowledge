---
title: Ralph loop (AFK implementation)
type: workflow
phase: [implementation]
tags: [automation, agents, tdd]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/huntley-ralph-wiggum-software-engineer.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:afk-vs-hitl
  - concept:agent-loop-simplicity
  - concept:agent-safe-tooling
  - concept:agent-sandbox-isolation
  - concept:clean-context-reviewer
  - concept:feedback-loop-ceiling
  - concept:kanban-over-phases
  - concept:own-your-planning-stack
  - concept:push-vs-pull-context
  - concept:sand-castle-parallelization
  - concept:tdd-for-afk
  - concept:vertical-slices
  - playbook:afk-night-shift
audience: [planner, implementer]
activate_when: "Setting up an unattended single-agent implementation loop."
cluster: afk-loops
---

## Summary
A bash loop that picks one unblocked AFK-tagged issue, runs an agent with accept-edits permissions and a TDD-enforced prompt, commits, and repeats — turning an issue queue into night-shift output. Coined by Geoffrey Huntley; the canonical minimal form is `while :; do cat PROMPT.md | claude-code; done`.

## Why it matters
Once issues are vertically sliced and AFK-tagged, implementation becomes a delegation problem. The Ralph loop is the simplest pattern that delegates safely: bounded agent invocations, TDD as a quality gate, fresh-context reviewer between, no infinite-running daemons. It is also the substrate that more sophisticated parallel patterns (Pocock's sandcastle) wrap.

## How to apply

### Minimal loop (Huntley's original)
```bash
while :; do cat PROMPT.md | claude-code; done
```
`PROMPT.md` carries specifications, context, and hard constraints. Update it when Ralph makes mistakes rather than switching tools ("tune Ralph like a guitar").

### One item per iteration — hard constraint
Each loop iteration must accomplish exactly one task. Multi-task iterations degrade context window efficiency and output quality. This is a design principle, not a guideline.

### Two-phase structure
- **Generate:** Steer via technical standard libraries and specifications in the prompt. Wrong patterns → update the standard library, not the model.
- **Backpressure:** Every iteration gates on tests, compilation, static analysis, and security scanning. Rust's type system provides automatic backpressure; dynamic languages need external checkers (Dialyzer, Pyre).

### Implementer-as-agent variant (Pocock extension)
- Read all open AFK-tagged issues into a variable; grab the last N commits as context.
- Invoke the agent with `--permission-mode accept-edits`, a prompt that says: pick next unblocked AFK task → use TDD (red-green-refactor skill) → run feedback loops → commit → output a summary.
- After commit, fire a reviewer in a clean context (Opus recommended) that pushes coding standards and pulls only diffs/issue.
- On review pass: merge. On fail: kick to fix loop with max retries before flagging human-in-loop.
- Keep the implementer in Sonnet (or equivalent) and the reviewer in Opus for the cost-quality split.

### Prompt guards
- Explicitly forbid placeholder implementations: instruct the agent that minimal/stub implementations are not acceptable and full implementations are required.
- Include a self-improvement directive: after each iteration, update `@AGENT.md` (or equivalent) with any new learnings so the next loop starts with better context.

## Caveats
- **Greenfield bias.** Ralph works best bootstrapping new projects from scratch. Modifying existing codebases is harder; scope carefully. (Huntley's explicit caveat.)
- Cost scales with parallelism. Set per-issue and per-day budgets.
- Feedback-loop quality is the ceiling — slow tests, flaky assertions, or weak type errors directly cap output quality.
- Senior engineering expertise remains essential for guiding the loop. Ralph is not fully autonomous.

## Related
- [vertical-slices](vertical-slices.md) — what feeds the loop
- [clean-context-reviewer](clean-context-reviewer.md) — the review half
- [push-vs-pull-context](push-vs-pull-context.md) — context discipline within the loop
- [tdd-for-afk](tdd-for-afk.md) — the TDD gate inside each iteration
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — why backpressure quality determines output quality
