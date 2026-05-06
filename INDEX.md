# Index

_Last generated: 2026-05-06_

## Playbooks

- [AFK night-shift implementation loop](playbooks/afk-night-shift.md) — `draft`

## Concepts by type

### Mental models
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — Every LLM session has a smart zone (~100k tokens) where attention is clean, then degrades.

### Principles
- [Clean-context reviewer](concepts/clean-context-reviewer.md) — Every implementation must be reviewed by a fresh agent in a clean context.
- [Deep modules over shallow modules](concepts/deep-modules.md) — Prefer small interfaces with rich internals over many tiny files.
- [Push vs pull context](concepts/push-vs-pull-context.md) — Push for reviewers, pull for implementers.
- [Ubiquitous language (CONTEXT.md / DDD)](concepts/ubiquitous-language.md) — Every project keeps a glossary of its domain terms.
- [Vertical slices (tracer bullets) over horizontal layers](concepts/vertical-slices.md) — Decompose into thin end-to-end slices.

### Techniques
- [AFK vs human-in-the-loop tagging](concepts/afk-vs-hitl.md) — Tag every issue as delegate-able or judgment-needed.
- [Grilling for alignment](concepts/grilling-alignment.md) — Have the AI interview you to reach a shared design concept.
- [Three-route throwaway prototype (front-end)](concepts/three-route-prototype.md) — Three variant routes, pick the winner, then implement.

### Workflows
- [Ralph loop (AFK implementation)](concepts/ralph-loop.md) — Bash loop that picks the next AFK issue and runs an agent on it.

### Anti-patterns
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md) — Compacting accumulates sediment; clearing wins.
- [Doc rot in the repo](concepts/doc-rot.md) — Stale PRDs in the repo become authoritative for future agents.

## Concepts by phase

### planning
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Grilling for alignment](concepts/grilling-alignment.md)
- [Deep modules](concepts/deep-modules.md)
- [Doc rot](concepts/doc-rot.md)
- [Three-route prototype](concepts/three-route-prototype.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)

### decomposition
- [Vertical slices](concepts/vertical-slices.md)
- [AFK vs HITL](concepts/afk-vs-hitl.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)

### implementation
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing](concepts/compacting-vs-clearing.md)
- [Vertical slices](concepts/vertical-slices.md)
- [Ralph loop](concepts/ralph-loop.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)
- [Deep modules](concepts/deep-modules.md)
- [Doc rot](concepts/doc-rot.md)
- [Three-route prototype](concepts/three-route-prototype.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)

### review
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing](concepts/compacting-vs-clearing.md)
- [Clean-context reviewer](concepts/clean-context-reviewer.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)
- [Ubiquitous language](concepts/ubiquitous-language.md)

### qa
(none yet)

## Concepts by tag

### context-management
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)

### review
- [Clean-context reviewer](concepts/clean-context-reviewer.md)

### prd
- [Grilling for alignment](concepts/grilling-alignment.md)
- [Doc rot](concepts/doc-rot.md)

### architecture
- [Deep modules over shallow modules](concepts/deep-modules.md)

(other tags collapsed to misc — regenerate via `/build-index` for full breakdown)

## Sources

### YouTube
- [Vibe-Coding to Vibe-Engineering — Matt Pocock @ AI Engineer 2025](sources/youtube/pocock-vibe-engineering-2025.md)

<details>
<summary>Deprecated (0)</summary>
(none yet)
</details>
