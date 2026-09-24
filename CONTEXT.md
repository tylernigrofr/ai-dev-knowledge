# CONTEXT.md — AI Dev Knowledge Base

The project's ubiquitous-language doc, curation rules, and frontmatter schemas.

## Ubiquitous language

- **Source** — a raw capture of an external artifact (YouTube transcript, article snapshot, social post, repo notes). Lives in `sources/<type>/`. Cited by concepts.
- **Concept** — an atomic, single-idea note. One file per idea. Tagged by type, phase, and free-form tags. Always cites ≥1 source.
- **Playbook** — a workflow-shaped recipe (prerequisites → setup → loop → verification → failure modes). Cites the concepts that justify each step.
- **Drop** — a messy item dropped into `_inbox/drops/` for triage (social post paste, half-formed thought, snippet).
- **Triage** — the process of routing drops/URLs into sources, concepts, or the trash.
- **Curation gate** — the Refine / Replace / Supersede / Reject / Create decision applied to every new insight.
- **Phase** — lifecycle phase a concept/playbook touches: `planning | decomposition | implementation | review | qa`.
- **Type (concept)** — `mental-model | principle | technique | tool | framework | anti-pattern | workflow`.

## Curation rules

1. **One idea per concept file.** Can't summarize the concept in one sentence → split.
2. **Soft cap: 200 lines / ~1500 words per concept.** Audit flags overruns.
3. **Default to refine, not create.** New concept files require justification — most insights should refine an existing concept rather than spawn a new one.
4. **Every concept cites ≥1 source.** No uncited claims.
5. **Deprecated concepts and playbooks stay** (link stability) but are hidden from search and collapsed in `INDEX.md`. Use `status: deprecated` + `superseded_by: <slug>` and a one-line `> **Deprecated.**` note above the Summary.
6. **Playbooks must cite concepts.** Playbooks without `concepts_used:` are suspect.
7. **`last_reviewed` updates on any non-trivial edit.**
8. **Owner practice is a first-class source.** Lessons from the owner's own repos are captured as `sources/repos/*-practice.md`, generalized (no private product detail, since this repo is public).

## Frontmatter schemas

### `sources/<type>/<slug>.md`

```yaml
---
title: "Vibe-Coding to Vibe-Engineering — Matt Pocock @ AI Engineer 2025"
type: youtube              # youtube | article | paper | repo | social | other
url: https://youtu.be/QFHIoCo-Ko
author: Matt Pocock
published: 2025-10-01
captured: 2026-05-06
status: extracted          # raw | extracted | superseded
concepts_seeded: [smart-zone-vs-dumb-zone, grilling-alignment]
---
```

### `concepts/<slug>.md`

```yaml
---
title: Smart zone vs dumb zone
type: mental-model         # mental-model | principle | technique | tool | framework | anti-pattern | workflow
phase: [planning, implementation, review]
tags: [context-management, attention, token-budget]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable             # draft | stable | contested | deprecated
superseded_by: null
last_reviewed: 2026-05-06
referenced_by: []          # computed by `scripts/kb.py refs`; never hand-edit
audience: [planner, implementer, reviewer]   # which agent role(s) this concept serves
activate_when: "context window is filling and attention is degrading"  # one-line trigger for pulling it
counter_to: null           # optional: the positive concept this anti-pattern opposes
cluster: context-management  # optional: its single cluster in concepts/_clusters/
---
```

Concept body sections (in order):

1. **Summary** — one sentence stating the claim, copy-pasteable.
2. **Why it matters** — ~3 sentences on stakes / impact.
3. **How to apply** — concrete steps, rules, or snippets.
4. **Caveats** — when it doesn't apply, contested points.
5. **Related** — links to related concepts, opposing concepts, anti-patterns.

### `playbooks/<slug>.md`

```yaml
---
title: AFK night-shift implementation loop
phase: [implementation]
tags: [parallelization, ralph-loop, sandcastle]
concepts_used: [ralph-loop, vertical-slices, push-vs-pull-context, clean-context-reviewer]
tools: [sandcastle, opencode, claude-code]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---
```

Playbook body sections:
1. **Prerequisites** — what must be true before starting.
2. **Setup** — one-time configuration steps.
3. **Loop** — the recurring workflow steps.
4. **Verification** — how to know it worked.
5. **Failure modes** — what goes wrong and how to recover.

## Clusters

`concepts/_clusters/<slug>.md` are thin deep-module indexes over the flat concept list: a seam statement plus members with one-line roles. A concept opts in with `cluster: <slug>`. Membership is single-assignment, and deprecated concepts are not members. `kb.py lint` checks that each cluster lists its members.

## Inbox lifecycle

- URLs → `_inbox/urls.md` (one per line).
- Messier drops → `_inbox/drops/YYYY-MM-DD-<slug>.md`.
- `/triage-inbox` routes each to: **source** (migrate to `sources/`), **seed** (distill into concept(s)), or **junk** (delete).
- Processed drops move to `_inbox/_processed/YYYY-MM/` with a routing-header line appended.

## Curation gate (`/distill-concept`)

For every new insight, pick exactly one:
- **Refine** — small clarification / better phrasing / new example. Edit existing concept.
- **Replace section** — new info clearly improves a part. Edit that section, note the source.
- **Supersede** — new idea materially better. Mark old `status: deprecated`, add `superseded_by`. Old file stays.
- **Reject** — duplicate or weaker. Drop it, log why.
- **Create** — last resort. Only when no existing concept can absorb the idea.
