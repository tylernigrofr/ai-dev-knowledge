---
name: review-gates
description: Independent checks between "agent says done" and "merged" — clean-context review, evals, diagnosis discipline.
type: cluster
members:
  - clean-context-reviewer
  - llm-as-judge-evals
  - diagnose-loop
  - feedback-loop-ceiling
  - integration-testing-bias
  - mock-at-boundaries
last_reviewed: 2026-05-07
---

## Seam

The shared concern: an agent in its own dirty context cannot reliably review its own work. These concepts describe the **gates** — fresh-context reviewers, LLM-as-judge evals on small sets, disciplined diagnosis when something fails, and the test design (integration-biased, mocking only at true boundaries) that gives review something honest to bite on.

## Members

- **clean-context-reviewer** — a second agent in a clean context reviews the diff; the original is too anchored.
- **llm-as-judge-evals** — small judge sets to iterate on agent systems where unit tests can't reach.
- **diagnose-loop** — six-phase reproduce → minimise → hypothesise → instrument → fix → regress.
- **feedback-loop-ceiling** — output quality is bounded by signal quality; invest in the loop before the prompt.
- **integration-testing-bias** — favor grey-box integration tests over unit-mocking pyramids for AI work.
- **mock-at-boundaries** — only mock SDK-style boundaries; in-process code stays real.
