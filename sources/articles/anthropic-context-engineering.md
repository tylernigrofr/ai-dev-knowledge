---
title: "Effective Context Engineering for AI Agents — Anthropic Engineering Blog"
type: article
url: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
author: Anthropic
published: 2025-01-01
captured: 2026-05-06
status: extracted
concepts_seeded:
  - smart-zone-vs-dumb-zone
  - compacting-vs-clearing
  - push-vs-pull-context
  - subagents-as-delegation
  - just-in-time-docs
---

# Effective Context Engineering for AI Agents

Anthropic engineering post defining "context engineering" as the successor to prompt engineering, with guidance on every layer of the context stack.

## Load-bearing claims

### Context engineering ≠ prompt engineering
Prompt engineering is discrete and task-focused. Context engineering is iterative — the curation phase runs every inference turn. It covers "all the other information that may land there outside of the prompts": tool outputs, retrieved data, memory, conversation history, and examples.

### Context rot is architectural, not just behavioral
As token count grows, model performance degrades for three structural reasons:
1. Transformer attention creates n² pairwise relationships — thins out as n grows.
2. Models are trained mostly on shorter sequences, giving them less "experience" with long-range context dependencies.
3. Position encoding interpolation degrades token-position understanding at length.

Result: context has **diminishing marginal returns**. Advertised window size ≠ usable window size.

### System prompts — the "right altitude" principle
Two failure modes: (a) hardcoding complex logic ("brittle, high maintenance") and (b) high-level vague guidance ("fails to give concrete signals, falsely assumes shared context"). Optimal: specific enough to guide behavior, flexible enough to provide strong heuristics. Start minimal on the best available model, then iterate from failure modes, not from anticipated edge cases.

### Tool bloat is a decision-ambiguity problem
Bloated tool sets that cover too much functionality or create overlapping decision points degrade agent performance. Rule: "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better." Tools should be well-understood, self-contained, minimal in number, and have descriptive, unambiguous parameter names.

### Just-in-time context over pre-loading
Agents should maintain lightweight identifiers (file paths, stored queries, web links) and load data at runtime via tools rather than stuffing context upfront. Claude Code example: writes targeted DB queries + bash commands instead of loading full datasets. Mirrors human cognition — we don't memorize corpuses, we index and retrieve.

### Compaction: maximize recall first, then precision
Compaction is not a simple summarize-and-continue operation. Protocol: first maximize recall (ensure every relevant piece is captured), then iterate to improve precision (eliminate redundant tool outputs, transient scaffolding). Tool call results are typical candidates for safe removal after serving their immediate purpose.

### Structured note-taking as persistent memory
For long-horizon tasks, agents should write notes to persistent storage outside the context window, pulled back in at later steps. Provides "persistent memory with minimal overhead." Example: Claude playing Pokémon maintained precise tallies across thousands of game steps, surviving context resets by reading its own notes.

### Sub-agent architectures as context isolation
Each sub-agent handles a focused task with a clean context window. Main agent coordinates at high-level plan layer. Sub-agents may use tens of thousands of tokens exploring, but return a condensed 1,000–2,000 token summary. This is "clear separation of concerns" — the sub-agent's exploration cost is paid locally, not globally.

### Choosing the right long-horizon technique
- **Compaction**: best for tasks requiring extensive back-and-forth conversational flow.
- **Note-taking**: best for iterative development with clear milestones.
- **Multi-agent**: best for research/analysis where parallel exploration pays dividends.

### Core maxim
"Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome." Even as models improve, treating context as a precious finite resource remains central.
