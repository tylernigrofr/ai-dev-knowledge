---
title: Error compounding — why minor faults derail stateful agents
type: mental-model
phase: [implementation, qa]
tags: [stateful-agents, debugging, error-handling, production]
sources:
  - sources/articles/anthropic-multi-agent-research-system.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
In stateful, multi-step agentic systems, errors compound rather than isolate — a minor issue that would be harmless in traditional software can cascade through downstream steps and derail the entire task.

## Why it matters
Traditional software components fail locally: a bad database call throws an exception, which is caught or surfaces immediately. A stateful agent accumulates intermediate results over many tool calls and reasoning steps. A subtly wrong conclusion in step 3 becomes an unchecked premise in step 7, which shapes the tool calls in step 12, which produces a plausible-looking but wrong final output. The gap between "something went wrong" and "the task is broken" is invisible and hard to pinpoint after the fact.

Anthropic's production system identified this as the defining operational property of agentic systems: "The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely."

## How to apply
- Build in resumable checkpoints at key decision points — if a step fails, the agent can restart from the last checkpoint rather than from scratch.
- Graceful degradation over hard failure: allow agents to adapt when a tool fails rather than halt. Define explicit fallback behaviors in tool descriptions.
- Prefer end-state evaluation over step validation: check that the agent achieved the intended final state, not that each intermediate step was structurally correct. This catches compounding errors that individually look valid.
- Instrument decision points, not just errors. Full production tracing of agent reasoning is necessary to diagnose cascading failures after the fact.
- For multi-step tasks, include mid-task verification: "Before proceeding to phase 2, confirm that X is true."

## Caveats
- Checkpoints add latency and token cost. Checkpoint granularity is a tradeoff against recovery cost.
- This is distinct from non-determinism: even a deterministic agent can exhibit error compounding if its intermediate states are unvalidated.

## Related
- [diagnose-loop](diagnose-loop.md) — structured approach for finding where the compound error originated
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — tight feedback loops prevent errors from accumulating silently
- [llm-as-judge-evals](llm-as-judge-evals.md) — end-state evaluation is the right eval shape for this failure mode
- [subagents-as-delegation](subagents-as-delegation.md) — subagents scope errors to their own context, limiting propagation
