---
title: Idea to agent-ready tickets (grill → spec → tickets)
phase: [planning, decomposition]
tags: [grilling, spec, tickets, github-issues, domain-model]
concepts_used:
  - grilling-alignment
  - ubiquitous-language
  - adr-discipline
  - prd-discipline
  - vertical-slices
  - kanban-over-phases
  - three-route-prototype
  - phase-boundary-decisions
tools: [claude-code, gh, mattpocock-skills]
status: stable
superseded_by: null
last_reviewed: 2026-09-24
---

Turn an idea into agent-ready GitHub tickets in one unbroken context: `/grill-with-docs` for alignment and domain docs, `/to-spec`, then `/to-tickets` with native blocking edges.

## Prerequisites
- The repo is set up with `/setup-matt-pocock-skills`, and `CONTEXT.md` + `docs/adr/` exist or will be created lazily.
- The idea fits in one session's worth of design. If it doesn't, start with `/wayfinder` (below).

## Setup
- Start a fresh session in the repo. Keep this whole playbook in **one unbroken context**: the spec and tickets should be built from the grilling verbatim, not from a summary.

## Loop
1. **`/grill-with-docs`**. Answer rounds of questions over the design tree.
   - Let it dispatch subagents for facts. Your job is decisions.
   - Accept `CONTEXT.md` edits inline as terms sharpen.
   - Accept an ADR only when the decision is hard to reverse, surprising, *and* a real trade-off.
2. **Detour if a question needs a runnable answer.** Use `/prototype`: a UI variants route, or a single-HTML logic walkthrough.
   - Bridge it with `/handoff` out and back if it lives in another directory.
   - Keep the prototype on a `prototype/<name>` branch and link it from the ticket.
3. **`/to-spec`**. Publish the spec as a GitHub issue, with an out-of-scope section. Don't re-read it for polish.
4. **`/to-tickets`**. Produce tracer-bullet tickets, each sized for one fresh context. Review the breakdown before publishing:
   - Is the granularity right?
   - Are the blocking edges genuine?
   - Does any wide refactor use expand–contract?

   Then publish them blockers-first, with native blocking links and `ready-for-agent`.
5. **Hand over to implementation.** A small build runs as `/implement` in place. Anything bigger goes to [orchestrated-issue-waves](orchestrated-issue-waves.md), usually after a `/clear`, since the tickets now carry the context.

## Verification
- Every ticket reads as behavior with acceptance criteria. None contains file paths or code, except decision-rich prototype snippets.
- The frontier is non-empty, and there are no cycles in the blocking edges.
- New domain terms from the session are in `CONTEXT.md`.

## Failure modes
- **Foggy scope.** Grilling keeps branching and never converges. Stop and use `/wayfinder`: it produces a map of decision tickets resolved one at a time, then merges back here at `/to-spec`.
- **Horizontal tickets** ("DB layer", "API layer"). Re-slice vertically, with prefactoring tickets first.
- **Triaging your own tickets.** `/triage` is for issues you *didn't* write.
- **Context blown before `/to-tickets`.** `/compact` at the nearest boundary with an instruction to keep the decisions, rather than pushing on degraded.
