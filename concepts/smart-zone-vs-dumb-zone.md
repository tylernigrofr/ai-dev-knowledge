---
title: Smart zone vs dumb zone
type: mental-model
phase: [planning, implementation, review]
tags: [context-management, attention, token-budget]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/anthropic-context-engineering.md
  - sources/articles/anthropic-multi-agent-research-system.md
  - sources/articles/anthropic-claude-code-best-practices.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:clean-context-reviewer
  - concept:compacting-vs-clearing
  - concept:handoff-docs
  - concept:subagents-as-delegation
  - playbook:afk-night-shift
audience: [planner, implementer]
activate_when: "Deciding when to clear context, split work, or delegate to a subagent."
cluster: context-management
---

## Summary
Every LLM session has a smart zone (~100k tokens, regardless of advertised context window) where attention is clean, then degrades into a dumb zone making sloppy decisions.

## Why it matters
Advertised 1M-token windows do not buy you 10× more useful context — they buy you more dumb zone. Tasks that overflow the smart zone produce noticeably worse output: missed constraints, hallucinated APIs, contradictions with earlier decisions. Sizing tasks to fit the smart zone is the cheapest quality lever you have.

Three architectural reasons the cliff exists (per Anthropic's engineering blog): (1) transformer attention creates n² pairwise relationships for n tokens — attention thins as n grows; (2) models train mostly on shorter sequences, giving them less "experience" with long-range context dependencies; (3) position-encoding interpolation degrades token-position understanding at extreme lengths. These are structural, not fixable by prompt alone.

## How to apply
- Treat ~80–100k tokens as the practical working ceiling per session.
- Set up a token-count status line in your harness so you can see live usage. (See Pocock's article on aihero.dev.)
- When usage approaches the ceiling, clear context and resume from a handoff doc rather than continuing.
- Decompose tasks so each subtask fits comfortably under the ceiling.
- For long-horizon agents spanning hundreds of turns, the in-context approach breaks down entirely. Use external memory storage and strategic retrieval — pull only the relevant prior context back in before approaching limits, rather than keeping everything in one window.

## Caveats
- The 100k figure is a working heuristic, not a measurement. Different model versions and task shapes shift the cliff.
- For pure summarization or retrieval tasks, larger contexts degrade more gracefully than for reasoning-heavy tasks.

## Related
- [compacting-vs-clearing](compacting-vs-clearing.md) — what to do when you hit the ceiling
- [clean-context-reviewer](clean-context-reviewer.md) — applying the smart-zone principle to review
- [push-vs-pull-context](push-vs-pull-context.md) — managing what fills the smart zone
