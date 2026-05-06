# Index

_Last generated: 2026-05-06_

## Playbooks

- [AFK night-shift implementation loop](playbooks/afk-night-shift.md) — `draft`

## Concepts by type

### Mental models
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — Every LLM session has a smart zone (~100k tokens) where attention is clean, then degrades.
- [Pre-AI fundamentals map onto AI workflows](concepts/pre-ai-fundamentals.md) — Old SE books on modularity, tracer bullets, refactoring describe what agents need.

### Principles
- [Clean-context reviewer](concepts/clean-context-reviewer.md) — Every implementation must be reviewed by a fresh agent in a clean context.
- [Deep modules over shallow modules](concepts/deep-modules.md) — Small interfaces, rich internals; deletion test, seams, leverage, locality.
- [Push vs pull context](concepts/push-vs-pull-context.md) — Push for reviewers, pull for implementers.
- [Ubiquitous language (CONTEXT.md / DDD)](concepts/ubiquitous-language.md) — Every project keeps a glossary of its domain terms.
- [Vertical slices (tracer bullets) over horizontal layers](concepts/vertical-slices.md) — Decompose into thin end-to-end slices.
- [PRD discipline](concepts/prd-discipline.md) — Out-of-scope is the definition of done; don't self-review; don't over-polish.
- [Kanban (DAG) over multi-phase plans](concepts/kanban-over-phases.md) — Independently grabbable issues unlock parallelism.
- [TDD non-negotiable for AFK work](concepts/tdd-for-afk.md) — Red-green-refactor prevents test-cheating.
- [Feedback-loop quality is the ceiling](concepts/feedback-loop-ceiling.md) — Bad signals cap agent output regardless of model.
- [Own your planning stack](concepts/own-your-planning-stack.md) — Don't outsource skills/prompts/loops to opaque frameworks.
- [ADR discipline (offer sparingly)](concepts/adr-discipline.md) — Only when hard-to-reverse + surprising + real trade-off.
- [Integration testing bias for AI work](concepts/integration-testing-bias.md) — Test through grey-box interfaces, not unit-level inside.
- [Just-in-time AI-generated docs](concepts/just-in-time-docs.md) — Regenerate from code on demand; don't commit drift-prone markdown.

### Techniques
- [AFK vs human-in-the-loop tagging](concepts/afk-vs-hitl.md) — Tag every issue as delegate-able or judgment-needed.
- [Grilling for alignment](concepts/grilling-alignment.md) — Have the AI interview you to reach a shared design concept.
- [Throwaway prototype (logic vs UI)](concepts/three-route-prototype.md) — Bifurcate by question: terminal app for logic, multi-route variants for UI.
- [Design interfaces yourself, delegate implementation](concepts/design-interfaces-delegate-implementation.md) — Keep mental map intact; let AI fill gray boxes.
- [Subagents as delegation](concepts/subagents-as-delegation.md) — Isolated context, summary return; protects the smart zone.
- [Zoom out for unfamiliar code](concepts/zoom-out.md) — Force a breadth-first map of modules in domain-glossary vocabulary.
- [Handoff documents](concepts/handoff-docs.md) — Bridge fresh sessions across context resets without duplicating durable artifacts.

### Workflows
- [Ralph loop (AFK implementation)](concepts/ralph-loop.md) — Bash loop that picks the next AFK issue and runs an agent on it.
- [Sand Castle parallelization](concepts/sand-castle-parallelization.md) — Planner + sandboxed implementers + reviewers + merger over live kanban.
- [Disciplined diagnosis loop](concepts/diagnose-loop.md) — Six-phase debug discipline; Phase 1 (build the loop) is the skill.
- [Triage state machine](concepts/triage-state-machine.md) — Two category roles + five state roles; AFK queue only contains `ready-for-agent`.

### Anti-patterns
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md) — Compacting accumulates sediment; clearing wins.
- [Doc rot in the repo](concepts/doc-rot.md) — Stale PRDs in the repo become authoritative for future agents.

## Concepts by phase

### planning
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Grilling for alignment](concepts/grilling-alignment.md)
- [Deep modules](concepts/deep-modules.md)
- [Doc rot](concepts/doc-rot.md)
- [Throwaway prototype](concepts/three-route-prototype.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)
- [PRD discipline](concepts/prd-discipline.md)
- [Design interfaces, delegate implementation](concepts/design-interfaces-delegate-implementation.md)
- [Own your planning stack](concepts/own-your-planning-stack.md)
- [Subagents as delegation](concepts/subagents-as-delegation.md)
- [Pre-AI fundamentals](concepts/pre-ai-fundamentals.md)
- [Zoom out](concepts/zoom-out.md)
- [Handoff docs](concepts/handoff-docs.md)
- [ADR discipline](concepts/adr-discipline.md)

