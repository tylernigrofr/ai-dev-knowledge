---
title: Compacting vs clearing context
type: anti-pattern
phase: [implementation, review]
tags: [context-management, handoff, memento]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/articles/anthropic-claude-code-best-practices.md
  - sources/articles/anthropic-context-engineering.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Compacting accumulated context feels productive but leaves sediment that degrades reasoning; clearing and resuming from a clean handoff almost always wins.

## Why it matters
LLMs are the guy from Memento — they cannot tell the difference between high-signal and low-signal context, so summarization-in-place keeps the noise. A clean reset with a deliberate handoff doc preserves what matters and discards what doesn't. Workflow artifacts (PRDs, issue files, skills, handoffs) must be designed to survive resets, because resets are the goal, not the failure mode.

## How to apply
- When usage approaches the smart-zone ceiling, write a handoff doc capturing: open question, current state, decisions made, what to do next.
- Clear the session and seed a fresh one with the handoff.
- Resist the urge to "just keep going" — the next session in a clean context is faster and produces better work.
- **After two failed corrections in a row, stop.** Don't keep correcting. `/clear` and write a better initial prompt that incorporates what you learned from the failed attempts. A clean session with a better prompt almost always outperforms a long session with accumulated corrections. (Anthropic's own guidance.)
- **Between unrelated tasks, always `/clear`** — mixing contexts from separate workstreams produces "kitchen-sink sessions" where irrelevant information degrades performance on both tasks.

## Caveats
- For very short tasks, a reset is overhead. The rule is for longer arcs.
- Some harnesses' built-in compaction is fine for transient state but should not replace deliberate handoff for substantive work.
- Claude Code's `/compact <instructions>` offers a middle path: summarize with explicit guidance on what to preserve (e.g., `/compact Focus on the API changes`). Still inferior to a clean reset for substantive work.
- When compaction is unavoidable (long conversational tasks without clear milestones), use the two-pass protocol from Anthropic: first maximize recall (capture every relevant architectural decision, unresolved bug, and implementation detail), then iterate to improve precision (remove redundant tool outputs and transient scaffolding). Tool call results are the primary safe-removal candidates.
- **Structured note-taking** is an alternative for very long-horizon tasks: agent writes persistent notes outside the context window, pulled back in at later steps. Provides persistent memory with minimal overhead. Complements rather than replaces the clear-and-handoff default.

## Related
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — why the cliff exists
- [clean-context-reviewer](clean-context-reviewer.md) — clearing for review specifically
