---
title: ACI (agent-computer interface) tool design
type: technique
phase: [implementation]
tags: [tools, aci, poka-yoke, documentation, agent-interface]
sources:
  - sources/articles/anthropic-building-effective-agents.md
  - sources/articles/anthropic-multi-agent-research-system.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Design every tool the agent calls with the same care a product team applies to human-facing UI — clear descriptions, poka-yoke argument shapes, and iterated workbench testing — because tool interfaces are the agent's primary reality and bad ones silently degrade reasoning.

## Why it matters
Agents don't interact with the world directly; they interact through tools. A poorly designed tool forces the model to hold extra mental overhead (remembering state, counting lines, inferring conventions) that consumes context it should be using for reasoning. Anthropic's team building the SWE-bench agent "spent more time optimizing tools than the overall prompt" — the tool interfaces were the leverage point. Every mistake the model makes with a tool is a latent failure waiting to compound.

## How to apply

**Format and schema:**
- Keep data formats close to naturally-occurring internet text — the model has seen billions of tokens in that distribution.
- Eliminate formatting overhead: don't require the model to count lines, keep running tallies, or escape special characters unnecessarily.
- Give the model enough tokens to "think before it writes itself into a corner" — avoid formats that force premature commitment.

**Documentation:**
- Write tool descriptions as if teaching a junior engineer who can't ask follow-up questions.
- Include: example usage, edge cases, exact input format requirements, and clear boundaries from other tools.
- If two tools could be confused, explicitly contrast them in each description.

**Poka-yoke argument design:**
- Restructure arguments so that the most common mistakes become structurally impossible.
- Canonical example: requiring absolute file paths instead of relative ones eliminated a class of path-resolution errors when the agent changed directories.
- "Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it?"

**Iteration:**
- Run many example inputs in a workbench before deploying; observe where the model errs.
- Iterate on the tool definition — argument names, types, descriptions — before iterating on the prompt.
- **Let agents self-improve descriptions.** Give an agent its own tool definitions plus a set of failed traces, and ask it to suggest rewrites. Anthropic measured a 40% reduction in task-completion time after a tool-testing agent rewrote its own descriptions — the descriptions, not the model, were the bottleneck. Human-review before redeploying.

**Distinguishing overlapping tools:**
- If two tools have adjacent purposes, contrast them in *both* descriptions: "Use X when Y; use Z when W."
- Include explicit negative examples: "Do not use this tool for [adjacent case] — use [other tool] instead."
- Scale delegation to task complexity: simple fact-finding may need 1 agent with 3–10 tool calls; complex multi-step research benefits from 10+ specialized subagents with cleanly partitioned tools.

## Caveats
- Applies to tools you control. Third-party APIs need a thin adapter layer to apply these principles.
- Over-constraining arguments (e.g. too-strict enum validation) can break on legitimate edge cases. Test the failure mode, not just the happy path.
- Self-improving descriptions can rationalize a bad description as good if the eval set is narrow. Validate against held-out tasks, not the same traces used to suggest the rewrite.
- Tool descriptions become stale as underlying capabilities change. Treat them like code, not prose.

## Related
- [workflow-before-agents](workflow-before-agents.md) — tool quality matters at every level of the complexity ladder
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — bad tool responses are a feedback-loop failure
- [mock-at-boundaries](mock-at-boundaries.md) — SDK-style granular interfaces apply the same philosophy to internal seams
- [agent-safe-tooling](agent-safe-tooling.md) — complementary concern: runtime behavior of tools agents invoke
- [subagents-as-delegation](subagents-as-delegation.md) — tools are the interface subagents use
- [agent-brief-format](agent-brief-format.md) — same description discipline applied to agent briefs
