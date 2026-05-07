---
title: Handoff documents for context resets
type: technique
phase: [planning, implementation]
tags: [context-management, handoff, session-boundaries]
sources: [sources/repos/pocock-skills.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by: []
audience: [planner, implementer]
activate_when: "Ending a session or about to clear context."
cluster: context-management
---

## Summary
Before clearing context or ending a session, write a short handoff document that summarises *only the conversation state* — not artifacts already captured elsewhere — so the next fresh agent can continue without re-deriving anything.

## Why it matters
Clearing context is the right move (see compacting-vs-clearing), but the next session starts at zero. Without a handoff, the new agent re-discovers what the previous one already learned, burning tokens on lookups and risking subtly different conclusions. A handoff doc preserves the *delta* between durable artifacts (PRDs, ADRs, issues, commits) and what's actually in the working memory of the current session — decisions that haven't been written down, hypotheses currently being tested, what was just ruled out.

## How to apply
- Pocock's `/handoff` skill: write to a path from `mktemp -t handoff-XXXXXX.md`.
- **Don't duplicate** PRDs, ADRs, issues, commit messages, diffs — reference them by path or URL.
- Capture: what you're trying to do, where you got to, what's been ruled out, what to try next, which skills the next session should use.
- Keep it short. If it's longer than a screen, you're duplicating something.
- Pass an argument describing what the next session will focus on so the doc tailors itself.

## Caveats
- Handoff only works if durable artifacts are already in good shape. If the PRD is stale, the handoff inherits the staleness.
- For trivial work, a clean clear without a handoff is fine.

## Related
- [compacting-vs-clearing](compacting-vs-clearing.md) — handoffs are how clearing stays cheap
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — handoffs let you keep every session in the smart zone
- [doc-rot](doc-rot.md) — handoffs are throwaway by design; resist promoting them to repo docs
