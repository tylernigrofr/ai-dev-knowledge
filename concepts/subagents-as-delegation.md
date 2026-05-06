---
title: Subagents are delegation, not subroutines
type: technique
phase: [planning, implementation, review]
tags: [subagents, context-isolation, exploration]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
A subagent burns its own tokens in an isolated context and returns only a summary, so use them aggressively for exploration, research, and any work whose intermediate output would otherwise pollute the parent's context.

## Why it matters
Every token in the parent's context shrinks the smart zone. If you grep, read 12 files, and skim a transcript directly in the parent, you've spent that budget on raw material the parent doesn't need to retain — only conclusions. A subagent does the same work in its own context, returns the conclusion, and the parent stays clean. This is the single biggest lever for keeping a long session in the smart zone.

## How to apply
- Default to subagents for: open-ended search, "where does X live in the codebase," reading long docs, multi-file exploration, independent verification of a hypothesis.
- Brief the subagent like a colleague who just walked in: goal, what's been ruled out, what shape the answer should take.
- Ask for short reports. "Under 200 words" beats "tell me everything."
- Run independent subagents in parallel — single message with multiple tool calls.
- Don't subagent for tasks where the parent must see the intermediate state (e.g., interactive debugging).

## Caveats
- Subagents can't see the parent's conversation. Self-contained briefs are mandatory.
- Their summaries describe intent, not necessarily reality — verify their concrete claims (file paths, function names) before acting.

## Related
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — what subagents protect
- [compacting-vs-clearing](compacting-vs-clearing.md) — subagents as a clearing strategy
- [clean-context-reviewer](clean-context-reviewer.md) — the reviewer is itself a kind of subagent
