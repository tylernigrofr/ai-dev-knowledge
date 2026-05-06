---
title: "Vibe-Coding to Vibe-Engineering — Matt Pocock @ AI Engineer 2025"
type: youtube
url: https://youtu.be/QFHIoCo-Ko
author: Matt Pocock
published: 2025-10-01
captured: 2026-05-06
status: extracted
concepts_seeded:
  - smart-zone-vs-dumb-zone
  - compacting-vs-clearing
  - grilling-alignment
  - vertical-slices
  - ralph-loop
  - clean-context-reviewer
  - push-vs-pull-context
  - deep-modules
  - afk-vs-hitl
  - doc-rot
  - three-route-prototype
  - ubiquitous-language
---

# Vibe-Coding to Vibe-Engineering

Matt Pocock's workshop talk on practical AI-driven engineering workflows. Source for the founding concepts of this KB. The full transcript is archived locally; what's preserved here is the structured extraction — the load-bearing claims grouped by topic, with each claim attributable back to a concept.

## Source notes

- Original transcript captured into the brainstorming session that produced this KB's design (`docs/superpowers/specs/2026-05-06-ai-dev-knowledge-base-design.md`).
- This file is the canonical citation target for the seed concepts; refining the source content (e.g. adding a fuller transcript or a link to slides) does not require updating concepts unless a claim changes.

## Extracted insights

### Mental models

- **Smart zone vs dumb zone.** Every LLM session has a smart zone (~100k tokens working number) where attention relationships are clean, then degrades. 1M context windows just ship "more dumb zone." Size every task to fit. → `concepts/smart-zone-vs-dumb-zone.md`
- **LLMs are the guy from Memento.** Compacting feels productive but accumulates sediment. Clearing and restarting with a clean handoff almost always wins. → `concepts/compacting-vs-clearing.md`

### Planning phase

- **Specs-to-code regen loop doesn't work.** Code is the battleground; you need eyes on it. What you want is a *shared design concept* (Brooks, *The Design of Design*).
- **Grilling skill.** A tiny prompt that interviews you relentlessly, one question at a time, with a recommended answer for each. 40–100 questions per session. The conversation history is the alignment artifact. → `concepts/grilling-alignment.md`
- **Don't review your own PRD.** You aligned during grilling. Reading the summary tests nothing. LLMs are good at summarization.
- **PRDs need an out-of-scope section** to capture negative decisions (the definition of done).

### Decomposition

- **Kanban over multi-phase plans.** Phase plans serialize work; kanban with a DAG enables parallelism. → (concept covered indirectly via `vertical-slices` + ralph-loop)
- **Vertical slices / tracer bullets, not horizontal layers.** AI loves DB → API → frontend; you get zero feedback until phase 3. Vertical slices give a working flow on day one. → `concepts/vertical-slices.md`
- **AFK vs human-in-the-loop tagging.** Tag each issue. AFK = delegate-able overnight; HITL = needs your judgment. → `concepts/afk-vs-hitl.md`

### Implementation

- **Ralph loop.** A simple bash loop: read open issues, last N commits, run agent with accept-edits, prompt picks next AFK task, uses TDD, runs feedback loops, commits, summarizes. → `concepts/ralph-loop.md`
- **TDD is non-negotiable for AFK work.** A red-green-refactor skill prevents the AI from cheating tests.
- **Feedback-loop quality is the ceiling on AI output.** Bad type errors, slow tests, flaky assertions all directly cap quality.

### Review

- **Reviewer must be in a clean context.** Self-review happens in the dumb zone. Always clear and start a fresh reviewer. Sonnet for implementation, Opus for review. → `concepts/clean-context-reviewer.md`

### Coding standards

- **Push vs pull.** Push = always-on (CLAUDE.md, system prompt). Pull = fetched on demand (skills with description headers). Push for reviewer, pull for implementer. → `concepts/push-vs-pull-context.md`

### Codebase shape

- **Deep modules > shallow modules** (Ousterhout). Small interface, lots inside. Lets you draw clean test boundaries; shallow modules force mocking hell. → `concepts/deep-modules.md`
- **Design module interfaces yourself; delegate the implementation.** Keeps your mental map intact while letting the AI move fast inside the gray boxes.

### Front-end

- **AI is multimodal-blind on visual judgment.** Don't one-shot polished UI. Three throwaway routes you click between → pick → grill → real implementation. → `concepts/three-route-prototype.md`

### Misc

- **Doc rot is real.** Closed PRDs in the repo get found by future agents and used as authoritative after the code has diverged. Pocock closes GitHub issues rather than keeping markdown PRDs in the repo. → `concepts/doc-rot.md`
- **Don't over-optimize the PRD.** The juice is in QA, not PRD perfection.
- **Don't outsource your planning stack.** Owning skills/prompts/loops means observability when things break.
- **Ubiquitous language doc** (`CONTEXT.md`, à la Eric Evans / DDD). Defines the project's jargon. Updated by `/grill-with-docs`. → `concepts/ubiquitous-language.md`
- **Subagents are delegation.** Burn their own tokens in isolated context, return summaries. Use aggressively for exploration.
- **Buy old software-engineering books.** Pre-AI writing on modularity, tracer bullets, refactoring, pragmatic programming maps almost perfectly onto AI workflows.
