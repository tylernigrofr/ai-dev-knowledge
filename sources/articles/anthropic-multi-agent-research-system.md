---
title: "How Anthropic Built Their Multi-Agent Research System"
type: article
url: https://www.anthropic.com/engineering/built-multi-agent-research-system
author: Anthropic Engineering
published: 2025-01-01
captured: 2026-05-06
status: extracted
concepts_seeded:
  - subagents-as-delegation
  - smart-zone-vs-dumb-zone
  - aci-tool-design
  - llm-as-judge-evals
  - error-compounding-in-agents
---

# How Anthropic Built Their Multi-Agent Research System

Engineering post from Anthropic on building a production multi-agent research system, covering architecture, evaluation, prompt engineering, and operational challenges.

## Load-bearing claims

### Orchestrator-worker pattern and performance
- Lead agent (Claude Opus 4) analyzes requests, develops strategy, and spawns multiple subagents (Claude Sonnet 4) simultaneously to explore different aspects in parallel.
- Multi-agent system outperformed single-agent Opus 4 by 90.2% on internal evaluations for breadth-first queries requiring parallel exploration.
- Token usage explains 80% of performance variance on the BrowseComp evaluation — distributing across separate context windows enables "more capacity for parallel reasoning."
- Running 3–5 subagents simultaneously plus 3+ parallel tool calls per agent "cut research time by up to 90% for complex queries."

### Token economics: multi-agent is expensive
- Agents consume approximately 4× more tokens than chat interactions.
- Multi-agent systems consume roughly 15× more tokens than chat — requiring demonstrably high-value tasks for economic viability.
- The performance gain is real, but the cost multiplier is not marginal — budget accordingly.

### Tool design is critical and improvable
- "Using the right tool is efficient — often, it's strictly necessary." Bad tool descriptions derail agents entirely.
- Clear, distinct tool purposes prevent tool confusion; overlapping or vague descriptions compound into repeated wrong calls.
- Claude models effectively diagnose prompt failures and suggest improvements. Tool-testing agents rewrote their own tool descriptions, achieving a "40% decrease in task completion time."

### Evaluation strategy: small samples + LLM-as-judge
- Start with ~20 queries representing real usage patterns. Early iterations show dramatic improvements (30% to 80% success rates), making small test sets effective.
- LLM-as-judge rubrics covering factual accuracy, citation accuracy, completeness, source quality, and tool efficiency — single LLM calls with 0.0–1.0 scoring proved most consistent.
- Human evaluation is still required: it reveals hallucinated answers, system failures, and subtle biases automation misses (e.g., agents choosing SEO-optimized content over academic sources).

### Error compounding: the defining property of stateful agents
- "The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely."
- Agents maintain state across extended periods; failures cascade unpredictably.
- Mitigations: resumable checkpoints, graceful error handling, allowing agents to adapt when tools fail.

### Long-horizon context management
- Agents spanning hundreds of turns require intelligent summarization, external memory storage, and strategic context retrieval before approaching context limits.
- Direct specialized agent outputs to external systems via lightweight references — prevents information loss and reduces token overhead in multi-stage processing.

### Debugging and deployment ops
- Non-deterministic behavior between identical runs requires "full production tracing" to diagnose failures systematically.
- Monitor "agent decision patterns and interaction structures" without accessing conversation contents for privacy-preserving diagnosis.
- Stateful agent networks require "rainbow deployments" (gradual traffic shift between old/new versions) to prevent disrupting running agents.

### Search strategy (research-specific)
- Begin with broad queries, evaluate available information, then progressively narrow focus — mirrors expert human research patterns.
- Extended thinking with interleaved reasoning helps subagents evaluate results and identify gaps mid-task.
