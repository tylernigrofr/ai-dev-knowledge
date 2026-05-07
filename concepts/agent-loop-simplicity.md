---
title: Agent loop simplicity (the 9-line core)
type: mental-model
phase: [implementation]
tags: [agents, architecture, tool-use, automation]
sources:
  - sources/articles/zeyliger-agent-loop.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by: []
audience: [implementer]
activate_when: "Building or evaluating an agent harness from scratch."
cluster: agent-skill-design
---

## Summary
The entire architecture of a capable LLM agent is a ~9-line loop: call the model, print output, handle tool calls, feed results back — with a single bash tool covering a surprisingly wide range of real tasks.

## Why it matters
The simplicity is load-bearing, not cosmetic. Practitioners over-engineer agent infrastructure before proving the loop works, adding orchestration layers, custom parsers, and workflow engines on top of a core that could be a `while True` in a weekend script. Zeyliger's surprise ("shockingly simple") captures the mismatch between perceived complexity and actual implementation: the loop is not the hard part. The hard parts are tool quality, prompt discipline, and feedback signal — all of which sit *outside* the loop. Understanding the loop's simplicity prevents misplaced architectural investment.

## How to apply
- Start with a single bash tool. Prove the loop works end-to-end before adding specialized tools.
- Specialize tools only when you have evidence the general tool is failing: wrong edits, lost context, slow iteration.
- When debugging an agent, audit the loop first — is the tool result being fed back correctly? Is the conversation history accumulating right? Most loop bugs are plumbing, not model quality.
- Use the 9-line mental model to evaluate agentic frameworks: if a framework makes the loop *more* complex to understand, that's a cost that needs justification.

## Caveats
- The simplicity applies to the *core loop*, not to production concerns: auth, cost budgets, rate limits, safety rails, parallelism, and context compaction all add real complexity.
- "Bash is enough" is a 2025-era claim with Claude 3.7 Sonnet-class models. As tasks grow more complex (file-system isolation, multi-repo, long context), specialized tools earn their keep faster.
- Single-threaded interactive loops differ meaningfully from multi-agent parallel loops (see ralph-loop, sand-castle-parallelization). The simplicity claim does not extend to orchestration of multiple agents.

## Related
- [ralph-loop](ralph-loop.md) — a concrete production pattern built on this loop
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — what actually limits what the loop can produce
- [sand-castle-parallelization](sand-castle-parallelization.md) — when you need more than one loop
