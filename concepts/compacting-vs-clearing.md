---
title: Compacting vs clearing context
type: anti-pattern
phase: [implementation, review]
tags: [context-management, handoff, memento]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
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

## Caveats
- For very short tasks, a reset is overhead. The rule is for longer arcs.
- Some harnesses' built-in compaction is fine for transient state but should not replace deliberate handoff for substantive work.

## Related
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — why the cliff exists
- [clean-context-reviewer](clean-context-reviewer.md) — clearing for review specifically
