---
title: LLM-as-judge with small sample sets for iterating agent systems
type: technique
phase: [qa, review]
tags: [evals, testing, llm-as-judge, multi-agent]
sources:
  - sources/articles/anthropic-multi-agent-research-system.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:error-compounding-in-agents
audience: [reviewer, implementer]
activate_when: "Evaluating an agentic system or comparing prompt/system variants."
cluster: review-gates
---

## Summary
Start evaluation with ~20 representative queries scored by an LLM against a rubric; early iterations yield dramatic measurable improvements and small test sets are effective precisely because the improvement signal is large.

## Why it matters
Traditional software testing assumes deterministic outputs and benefits from large sample sizes. Agentic systems are non-deterministic, expensive per run, and improve in large jumps early in development. A 20-query eval set catches the most consequential failures fast, lets you iterate quickly, and avoids burning compute on premature statistical precision. As the system matures, you expand the set — but starting small is the right move, not a shortcut.

The LLM-as-judge approach enables evaluation at scale without the bottleneck of human scoring. A consistent rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) with 0.0–1.0 scoring per dimension yields scores comparable in consistency to human raters for most dimensions.

## How to apply
- Curate ~20 queries that represent the full range of real usage patterns: simple lookups, complex multi-step research, edge cases you've already hit.
- Write a rubric covering the dimensions that matter for your system. Each dimension should be scoreable on 0.0–1.0 with a clear description of what each end of the scale means.
- Use a single LLM call per evaluation (not multi-turn, not committee) — it is most consistent.
- Run human evaluation in parallel on a subset, especially for: hallucinated answers, subtle biases (e.g., agents preferring SEO-optimized content over authoritative sources), and system-level failures that look like partial successes.
- Track scores over iterations. A jump from 30% to 80% success rate in early iterations is normal — this is the useful signal window.
- As the system stabilizes, expand the eval set to improve statistical confidence. Don't expand prematurely.

## Caveats
- LLM judges have systematic biases: they favor verbose answers, familiar styles, and outputs that look similar to training data. Human spot-checks are not optional.
- A 20-query set cannot catch tail failures. Production monitoring (tracing, anomaly detection) is the complement, not a replacement.
- Rubric quality dominates outcome quality. A vague rubric produces uninformative scores — invest time in it before running.

## Related
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — evals are the feedback loop for agent systems
- [tdd-for-afk](tdd-for-afk.md) — adjacent discipline for implementation-level feedback
- [error-compounding-in-agents](error-compounding-in-agents.md) — what good evals need to catch
