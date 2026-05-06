---
title: "Building Effective Agents — Anthropic Engineering"
type: article
url: https://www.anthropic.com/engineering/building-effective-agents
author: Erik S. and Barry Zhang (Anthropic)
published: 2024-12-19
captured: 2026-05-06
status: extracted
concepts_seeded:
  - workflow-before-agents
  - aci-tool-design
  - own-your-planning-stack
  - feedback-loop-ceiling
---

# Building Effective Agents — extraction

Anthropic engineering post laying out a practical taxonomy of agentic system patterns, tool-design heuristics, and a "simplicity first" design philosophy.

## Load-bearing claims

### Simplicity ladder: workflows before agents
"Finding the simplest solution possible, and only increasing complexity when needed." Agentic systems "trade latency and cost for better task performance" — that trade must be earned. Start with a single well-engineered prompt; escalate to multi-step workflows; escalate to fully autonomous agents only when fixed paths cannot be hardcoded. Complexity must demonstrably improve outcomes.

### The five workflow patterns (before going agentic)
Before reaching for a full agent, consider these in roughly ascending complexity:
1. **Prompt chaining** — sequential LLM calls where each processes the prior output; intermediate gates verify quality.
2. **Routing** — classify input, direct to a specialized prompt/model; separates concerns, allows model-size optimization.
3. **Parallelization** — two variants: *sectioning* (independent subtasks in parallel) or *voting* (same task N times for diverse outputs).
4. **Orchestrator-workers** — central LLM dynamically decomposes and delegates to worker LLMs; subtasks aren't pre-defined, which distinguishes it from parallelization.
5. **Evaluator-optimizer** — one call generates, another evaluates and loops; valuable when "LLM responses can be demonstrably improved when a human articulates their feedback" and when clear evaluation criteria exist.

### Augmented LLM as the atomic unit
An "augmented LLM" — an LLM enhanced with retrieval, tools, and memory — is the building block. All patterns compose these. The emphasis is on tailoring the augmentations to the specific use case and providing a "well-documented interface for your LLM."

### ACI: treat tool interfaces with HCI-level care
"We spent more time optimizing tools than the overall prompt" (SWE-bench). Tools are the agent's world-interface — design them as carefully as a product team designs user-facing UI. Specific guidance: (a) pick formats that minimize model "thinking" overhead; (b) keep format close to naturally-occurring internet text; (c) avoid formatting overhead (e.g. line-counting); (d) include example usage, edge cases, input format requirements, and clear boundaries; (e) test extensively in workbench; (f) apply poka-yoke: restructure arguments so mistakes are structurally hard. Canonical example: required absolute file paths eliminated a whole class of relative-path errors.

### Environmental grounding at every step
"During execution, it's crucial for the agents to gain 'ground truth' from the environment at each step (such as tool call results or code execution) to assess its progress." Agents are not batch processors — each step's output changes what the next step should be.

### Avoid framework abstraction for orchestration
"Frameworks often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug." Recommendation: "start by using LLM APIs directly: many patterns can be implemented in a few lines of code." "Incorrect assumptions about what's under the hood are a common source of customer error."

### Human-in-the-loop checkpoints
Agents can and should "pause for human feedback at checkpoints or when encountering blockers." For coding agents specifically, "human review remains crucial for ensuring solutions align with broader system requirements" even when automated tests pass.
