---
title: Workflow-before-agents complexity ladder
type: principle
phase: [planning, decomposition]
tags: [agents, workflows, simplicity, orchestration, complexity]
sources:
  - sources/articles/anthropic-building-effective-agents.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:aci-tool-design
audience: [planner, implementer]
activate_when: "Tempted to build an autonomous agent before trying simpler patterns."
cluster: agent-skill-design
---

## Summary
Reach for autonomous agents only after simpler workflow patterns fail — each step up the complexity ladder (single prompt → chaining → routing → parallelization → orchestrator-workers → evaluator-optimizer → full agent) must earn its added latency and error-compounding risk.

## Why it matters
Autonomous agents are seductive but costly: they trade latency and cost for flexibility, and their errors compound — a wrong decision at step 3 can corrupt every step downstream. Most real tasks can be solved by a well-chosen workflow pattern that keeps LLM calls predictable and auditable. Anthropic's SWE-bench work validates the pattern: they spent more time on tool design than on agent architecture, because the scaffolding mattered more than the autonomy.

## How to apply

**The ladder — stop at the lowest rung that solves the problem:**

1. **Single prompt** — optimize with comprehensive evaluation before adding steps.
2. **Prompt chaining** — fixed sequential steps with intermediate gates; use when a task decomposes cleanly into ordered subtasks.
3. **Routing** — classify input, dispatch to specialized prompt/model; use when distinct input categories benefit from different handling or model sizes.
4. **Parallelization** — *sectioning* (independent subtasks in parallel) or *voting* (N runs for consensus/diversity); use when subtasks are independent or when diverse outputs reduce variance.
5. **Orchestrator-workers** — central LLM dynamically decomposes and delegates; use when subtasks aren't pre-definable (e.g. complex multi-file changes).
6. **Evaluator-optimizer** — generator + separate evaluator in a loop; use only when clear evaluation criteria exist and iterative refinement demonstrably improves output.
7. **Full agent** — LLM drives its own tool use and planning loop; use only when "open-ended problems where it's difficult or impossible to predict the required number of steps."

**Decision heuristic:** "You should consider adding complexity *only* when it demonstrably improves outcomes." Benchmark each step up against the simpler baseline.

## Caveats
- The right level depends on task predictability, not task difficulty. A hard but well-defined task (e.g. code translation with known grammar) may stay at rung 2; a medium task with an unknown step count may need rung 7.
- Workflows are not inferior — they're often faster, cheaper, and more auditable than agents for production systems.

## Related
- [vertical-slices](vertical-slices.md) — within any rung, build end-to-end slices before expanding breadth
- [aci-tool-design](aci-tool-design.md) — the tool design that makes every rung more reliable
- [own-your-planning-stack](own-your-planning-stack.md) — own the orchestration code regardless of rung
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — each rung's quality is still capped by signal quality
