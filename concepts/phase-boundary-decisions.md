---
title: Phase-boundary decisions (continue → clear → handoff → subagent → compact)
type: technique
phase: [planning, implementation, review]
tags: [context-management, handoff, compaction, session-boundaries]
sources:
  - sources/repos/pocock-skills.md
  - sources/articles/claude-code-orchestration-docs-2026.md
  - sources/youtube/pocock-vibe-engineering-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
---

## Summary
Decide what to do with a session's context only at a phase boundary, by walking an ordered test (continue, then `/clear`, then `/handoff`, then a subagent, then `/compact`) where the first "yes" wins. Mid-phase, either continue or split the rest into subagents.

## Why it matters
Every move except Continue turns a **primary source** (the session as it happened) into a lossy **secondary source** (a summary). Clearing a context that was still relevant loses the *why* behind decisions, and reading the diff back doesn't recover it. Compacting mid-phase makes the agent lose the thread, and Anthropic notes the model is "at its least intelligent point when compacting". The older rule of thumb, "always clear and hand off rather than compact", was too blunt. Many boundaries are best served by just continuing, and many by a plain `/clear` with no handoff at all.

## How to apply
At the boundary between two phases (grilling → implementation, implementation → QA), ask in order:

1. **Continue?** Yes if the next phase needs this one verbatim (grilling → spec → tickets is the standard case) or if there's enough smart zone left for it to fit (~150k tokens on current frontier models).
2. **`/clear`?** Yes if nothing here matters to what's next. It's the cheapest move, and the old session stays resumable.
3. **`/handoff`?** Only when something has to *travel*: a new harness (Claude → Codex), a new directory or repo, a colleague, or a side task forked mid-phase. See [handoff-docs](handoff-docs.md).
4. **Subagent?** Yes if the next task can run AFK with no steering. Automated review is the standard case.
5. **Otherwise `/compact <what the next phase needs>`.** It's the default, but only reached after ruling out the rest. Always pass an instruction.

Other rules:
- **After two failed corrections in a row, stop.** Prefer `/rewind` or `/clear` plus a better prompt over stacking corrections.
- **Between unrelated tasks, always `/clear`.** Kitchen-sink sessions degrade both tasks.
- For an **orchestrator** session, the orchestrator's context is the scarce resource. Keep workers' reports short and structured, and keep task state in issues so a fresh orchestrator can resume from GitHub instead of from memory.

## Caveats
- These are judgment calls. The same boundary can go two ways on two days, and the value is in asking the questions in order.
- The 150k figure is a heuristic that has drifted upward with each model generation (it was ~100k in early 2026).

## Related
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md): why the budget exists
- [handoff-docs](handoff-docs.md): option 3
- [subagents-as-delegation](subagents-as-delegation.md): option 4
- [compacting-vs-clearing](compacting-vs-clearing.md): the older, blunter rule this supersedes
