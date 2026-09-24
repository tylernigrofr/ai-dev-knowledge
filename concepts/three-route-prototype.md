---
title: Throwaway prototype (logic vs UI bifurcation)
type: technique
phase: [planning, implementation]
tags: [frontend, prototyping, multimodal-blindness, state-machine, logic]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
referenced_by:
  - concept:llm-not-a-trustworthy-abstraction
  - concept:strategic-programming
  - playbook:idea-to-tickets
audience: [planner, implementer]
activate_when: "Need to answer a state-machine or UI design question before committing."
cluster: decomposition
---

## Summary
A prototype is throwaway code that answers a question, and the question decides the shape — for "what should this look like?" build several radically different UI variants on a single switchable route; for "does this logic / state model feel right?" build a single shareable HTML file that pushes the state machine through hard-to-reason-about cases.

## Why it matters
AI is multimodal-blind on visual judgment, so for UI work it can't tell you which option feels right — but humans pick from three concrete variants dramatically faster than they describe what they want in words. For logic and state-model questions, paper reasoning is unreliable and tests too rigid; an interactive walkthrough lets you push edge cases by hand and see the resulting state. The two prototype shapes answer different questions; getting the branch wrong wastes the prototype.

## How to apply

**Pick the branch first.** Identify the question being answered:

- "Does this logic / state model feel right?" → **logic prototype** (single HTML file).
- "What should this look like?" → **UI prototype** (multi-variant route).

If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch matches the surrounding code (backend module → logic; page/component → UI) and state the assumption at the top of the prototype.

**UI branch.**
- Three variants on routes like `/proto-a`, `/proto-b`, `/proto-c`, switchable via URL search param + a floating bottom bar.
- Genuinely different approaches (layout, density, interaction model), not minor color/spacing variations.
- Click through, pick a winner, feed it into `/grill-with-docs` for the real implementation. Discard the others.

**Logic branch.**
- A single HTML file the user double-clicks: free-play buttons plus tabbed guided walkthroughs, drivable by a non-developer. (Earlier versions used a terminal app.)
- State in memory only — no persistence (persistence is the thing the prototype is *checking*, not depending on).
- After every action, print the full relevant state so changes are visible.
- Push the state machine through cases that are hard to reason about on paper.

**Rules that apply to both branches.**
1. Throwaway from day one and *clearly marked as such*. Locate close to where it'll be used so context is obvious.
2. Trivial to run: one task-runner command for UI, double-click for the logic HTML file.
3. No tests, no error handling beyond runnable, no abstractions. Skip polish.
4. The *answer* folds into the real code (ADR, ticket, or a decision-rich snippet inlined in the ticket).
5. "Throwaway" constrains how it's written, not whether it survives: keep it on a `prototype/<name>` branch off main as a primary source and link it from the implementation issue. Never merge it.

## Caveats
- For greenfield UIs without existing conventions, more iterations may be valuable.
- Logic prototypes can degenerate into a "second implementation" — keep them ruthlessly minimal.

## Related
- [grilling-alignment](grilling-alignment.md) — what happens after you pick
- [doc-rot](doc-rot.md) — why prototypes live on a branch, not in main
- [adr-discipline](adr-discipline.md) — where the prototype's answer might land
