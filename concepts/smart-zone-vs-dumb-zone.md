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
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24

---

## Summary
Every LLM session has a smart zone (~150k tokens on current frontier models, regardless of advertised context window) where attention is clean, then degrades into a dumb zone making sloppy decisions.

## Why it matters
Advertised 1M-token windows do not buy you 10× more useful context — they buy you more dumb zone. Tasks that overflow the smart zone produce noticeably worse output: missed constraints, hallucinated APIs, contradictions with earlier decisions. Sizing tasks to fit the smart zone is the cheapest quality lever you have.

Three architectural reasons the cliff exists (per Anthropic's engineering blog): (1) transformer attention creates n² pairwise relationships for n tokens — attention thins as n grows; (2) models train mostly on shorter sequences, giving them less "experience" with long-range context dependencies; (3) position-encoding interpolation degrades token-position understanding at extreme lengths. These are structural, not fixable by prompt alone.

## How to apply
- Treat ~150k tokens as the practical working ceiling per session on current frontier models (Pocock revised this up from ~100k in 2026 as models improved).
- Set up a token-count status line in your harness so you can see live usage. (See Pocock's article on aihero.dev.)
- When usage approaches the ceiling, decide at the next phase boundary. Don't compact mid-phase (see [phase-boundary-decisions](phase-boundary-decisions.md)).
- Decompose tasks so each subtask fits comfortably under the ceiling.
- For long-horizon agents spanning hundreds of turns, the in-context approach breaks down entirely. Use external memory storage and strategic retrieval — pull only the relevant prior context back in before approaching limits, rather than keeping everything in one window.

## Caveats
- The 150k figure is a working heuristic, not a measurement. Different model versions and task shapes shift the cliff.
- For pure summarization or retrieval tasks, larger contexts degrade more gracefully than for reasoning-heavy tasks.

## Related
- [phase-boundary-decisions](phase-boundary-decisions.md): what to do when you hit the ceiling
- [clean-context-reviewer](clean-context-reviewer.md) — applying the smart-zone principle to review
- [push-vs-pull-context](push-vs-pull-context.md) — managing what fills the smart zone