### decomposition
- [Vertical slices](concepts/vertical-slices.md)
- [AFK vs HITL](concepts/afk-vs-hitl.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)
- [PRD discipline](concepts/prd-discipline.md)
- [Kanban over phases](concepts/kanban-over-phases.md)
- [Triage state machine](concepts/triage-state-machine.md)
- [ADR discipline](concepts/adr-discipline.md)

### implementation
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing](concepts/compacting-vs-clearing.md)
- [Vertical slices](concepts/vertical-slices.md)
- [Ralph loop](concepts/ralph-loop.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)
- [Deep modules](concepts/deep-modules.md)
- [Doc rot](concepts/doc-rot.md)
- [Throwaway prototype](concepts/three-route-prototype.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)
- [TDD for AFK](concepts/tdd-for-afk.md)
- [Feedback-loop ceiling](concepts/feedback-loop-ceiling.md)
- [Design interfaces, delegate implementation](concepts/design-interfaces-delegate-implementation.md)
- [Own your planning stack](concepts/own-your-planning-stack.md)
- [Subagents as delegation](concepts/subagents-as-delegation.md)
- [Sand Castle parallelization](concepts/sand-castle-parallelization.md)
- [Pre-AI fundamentals](concepts/pre-ai-fundamentals.md)
- [Diagnose loop](concepts/diagnose-loop.md)
- [Zoom out](concepts/zoom-out.md)
- [Handoff docs](concepts/handoff-docs.md)

### review
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing](concepts/compacting-vs-clearing.md)
- [Clean-context reviewer](concepts/clean-context-reviewer.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)
- [Subagents as delegation](concepts/subagents-as-delegation.md)
- [Sand Castle parallelization](concepts/sand-castle-parallelization.md)
- [Pre-AI fundamentals](concepts/pre-ai-fundamentals.md)
- [Zoom out](concepts/zoom-out.md)

### qa
- [Sand Castle parallelization](concepts/sand-castle-parallelization.md)
- [Diagnose loop](concepts/diagnose-loop.md)
- [Triage state machine](concepts/triage-state-machine.md)
- [Integration testing bias](concepts/integration-testing-bias.md)

## Concepts by tag

### context-management
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)
- [Subagents as delegation](concepts/subagents-as-delegation.md)
- [Handoff docs](concepts/handoff-docs.md)

### review
- [Clean-context reviewer](concepts/clean-context-reviewer.md)

### prd
- [Grilling for alignment](concepts/grilling-alignment.md)
- [Doc rot](concepts/doc-rot.md)
- [PRD discipline](concepts/prd-discipline.md)

### architecture
- [Deep modules over shallow modules](concepts/deep-modules.md)
- [Design interfaces, delegate implementation](concepts/design-interfaces-delegate-implementation.md)

### parallelization
- [Kanban over phases](concepts/kanban-over-phases.md)
- [Sand Castle parallelization](concepts/sand-castle-parallelization.md)

### tdd
- [TDD for AFK](concepts/tdd-for-afk.md)
- [Feedback-loop ceiling](concepts/feedback-loop-ceiling.md)

### debugging
- [Diagnose loop](concepts/diagnose-loop.md)
- [Feedback-loop ceiling](concepts/feedback-loop-ceiling.md)

### documentation
- [Ubiquitous language](concepts/ubiquitous-language.md)
- [ADR discipline](concepts/adr-discipline.md)
- [Doc rot](concepts/doc-rot.md)
- [Just-in-time docs](concepts/just-in-time-docs.md)

### testing
- [Integration testing bias](concepts/integration-testing-bias.md)
- [TDD for AFK](concepts/tdd-for-afk.md)
- [Feedback-loop ceiling](concepts/feedback-loop-ceiling.md)

### triage
- [Triage state machine](concepts/triage-state-machine.md)
- [AFK vs HITL](concepts/afk-vs-hitl.md)

(other tags collapsed to misc — regenerate via `/build-index` for full breakdown)

## Sources

### YouTube
- [Vibe-Coding to Vibe-Engineering — Matt Pocock @ AI Engineer 2025](sources/youtube/pocock-vibe-engineering-2025.md)

### Repos
- [mattpocock/skills — Skills For Real Engineers](sources/repos/pocock-skills.md)

### Articles
- [Matt Pocock — aihero.dev articles (Jan–Mar 2026)](sources/articles/pocock-aihero-articles.md) — six posts consolidated

<details>
<summary>Deprecated (0)</summary>
(none yet)
</details>
