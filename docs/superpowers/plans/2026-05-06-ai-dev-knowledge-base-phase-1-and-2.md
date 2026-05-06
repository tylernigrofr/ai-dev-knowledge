# AI Dev Knowledge Base — Phase 1 + 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stand up a usable AI-driven-development knowledge base — directory skeleton, frontmatter schemas, hand-seeded starter content from the Matt Pocock material, and the core agent-facing skills (`kb-search`, `kb-pull`, `add-source`, `distill-concept`, `triage-inbox`, `build-index`).

**Architecture:** Plain Markdown files with YAML frontmatter as the source of truth. Three tiers: `sources/` (raw captures), `concepts/` (atomic, one-idea-per-file), `playbooks/` (workflow recipes citing concepts). Curation gate via `/distill-concept` keeps it lean. Cross-project agents pull via `kb-search` against `$AI_KB_PATH`.

**Tech Stack:** Markdown + YAML frontmatter, JSON Schema for validation, Claude Code skills (markdown prompt files in `skills/`), Supadata MCP for YouTube transcripts, PowerShell/Bash for any scripting (Windows host).

**Source spec:** [docs/superpowers/specs/2026-05-06-ai-dev-knowledge-base-design.md](../specs/2026-05-06-ai-dev-knowledge-base-design.md)

**Out of scope for this plan** (deferred to later plans):
- Phase 3 maintenance skills (`/update-playbook`, `/review-staleness`)
- Phase 4 static site (`site/` Astro Starlight project)
- Phase 5 future affordances (RAG chat, scheduled sweepers, plugin packaging)

---

## File Structure

| Path | Purpose |
|---|---|
| `README.md` | Human entry point: what this is, how it's structured, how to use it |
| `CONTEXT.md` | Ubiquitous-language doc + curation rules + frontmatter schemas (the project's own DDD glossary) |
| `INDEX.md` | Auto-generated multi-axis index (by type, phase, tag, status) |
| `.schemas/source.schema.json` | JSON Schema for source frontmatter |
| `.schemas/concept.schema.json` | JSON Schema for concept frontmatter |
| `.schemas/playbook.schema.json` | JSON Schema for playbook frontmatter |
| `.claude/settings.json` | Permissions for skills (read/write KB paths) |
| `sources/youtube/pocock-vibe-engineering-2025.md` | Seed source from the brainstorming conversation |
| `concepts/<12 starter concepts>.md` | Hand-seeded atomic concepts |
| `playbooks/afk-night-shift.md` | Stub playbook citing the concepts |
| `_inbox/urls.md` | Empty queue file (placeholder ready) |
| `_inbox/drops/.gitkeep` | Keep folder in git |
| `_inbox/_processed/.gitkeep` | Keep folder in git |
| `skills/kb-search.md` | Query KB by tag/type/phase/freetext |
| `skills/kb-pull.md` | Return full content for a slug |
| `skills/add-source.md` | One-shot source ingestion |
| `skills/distill-concept.md` | The curation gate |
| `skills/triage-inbox.md` | Batch inbox processor |
| `skills/build-index.md` | Regenerate `INDEX.md` |

---

## Task 1: Directory skeleton + .gitkeep placeholders

**Files:**
- Create: `_inbox/urls.md`, `_inbox/drops/.gitkeep`, `_inbox/_processed/.gitkeep`
- Create: `sources/youtube/.gitkeep`, `sources/articles/.gitkeep`, `sources/papers/.gitkeep`, `sources/repos/.gitkeep`, `sources/social/.gitkeep`
- Create: `concepts/.gitkeep`, `playbooks/.gitkeep`, `skills/.gitkeep`, `.schemas/.gitkeep`, `.claude/.gitkeep`

- [ ] **Step 1: Create all directories and placeholder files**

Use Bash:
```bash
mkdir -p _inbox/drops _inbox/_processed sources/youtube sources/articles sources/papers sources/repos sources/social concepts playbooks skills .schemas .claude
touch _inbox/drops/.gitkeep _inbox/_processed/.gitkeep sources/youtube/.gitkeep sources/articles/.gitkeep sources/papers/.gitkeep sources/repos/.gitkeep sources/social/.gitkeep concepts/.gitkeep playbooks/.gitkeep skills/.gitkeep .schemas/.gitkeep .claude/.gitkeep
```

- [ ] **Step 2: Create `_inbox/urls.md` with header**

Write to `_inbox/urls.md`:
```markdown
# Inbox: URLs to triage

One URL per line. The `/triage-inbox` skill processes and removes lines as it works through them.

<!-- urls go below this line -->
```

- [ ] **Step 3: Verify structure**

Run: `git status`
Expected: untracked files for all `.gitkeep` placeholders + `_inbox/urls.md`.

- [ ] **Step 4: Commit**

```bash
git add _inbox sources concepts playbooks skills .schemas .claude
git commit -m "chore: scaffold KB directory structure"
```

---

## Task 2: Write `CONTEXT.md`

**Files:**
- Create: `CONTEXT.md`

- [ ] **Step 1: Write `CONTEXT.md`**

```markdown
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
5. **Deprecated concepts stay** (link stability) but are hidden from the default `INDEX.md`. Use `status: deprecated` + `superseded_by: <slug>`.
6. **Playbooks must cite concepts.** Playbooks without `concepts_used:` are suspect.
7. **`last_reviewed` updates on any non-trivial edit.**

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
last_reviewed: 2026-05-06
---
```

Playbook body sections:
1. **Prerequisites** — what must be true before starting.
2. **Setup** — one-time configuration steps.
3. **Loop** — the recurring workflow steps.
4. **Verification** — how to know it worked.
5. **Failure modes** — what goes wrong and how to recover.

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
```

- [ ] **Step 2: Verify file exists**

Run: `ls CONTEXT.md`
Expected: file listed.

- [ ] **Step 3: Commit**

```bash
git add CONTEXT.md
git commit -m "docs: add CONTEXT.md ubiquitous-language and curation rules"
```

---

## Task 3: JSON Schemas for frontmatter validation

**Files:**
- Create: `.schemas/source.schema.json`, `.schemas/concept.schema.json`, `.schemas/playbook.schema.json`

- [ ] **Step 1: Write `.schemas/source.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Source frontmatter",
  "type": "object",
  "required": ["title", "type", "captured", "status"],
  "properties": {
    "title": { "type": "string" },
    "type": { "enum": ["youtube", "article", "paper", "repo", "social", "other"] },
    "url": { "type": "string" },
    "author": { "type": "string" },
    "published": { "type": "string", "format": "date" },
    "captured": { "type": "string", "format": "date" },
    "status": { "enum": ["raw", "extracted", "superseded"] },
    "concepts_seeded": { "type": "array", "items": { "type": "string" } }
  },
  "additionalProperties": false
}
```

- [ ] **Step 2: Write `.schemas/concept.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Concept frontmatter",
  "type": "object",
  "required": ["title", "type", "phase", "tags", "sources", "status", "last_reviewed"],
  "properties": {
    "title": { "type": "string" },
    "type": { "enum": ["mental-model", "principle", "technique", "tool", "framework", "anti-pattern", "workflow"] },
    "phase": {
      "type": "array",
      "items": { "enum": ["planning", "decomposition", "implementation", "review", "qa"] }
    },
    "tags": { "type": "array", "items": { "type": "string" } },
    "sources": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "status": { "enum": ["draft", "stable", "contested", "deprecated"] },
    "superseded_by": { "type": ["string", "null"] },
    "last_reviewed": { "type": "string", "format": "date" }
  },
  "additionalProperties": false
}
```

- [ ] **Step 3: Write `.schemas/playbook.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Playbook frontmatter",
  "type": "object",
  "required": ["title", "phase", "tags", "concepts_used", "status", "last_reviewed"],
  "properties": {
    "title": { "type": "string" },
    "phase": {
      "type": "array",
      "items": { "enum": ["planning", "decomposition", "implementation", "review", "qa"] }
    },
    "tags": { "type": "array", "items": { "type": "string" } },
    "concepts_used": { "type": "array", "items": { "type": "string" }, "minItems": 1 },
    "tools": { "type": "array", "items": { "type": "string" } },
    "status": { "enum": ["draft", "stable", "contested", "deprecated"] },
    "last_reviewed": { "type": "string", "format": "date" }
  },
  "additionalProperties": false
}
```

- [ ] **Step 4: Remove `.gitkeep`**

```bash
rm .schemas/.gitkeep
```

- [ ] **Step 5: Commit**

```bash
git add .schemas/
git commit -m "chore: add JSON Schemas for source/concept/playbook frontmatter"
```

---

## Task 4: `README.md`

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`**

```markdown
# AI Dev Knowledge Base

Curated, lean knowledge base of state-of-the-art AI-driven development practices and the proven software-engineering fundamentals they lean on. Optimized for **AI agents pulling context on demand**, browsable as a wiki as a free byproduct.

## What's in here

- **`sources/`** — raw captures (YouTube transcripts, articles, papers, repos, social posts).
- **`concepts/`** — atomic notes, one idea per file, citing sources.
- **`playbooks/`** — workflow-shaped recipes citing concepts.
- **`_inbox/`** — drop zone for unprocessed material; `/triage-inbox` resolves it.
- **`skills/`** — agent-facing verbs (`kb-search`, `kb-pull`, `add-source`, `distill-concept`, `triage-inbox`, `build-index`).
- **`CONTEXT.md`** — ubiquitous-language doc + curation rules + frontmatter schemas. **Read this first.**
- **`INDEX.md`** — auto-generated index. Regenerate with `/build-index`.

## How to use it (human)

- Browse `concepts/` and `playbooks/` directly, or open `INDEX.md`.
- Add new material by dropping URLs in `_inbox/urls.md` or files in `_inbox/drops/`. Then run `/triage-inbox`.

## How to use it (agent, from another project)

1. Ensure `AI_KB_PATH` is set in your shell to this repo's absolute path.
2. In your project's `CLAUDE.md`, add:
   > AI dev best practices live at `$AI_KB_PATH/`. Search `concepts/` and `playbooks/` by frontmatter tag/type/phase. Use the `kb-search` skill if installed.
3. Optionally copy or symlink `skills/kb-search.md` and `skills/kb-pull.md` into your project's `.claude/skills/`.

## Spec & design

- [Design spec](docs/superpowers/specs/2026-05-06-ai-dev-knowledge-base-design.md)
- [Phase 1+2 implementation plan](docs/superpowers/plans/2026-05-06-ai-dev-knowledge-base-phase-1-and-2.md)

## Curation philosophy

Lean over comprehensive. Default to refining existing concepts, not creating new ones. Every concept cites a source. Periodic audit (`/review-staleness`, future) prunes bloat. See `CONTEXT.md` for the full rules.
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add README"
```

---

## Task 5: Seed source — Pocock AI Engineer 2025

**Files:**
- Create: `sources/youtube/pocock-vibe-engineering-2025.md`

- [ ] **Step 1: Write source file**

Write to `sources/youtube/pocock-vibe-engineering-2025.md`. Use this exact content:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add sources/youtube/pocock-vibe-engineering-2025.md
git commit -m "docs(sources): add Pocock AI Engineer 2025 source with extracted insights"
```

---

## Task 6: Seed concepts (12 atomic notes)

**Files (all under `concepts/`):**
- `smart-zone-vs-dumb-zone.md`
- `compacting-vs-clearing.md`
- `grilling-alignment.md`
- `vertical-slices.md`
- `ralph-loop.md`
- `clean-context-reviewer.md`
- `push-vs-pull-context.md`
- `deep-modules.md`
- `afk-vs-hitl.md`
- `doc-rot.md`
- `three-route-prototype.md`
- `ubiquitous-language.md`

Each concept follows the body structure from `CONTEXT.md`: Summary → Why it matters → How to apply → Caveats → Related. Frontmatter validates against `.schemas/concept.schema.json`. All cite `sources/youtube/pocock-vibe-engineering-2025.md`. All `last_reviewed: 2026-05-06`. All `status: stable` unless noted.

- [ ] **Step 1: Write `concepts/smart-zone-vs-dumb-zone.md`**

```markdown
---
title: Smart zone vs dumb zone
type: mental-model
phase: [planning, implementation, review]
tags: [context-management, attention, token-budget]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Every LLM session has a smart zone (~100k tokens, regardless of advertised context window) where attention is clean, then degrades into a dumb zone making sloppy decisions.

## Why it matters
Advertised 1M-token windows do not buy you 10× more useful context — they buy you more dumb zone. Tasks that overflow the smart zone produce noticeably worse output: missed constraints, hallucinated APIs, contradictions with earlier decisions. Sizing tasks to fit the smart zone is the cheapest quality lever you have.

## How to apply
- Treat ~80–100k tokens as the practical working ceiling per session.
- Set up a token-count status line in your harness so you can see live usage. (See Pocock's article on aihero.dev.)
- When usage approaches the ceiling, clear context and resume from a handoff doc rather than continuing.
- Decompose tasks so each subtask fits comfortably under the ceiling.

## Caveats
- The 100k figure is a working heuristic, not a measurement. Different model versions and task shapes shift the cliff.
- For pure summarization or retrieval tasks, larger contexts degrade more gracefully than for reasoning-heavy tasks.

## Related
- [compacting-vs-clearing](compacting-vs-clearing.md) — what to do when you hit the ceiling
- [clean-context-reviewer](clean-context-reviewer.md) — applying the smart-zone principle to review
- [push-vs-pull-context](push-vs-pull-context.md) — managing what fills the smart zone
```

- [ ] **Step 2: Write `concepts/compacting-vs-clearing.md`**

```markdown
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
```

- [ ] **Step 3: Write `concepts/grilling-alignment.md`**

```markdown
---
title: Grilling for alignment (instead of spec-then-code)
type: technique
phase: [planning]
tags: [prd, alignment, brooks, design-of-design]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Reach a shared design concept by having the AI interview you relentlessly — one question at a time with a recommended answer — until 40–100 questions deep; the conversation is the alignment artifact, not the PRD that follows.

## Why it matters
Specs-to-code regeneration loops fail because the code is the battleground and you need eyes on it. What you actually need (per Brooks, *The Design of Design*) is a shared design concept between you and the model. Grilling produces it; reading a generated PRD does not. The PRD is just a summary — testing it tests nothing.

## How to apply
- Use a `/grill-me` skill (or `/grill-with-docs` for engineering work that should update `CONTEXT.md` and ADRs inline).
- Constrain to one question at a time, each with a recommended answer.
- Stop when novelty dies (three consecutive low-novelty questions) or you hit ~40 questions.
- Summarize into a PRD with a `/to-prd` skill — but **do not review the PRD afterward**. You already aligned.
- Include an out-of-scope section in the PRD to capture negative decisions (the definition of done).
- Pull in domain experts when grilling hits a question only they can answer.

## Caveats
- Grilling is permanently human-in-the-loop. You can't Ralph-loop alignment.
- For trivial tasks, a quick discussion beats a full grilling session.

## Related
- [doc-rot](doc-rot.md) — why PRDs in the repo become dangerous over time
- [ubiquitous-language](ubiquitous-language.md) — what gets updated during grilling
```

- [ ] **Step 4: Write `concepts/vertical-slices.md`**

```markdown
---
title: Vertical slices (tracer bullets) over horizontal layers
type: principle
phase: [decomposition, implementation]
tags: [decomposition, tracer-bullets, feedback-loops]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Decompose work into thin end-to-end slices that exercise the full stack, not into horizontal layers (DB → API → frontend) that defer feedback.

## Why it matters
AI agents — and humans — gravitate toward horizontal decomposition because it's locally tidy. The cost is that you don't see anything *work* until phase 3, by which time mistakes in phase 1 have compounded. Vertical slices give you a working flow on day one and continuous feedback. They also map naturally onto independently-grabbable kanban issues for parallel agent work.

## How to apply
- Every issue declares a "user-observable outcome" or is tagged `internal` / `infra` / `refactor` (and that's the explicit exception).
- Reject decompositions where issues are layer-shaped ("create user table", "build user API"). Re-shape into slices ("user can sign up and see their dashboard with placeholder data").
- The first slice should be the thinnest possible end-to-end demo. Subsequent slices add features, not layers.
- Build a small eval set of "good vs bad decompositions" to tune the `/decompose` skill over time.

## Caveats
- Some genuine cross-cutting work (auth, infrastructure, build pipeline) is layer-shaped by nature. Tag it explicitly so it doesn't pollute the rest of the board.

## Related
- [ralph-loop](ralph-loop.md) — what the slices feed into
- [afk-vs-hitl](afk-vs-hitl.md) — tagging slices for delegation
```

- [ ] **Step 5: Write `concepts/ralph-loop.md`**

```markdown
---
title: Ralph loop (AFK implementation)
type: workflow
phase: [implementation]
tags: [automation, agents, tdd]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
A simple bash loop that picks the next unblocked AFK-tagged issue, runs an agent with accept-edits permissions and a TDD-enforced prompt, commits, and repeats — turning issue queue into night-shift output.

## Why it matters
Once issues are vertically sliced and AFK-tagged, implementation becomes a delegation problem. The Ralph loop is the simplest pattern that delegates safely: bounded agent invocations, TDD as a quality gate, fresh-context reviewer between, no infinite-running daemons. It is also the substrate that more sophisticated parallel patterns (Pocock's sandcastle) wrap.

## How to apply
- Read all open AFK-tagged issues into a variable; grab the last N commits as context.
- Invoke the agent with `--permission-mode accept-edits`, a prompt that says: pick next unblocked AFK task → use TDD (red-green-refactor skill) → run feedback loops → commit → output a summary.
- After commit, fire a reviewer in a clean context (Opus recommended) that pushes coding standards and pulls only diffs/issue.
- On review pass: merge. On fail: kick to fix loop with max retries before flagging human-in-loop.
- Keep the implementer in Sonnet (or equivalent) and the reviewer in Opus for the cost-quality split.

## Caveats
- Cost scales with parallelism. Set per-issue and per-day budgets.
- Feedback-loop quality is the ceiling — slow tests, flaky assertions, or weak type errors directly cap output quality.

## Related
- [vertical-slices](vertical-slices.md) — what feeds the loop
- [clean-context-reviewer](clean-context-reviewer.md) — the review half
- [push-vs-pull-context](push-vs-pull-context.md) — context discipline within the loop
```

- [ ] **Step 6: Write `concepts/clean-context-reviewer.md`**

```markdown
---
title: Clean-context reviewer
type: principle
phase: [review]
tags: [review, context-isolation, quality-gate]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Every implementation must be reviewed by a fresh agent in a clean context that has not seen the implementation work — self-review happens in the dumb zone and catches almost nothing.

## Why it matters
An implementer that has been in-session has built justifications for its choices that survive into self-review. A clean reviewer has no such bias and judges the diff against the spec and standards alone. This is the most cost-effective single quality gate for AI-generated code.

## How to apply
- After each implementation commit, spawn a separate subprocess / session with no prior context.
- Feed the reviewer: the diff, the linked issue, push-style coding standards (`CONTEXT.md`, `ADR`s, `STANDARDS.md`).
- Use a smarter model for review than implementation — Pocock uses Opus for review and Sonnet for implementation.
- Output is structured pass/fail + findings. Gate merging on review pass.

## Caveats
- The reviewer's effectiveness is bounded by the standards it pushes. Vague standards → vague reviews.
- For trivial changes (typos, doc edits) the review overhead may exceed the value. Make the gate skippable, but default to on.

## Related
- [push-vs-pull-context](push-vs-pull-context.md) — what to push to the reviewer
- [smart-zone-vs-dumb-zone](smart-zone-vs-dumb-zone.md) — why fresh context matters
- [ralph-loop](ralph-loop.md) — where this fits in the AFK loop
```

- [ ] **Step 7: Write `concepts/push-vs-pull-context.md`**

```markdown
---
title: Push vs pull context
type: principle
phase: [implementation, review]
tags: [context-management, skills, system-prompt]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Push context = always-on instructions sent every turn (CLAUDE.md, system prompt). Pull context = on-demand fetched by the agent (skills with description headers). Push for reviewer, pull for implementer.

## Why it matters
Push tokens are spent every turn whether or not they're relevant — cheap when always-needed, wasteful otherwise. Pull tokens are spent only when the agent decides they're needed — efficient on average but only useful if the agent actually pulls. Reviewers want every relevant standard *every time* (push). Implementers want a clean working context plus the option to pull skills as needed (pull).

## How to apply
- Reviewer system prompt: concatenate everything in `push/` (coding standards, `CONTEXT.md`, ADRs, module map) ordered by priority; truncate from the bottom if over budget.
- Implementer system prompt: minimal — task description + tool to discover and pull from `skills/`.
- Skills used in pull mode must have a clear `description:` header so the agent's discovery step knows when to pull them.
- Anything pushed should justify being pushed every turn; otherwise demote to pull.

## Caveats
- An implementer that fails to pull a relevant skill is worse than one with the skill pushed. Monitor pull behavior; if a skill is missed often, consider pushing it.

## Related
- [clean-context-reviewer](clean-context-reviewer.md) — the canonical push consumer
- [ralph-loop](ralph-loop.md) — where push/pull discipline applies
```

- [ ] **Step 8: Write `concepts/deep-modules.md`**

```markdown
---
title: Deep modules over shallow modules
type: principle
phase: [planning, implementation]
tags: [architecture, ousterhout, testability, module-design]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Prefer deep modules (small interface, lots of functionality inside) over shallow modules (lots of tiny files with sprawled dependencies); deep modules let you draw clean test boundaries around real functionality.

## Why it matters
From Ousterhout's *A Philosophy of Software Design*. Shallow modules force you into mocking hell or testing nothing meaningful — and AI agents amplify the cost because they reason worse about scattered, tightly-coupled code. Deep modules give you a stable interface to test against, a small surface for the AI to reason about, and the ability to refactor internals without consumer changes.

## How to apply
- For each cluster of related code, identify the smallest reasonable public interface and hide everything else.
- Run something like `/improve-codebase-architecture` periodically to detect shallow-module clusters and propose consolidations.
- Maintain a canonical interface doc (e.g. `MODULES.md` or a section of `CONTEXT.md`) and treat divergence as a bug.
- Design module interfaces yourself; delegate the implementation. This keeps your mental map intact.

## Caveats
- "Deep" is not "huge." A 5000-line file is rarely a good module. The metric is interface narrowness vs. internal richness, not raw size.
- Forced consolidation across genuinely independent concerns creates worse coupling than the shallow case it replaces.

## Related
- [ubiquitous-language](ubiquitous-language.md) — what module names should match
- [push-vs-pull-context](push-vs-pull-context.md) — module map is canonical push content
```

- [ ] **Step 9: Write `concepts/afk-vs-hitl.md`**

```markdown
---
title: AFK vs human-in-the-loop tagging
type: technique
phase: [decomposition]
tags: [delegation, tagging, kanban]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Tag every issue as either AFK (delegate-able to an agent unsupervised) or human-in-the-loop (needs your judgment); the AFK queue feeds the night shift, HITL stays on your desk.

## Why it matters
Without explicit tagging, you either over-delegate (agents make decisions that need human judgment) or under-delegate (you stay in the loop on issues you don't need to be). Explicit tagging at decomposition time forces the question "can this be done unsupervised?" and produces a board where the night shift knows what it's allowed to grab.

## How to apply
- Add `mode: afk | human-in-loop` to every issue's frontmatter.
- Default to HITL; require justification to mark AFK (clear acceptance criteria, no ambiguous design questions, well-bounded scope).
- The Ralph loop only picks issues with `mode: afk`.
- Re-tag freely as you learn — issues that the night shift keeps tripping over should be flipped to HITL.

## Caveats
- Some issues are partially delegate-able. Either split them, or tag conservatively as HITL.

## Related
- [vertical-slices](vertical-slices.md) — what's being tagged
- [ralph-loop](ralph-loop.md) — the AFK consumer
```

- [ ] **Step 10: Write `concepts/doc-rot.md`**

```markdown
---
title: Doc rot in the repo
type: anti-pattern
phase: [planning, implementation]
tags: [prd, documentation, drift]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Closed PRDs left in the repo get found by future agents and used as authoritative even after the code has diverged; treat in-repo docs as living source-of-truth or remove them.

## Why it matters
Agents grep aggressively. Anything they find with a confident voice and matching keywords gets weighted as truth. A stale PRD describing a deprecated approach can override the actual code, especially when the code has no contradicting documentation. The bug surfaces as agents making "obvious" mistakes that come straight from the rotted doc.

## How to apply
- Don't keep closed PRDs as markdown in the repo. Close them in your issue tracker and let the tracker hold the history.
- Living docs (`CONTEXT.md`, ADRs, MODULES.md, playbooks) must have a clear update lifecycle and a `last_reviewed` field.
- Auto-archive docs whose linked issues have all closed (e.g. `prds/active/` → `prds/archived/`).
- Periodic audit (`/review-staleness`) for orphaned or drift-prone docs.

## Caveats
- Aggressive deletion loses useful context. The pattern is "move out of agent grep range," not "destroy."

## Related
- [grilling-alignment](grilling-alignment.md) — why PRDs exist in the first place
- [ubiquitous-language](ubiquitous-language.md) — the canonical living-doc example
```

- [ ] **Step 11: Write `concepts/three-route-prototype.md`**

```markdown
---
title: Three-route throwaway prototype (front-end)
type: technique
phase: [planning, implementation]
tags: [frontend, prototyping, multimodal-blindness]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
For UI work in mature codebases, don't try to one-shot a polished design — scaffold three throwaway routes with variant designs, click between them, pick what works, then grill the real implementation.

## Why it matters
AI is multimodal-blind on visual judgment. It can produce plausible UI code but cannot tell you which of three options actually feels right. The throwaway-routes pattern moves the visual judgment to a human (you), where it belongs, while still letting the AI generate the variants. Picking from three concrete options is dramatically more productive than describing what you want in words.

## How to apply
- Ask for three variants at routes like `/proto-a`, `/proto-b`, `/proto-c`.
- Make them genuinely different in approach (layout, density, interaction model), not minor color/spacing variations.
- Click through, pick the winner, screenshot if useful.
- Feed the chosen variant into a `/grill-with-docs` session for the real implementation. Discard the other two.

## Caveats
- For greenfield UIs without an existing codebase, more iterations may be valuable; the pattern is specifically for mature codebases where a polished one-shot is unlikely to fit existing conventions.

## Related
- [grilling-alignment](grilling-alignment.md) — what happens after you pick
```

- [ ] **Step 12: Write `concepts/ubiquitous-language.md`**

```markdown
---
title: Ubiquitous language (CONTEXT.md / DDD)
type: principle
phase: [planning, decomposition, implementation, review]
tags: [ddd, evans, glossary, context-md]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Maintain a `CONTEXT.md` in every project that defines the domain's shared language — every term that means something specific in this codebase has a definition there, and grilling sessions keep it current.

## Why it matters
From Eric Evans's *Domain-Driven Design*. When a codebase, a PRD, and an agent all use slightly different words for the same concept (or the same word for different concepts), every conversation has friction. A `CONTEXT.md` removes the ambiguity and gives the agent a deterministic place to look up jargon. It's also the cheapest possible "module map" — the names of modules and the names of concepts converge.

## How to apply
- One `CONTEXT.md` at the repo root. No nesting.
- One section per term: term name + 1–3 sentence definition + (optional) examples + (optional) related terms.
- Updated by `/grill-with-docs` whenever a grilling session reveals a term that wasn't defined or was used inconsistently.
- Pushed to reviewers (always-on) so reviews catch terminology drift.

## Caveats
- Don't define terms that are universal (e.g. "function", "class"). Only project-specific or overloaded terms.
- A CONTEXT.md that grows past a few hundred terms suggests the codebase needs decomposition more than the doc needs editing.

## Related
- [doc-rot](doc-rot.md) — what happens when CONTEXT.md isn't kept current
- [deep-modules](deep-modules.md) — module names should match CONTEXT terms
```

- [ ] **Step 13: Remove `concepts/.gitkeep`**

```bash
rm concepts/.gitkeep
```

- [ ] **Step 14: Commit**

```bash
git add concepts/
git commit -m "docs(concepts): seed 12 starter concepts from Pocock material"
```

---

## Task 7: Seed playbook stub — `afk-night-shift.md`

**Files:**
- Create: `playbooks/afk-night-shift.md`

- [ ] **Step 1: Write `playbooks/afk-night-shift.md`**

```markdown
---
title: AFK night-shift implementation loop
phase: [implementation]
tags: [parallelization, ralph-loop, sandcastle]
concepts_used:
  - ralph-loop
  - vertical-slices
  - afk-vs-hitl
  - clean-context-reviewer
  - push-vs-pull-context
  - smart-zone-vs-dumb-zone
tools: [sandcastle, opencode, claude-code]
status: draft
last_reviewed: 2026-05-06
---

## Prerequisites

- A backlog of issues that have been [vertically sliced](../concepts/vertical-slices.md) and tagged [AFK or HITL](../concepts/afk-vs-hitl.md).
- A `STANDARDS.md` (or equivalent) plus `CONTEXT.md` and any ADRs in a `docs/adr/` directory — these will be pushed to the reviewer.
- A working harness with sandboxed worktree support (e.g. Pocock's [sandcastle](https://github.com/mattpocock/sandcastle)) and per-task git worktrees.
- A red-green-refactor TDD skill installed (e.g. from `mattpocock/skills`).
- Per-issue and per-day cost budgets configured.

## Setup

1. Set up the sandcastle parallel-planner template (or equivalent harness):
   - Implementer prompt template at `.sandcastle/implement.md` referencing the TDD skill, accepting `{{ISSUE_NUMBER}}`, model = `claude-sonnet-4-6`, accept-edits permission.
   - Reviewer prompt template at `.sandcastle/review.md` that begins with `` !`cat CONTEXT.md` `` and `` !`cat docs/adr/*.md` `` and `` !`cat STANDARDS.md` ``, accepts `{{COMMIT_SHA}}`, model = `claude-opus-4-6`, read-only.
2. Wire up a logging hook so each agent invocation writes structured events to `.sandcastle/logs/` (consumed by the dashboard if present).
3. Confirm the issue tracker exposes "open AFK-tagged unblocked issues" via a single query (GitHub label query or local file scan).

## Loop

Per cycle (cron, manual, or watch-mode):

1. Query for unblocked `mode: afk` issues. If none, exit.
2. Pick the next N (default 3 for parallel; 1 for sequential).
3. For each issue, in its own git worktree + container:
   1. Run the implementer with `{{ISSUE_NUMBER}}` substituted. Use [TDD](../concepts/ralph-loop.md) — write failing test first.
   2. On commit, fire the reviewer in a [clean context](../concepts/clean-context-reviewer.md) against the diff.
   3. On review pass: merge into main; mark issue done.
   4. On review fail: kick to fix loop; max 2 retries before flagging human-in-loop.
4. Concurrently, run a QA-scout subagent that produces new issues against merged work — these land back on the kanban.
5. Repeat.

## Verification

- Successful cycle: open issue closed, commit on main, review report archived.
- Cost check: per-cycle cost within budget; if not, downgrade reviewer to Sonnet for low-risk slices.
- Drift check: `CONTEXT.md` and ADRs unchanged unless an issue explicitly touched them; flag silent drift.

## Failure modes

- **Implementer cheats the test.** Cause: TDD skill not pulled or weak. Fix: enforce skill via push, not pull, until trust is built.
- **Reviewer rubber-stamps.** Cause: standards too vague or push budget exhausted. Fix: tighten standards; trim non-load-bearing push content.
- **Cost runaway.** Cause: parallel Opus reviewers on big diffs. Fix: per-issue caps + downgrade reviewer to Sonnet on low-risk slices.
- **Merge conflicts pile up.** Cause: too many parallel implementers on related code. Fix: dependency-aware scheduling; the planner respects `blocked_by`.
- **Doc rot.** Cause: PRDs left in repo after issues close. Fix: see [doc-rot](../concepts/doc-rot.md).
```

- [ ] **Step 2: Remove `playbooks/.gitkeep`**

```bash
rm playbooks/.gitkeep
```

- [ ] **Step 3: Commit**

```bash
git add playbooks/
git commit -m "docs(playbooks): add afk-night-shift draft playbook"
```

---

## Task 8: Skill — `kb-search`

**Files:**
- Create: `skills/kb-search.md`

Skills in this KB are markdown prompt files with YAML frontmatter following the Claude Code skill format (name, description, instructions, examples). Their "test" is invocation — the verification step is to invoke and check output shape. Skills are not TDD'd in the conventional sense.

- [ ] **Step 1: Write `skills/kb-search.md`**

```markdown
---
name: kb-search
description: Use when the user or another agent needs to find concepts or playbooks in the AI dev knowledge base by tag, type, phase, or freetext. Returns a ranked list of matching files with one-line summaries. The main agent-facing retrieval verb of the KB.
---

# kb-search

Query the AI dev knowledge base at `$AI_KB_PATH` (or the current repo if invoked from inside the KB itself).

## Inputs

The user supplies one or more of:
- `query` — freetext keyword(s)
- `tag` — frontmatter tag (e.g. `context-management`)
- `type` — concept type (`mental-model | principle | technique | tool | framework | anti-pattern | workflow`)
- `phase` — lifecycle phase (`planning | decomposition | implementation | review | qa`)
- `kind` — `concept | playbook | source` (default: concept + playbook)

## Procedure

1. Resolve `$AI_KB_PATH`. If unset and not inside a KB repo, error with the message: "Set AI_KB_PATH or run from inside the KB repo."
2. List candidate files based on `kind` (default: `concepts/*.md` and `playbooks/*.md`).
3. Filter by frontmatter:
   - `tag` matches if it appears in the `tags` array.
   - `type` matches if `type:` equals (concepts only).
   - `phase` matches if it appears in the `phase` array.
   - Exclude `status: deprecated` unless explicitly requested via `include_deprecated: true`.
4. If `query` is provided, score remaining candidates by:
   - Title match (highest weight)
   - Tag match
   - Body match (Summary + Why it matters sections preferred)
5. Return top 10 results as a markdown list. Each item:
   - `[Title](relative/path.md)` — one-sentence summary (the Summary section).
   - Frontmatter chips: `type · phase · status`.

## Output format

```markdown
## kb-search results (N matches)

1. [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — Every LLM session has a smart zone (~100k tokens) where attention is clean, then degrades.
   `mental-model · planning,implementation,review · stable`
2. ...
```

## Examples

- "Find concepts tagged `context-management`" → filter by tag.
- "What does the KB say about reviewing AI code?" → freetext "review" + phase=review.
- "Show me all anti-patterns" → type=anti-pattern, no query.

## Caveats

- For deep retrieval (full content), use `kb-pull` after picking a result.
- This skill does not synthesize across results; it retrieves. Synthesis is the caller's job.
```

- [ ] **Step 2: Commit**

```bash
git add skills/kb-search.md
git commit -m "feat(skills): add kb-search retrieval skill"
```

---

## Task 9: Skill — `kb-pull`

**Files:**
- Create: `skills/kb-pull.md`

- [ ] **Step 1: Write `skills/kb-pull.md`**

```markdown
---
name: kb-pull
description: Use when an agent needs the full contents of a specific concept, playbook, or source from the AI dev knowledge base. Given a slug or path, returns the full markdown including frontmatter. Convenience wrapper around file read.
---

# kb-pull

Return the full contents of a single KB file.

## Inputs

- `slug` — the file slug (e.g. `smart-zone-vs-dumb-zone`) or full relative path (e.g. `concepts/smart-zone-vs-dumb-zone.md`).
- `kind` (optional) — `concept | playbook | source`. Used to disambiguate slug-only inputs.

## Procedure

1. Resolve `$AI_KB_PATH`.
2. If `slug` is a full path, read it. Else search:
   - `concepts/<slug>.md` if `kind` is concept or unspecified.
   - `playbooks/<slug>.md` if `kind` is playbook or unspecified.
   - `sources/*/<slug>.md` if `kind` is source or unspecified.
3. If multiple matches, list them and ask the caller to disambiguate.
4. Return the full file contents (frontmatter + body).

## Output format

Return raw markdown. The caller can render or excerpt as needed.

## Caveats

- For multi-file retrieval, call `kb-search` first.
- Deprecated entries are still pullable; the caller is responsible for noting the status.
```

- [ ] **Step 2: Commit**

```bash
git add skills/kb-pull.md
git commit -m "feat(skills): add kb-pull retrieval skill"
```

---

## Task 10: Skill — `add-source`

**Files:**
- Create: `skills/add-source.md`

- [ ] **Step 1: Write `skills/add-source.md`**

```markdown
---
name: add-source
description: Use when the user provides a single URL or pasted text and wants it added to the KB right now (skipping the inbox). Handles YouTube via Supadata MCP, articles via web fetch, and pasted text directly. Calls distill-concept after the source is captured.
---

# add-source

One-shot ingestion of a single source.

## Inputs

- A URL or pasted text.
- Optional: `type` override (`youtube | article | paper | repo | social | other`). Inferred from URL if not provided.
- Optional: `slug` override. Inferred from title if not provided.

## Procedure

1. **Capture content** based on type:
   - **YouTube**: Use the Supadata MCP `supadata_transcript` tool to fetch the transcript. Capture title, author, URL, published date if available.
   - **Article**: Fetch the page (web fetch). Capture title, author, URL, published date. Strip nav/footer; keep main content.
   - **Paper**: Same as article; flag `type: paper` for academic sources.
   - **Repo**: Capture README + key file paths + install notes. Note what's worth stealing.
   - **Social**: Capture the post text + author + URL. Often short — concept distillation will be the bulk of the work.
   - **Pasted text**: Treat as `type: other` unless overridden. Author = unknown unless provided.
2. **Write source file** to `sources/<type>/<slug>.md` with frontmatter per `.schemas/source.schema.json`.
3. **Extract candidate insights** from the captured content. Each insight should be a single load-bearing claim attributable to one or more concepts.
4. **For each candidate insight, call `distill-concept`**. The curation gate decides Refine / Replace / Supersede / Reject / Create.
5. **Update the source file's `concepts_seeded` array** with all concept slugs that were created or refined.
6. **Report** what was captured, what concepts were touched, and what was rejected.

## Output format

```markdown
## add-source result

**Source:** `sources/youtube/<slug>.md`
**Title:** ...
**Type:** youtube

**Concepts touched:**
- created: `concepts/foo.md`
- refined: `concepts/bar.md` (added "Why it matters" paragraph from new source)
- rejected: 2 candidate insights (duplicates of existing material)
```

## Caveats

- For long sources (full books, multi-hour videos), summarize before distilling — the smart zone applies.
- Paywalled articles: capture only what you have access to; note the limitation in the source body.
- Don't over-extract. Five high-quality insights beat twenty low-quality ones.
```

- [ ] **Step 2: Commit**

```bash
git add skills/add-source.md
git commit -m "feat(skills): add add-source ingestion skill"
```

---

## Task 11: Skill — `distill-concept`

**Files:**
- Create: `skills/distill-concept.md`

- [ ] **Step 1: Write `skills/distill-concept.md`**

```markdown
---
name: distill-concept
description: The KB curation gate. Use when a single insight needs to be routed into the concepts/ tree — decides Refine / Replace section / Supersede / Reject / Create. Called by add-source and triage-inbox; rarely invoked directly. The skill that keeps the KB lean.
---

# distill-concept

Apply the curation gate to a single insight.

## Inputs

- `insight` — a one-paragraph statement of the claim, with attribution to its source file.
- `source` — the source file slug or path the insight comes from.

## Procedure

1. **Find candidate concepts** — call `kb-search` with the insight's keywords + likely tags. Examine top 5 matches.
2. **Decide one of**:
   - **Refine** — the insight is a small clarification, a better phrasing, or a new example for an existing concept. Edit that concept inline. Bump `last_reviewed`. Add the source to `sources:` if not already there.
   - **Replace section** — the insight clearly improves one section (e.g. "How to apply") of an existing concept. Edit that section, preserve the rest. Bump `last_reviewed`. Add source.
   - **Supersede** — the insight is a materially better version of an existing concept's core claim. Mark the existing concept `status: deprecated` and add `superseded_by: <new-slug>`. Create the new concept. Old file stays for link integrity.
   - **Reject** — the insight is a duplicate or weaker than what's already in the KB. Log the rejection with reason in the triage report. Do not modify the KB.
   - **Create** — last resort. Only when no existing concept reasonably absorbs the insight. Justify in the triage report.
3. **Validate frontmatter** for any new or modified file against `.schemas/concept.schema.json`.
4. **Enforce the rules from CONTEXT.md**:
   - One idea per file. If the new file would not summarize in one sentence, decompose first.
   - 200-line soft cap. If a refine would push past it, decompose the existing concept instead.
   - Cite ≥1 source. Always.
5. **Report** the decision and the diff.

## Output format

```markdown
## distill-concept decision

**Insight:** "..."
**Source:** `sources/...`

**Decision:** refine
**Target:** `concepts/smart-zone-vs-dumb-zone.md`
**Change:** appended new "How to apply" bullet about token-count status line.
**last_reviewed:** updated to 2026-05-06
```

## Decision heuristics

- Two existing concepts both partially match → prefer the closer one and refine. Don't split the insight across both.
- Existing concept is older than 12 months and the new source post-dates a relevant model release → bias toward Supersede.
- Insight contradicts an existing concept → mark existing as `status: contested` and surface for human review rather than auto-Supersede.
- Brand-new domain that the KB doesn't cover at all → Create, but verify by searching twice with different keywords first.

## Caveats

- The default action is **Refine**. Create is the rarest outcome in a healthy KB. If you find yourself Creating most of the time, you're probably missing existing concepts in search.
- Refines should be small. A "refine" that touches every section is actually a Replace or a Supersede in disguise.
```

- [ ] **Step 2: Commit**

```bash
git add skills/distill-concept.md
git commit -m "feat(skills): add distill-concept curation gate skill"
```

---

## Task 12: Skill — `triage-inbox`

**Files:**
- Create: `skills/triage-inbox.md`

- [ ] **Step 1: Write `skills/triage-inbox.md`**

```markdown
---
name: triage-inbox
description: Use when the user wants to process accumulated material in _inbox/ — URLs in urls.md and drop files in drops/. Routes each item to source / seed / junk via add-source and distill-concept, then archives processed drops to _processed/. The batch verb of the KB ingestion pipeline.
---

# triage-inbox

Batch-process the inbox.

## Inputs

None — operates on the contents of `_inbox/` in the current KB.

## Procedure

### 1. Process `_inbox/urls.md`

For each non-comment, non-blank line:
1. Treat the line as a URL. Detect type from the URL (youtube.com / youtu.be → youtube, github.com → repo, x.com / twitter.com → social, else article).
2. Call `add-source` with the URL.
3. On success, remove the line from `urls.md`.
4. On failure (network, paywall, parse), leave the line and append a comment with the error.

### 2. Process `_inbox/drops/*.md`

For each drop file (sorted by filename, oldest first):
1. **Classify** the drop:
   - **Source-shaped** — has a clear external attribution (URL, author, publication). Treat as a pasted-source.
   - **Seed-shaped** — half-formed thoughts, snippets without clear attribution, the user's own ideas.
   - **Junk** — empty, duplicate, or obvious test content.
2. **Route**:
   - Source-shaped → call `add-source` with the pasted text.
   - Seed-shaped → extract the load-bearing claim(s) and call `distill-concept` directly with `source: <drop-path>`. (For seeds, the drop file *is* the source — copy it to `sources/social/` or `sources/other/` as appropriate before distilling.)
   - Junk → delete.
3. **Archive** the drop file:
   - Move to `_inbox/_processed/YYYY-MM/<original-filename>` where YYYY-MM is the drop's month.
   - Append a routing-header line at the end of the file: `<!-- routed: → concepts/foo.md, sources/youtube/bar.md -->`

### 3. Report

After the batch, output a triage report covering:
- URLs processed (✅ / ❌ with reasons)
- Drops processed (counts by route: source / seed / junk)
- Concepts created / refined / superseded / rejected
- Any items requiring user review (e.g. flagged `status: contested`)

## Output format

```markdown
## Triage report — 2026-05-06

### URLs (3 processed, 1 failed)
- ✅ https://youtu.be/X → sources/youtube/foo.md (refined 2 concepts)
- ✅ https://example.com/article → sources/articles/bar.md (created concepts/baz.md)
- ❌ https://paywalled.com/x — paywall, left in queue

### Drops (5 processed)
- 3 source-shaped → 3 sources, 7 concept refinements
- 1 seed → 1 concept refinement
- 1 junk → deleted

### Needs user review
- `concepts/old-thing.md` flagged `status: contested` — new source contradicts current claim
```

## Caveats

- Run incrementally. A 50-drop inbox in one session will exceed the smart zone — process in batches of ~10.
- After triage, run `build-index` to refresh `INDEX.md`.
- If a drop is clearly mis-categorized, fix the classification rather than forcing it through.
```

- [ ] **Step 2: Commit**

```bash
git add skills/triage-inbox.md
git commit -m "feat(skills): add triage-inbox batch processor skill"
```

---

## Task 13: Skill — `build-index`

**Files:**
- Create: `skills/build-index.md`

- [ ] **Step 1: Write `skills/build-index.md`**

```markdown
---
name: build-index
description: Use when concepts or playbooks have been added, modified, or deprecated and INDEX.md needs to be regenerated. Produces a multi-axis index (by type, phase, tag, status) reading from frontmatter. Hides deprecated entries by default.
---

# build-index

Regenerate `INDEX.md` from frontmatter.

## Procedure

1. **Read** all `concepts/*.md` and `playbooks/*.md`. Parse frontmatter.
2. **Validate** each frontmatter against `.schemas/concept.schema.json` and `.schemas/playbook.schema.json`. Collect errors but do not abort — emit a warnings section at the end of the index.
3. **Build sections**:
   - **Playbooks** (top of index, all playbooks alphabetically by title, with one-line summary).
   - **Concepts by type** — one subsection per `type` (mental-model, principle, technique, tool, framework, anti-pattern, workflow). Within each, alphabetical.
   - **Concepts by phase** — cross-cut. One subsection per phase with concepts that include it.
   - **Concepts by tag** — one subsection per tag, listing concepts. Tags appearing in only one concept can collapse to a "Misc tags" footer.
   - **Sources** — by type, alphabetical, link only. Source content is for citation, not browsing.
   - **Deprecated** (collapsed `<details>`) — concepts with `status: deprecated`, with their `superseded_by` link.
4. **Append a generation timestamp** at the bottom: `_Generated: YYYY-MM-DD HH:MM_`.
5. **Append warnings section** if any frontmatter validation failed.
6. **Write** `INDEX.md`.

## Output format

```markdown
# Index

_Last generated: 2026-05-06 14:30_

## Playbooks

- [AFK night-shift implementation loop](playbooks/afk-night-shift.md) — `draft`

## Concepts by type

### Mental models
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — ...

### Principles
- ...

### Anti-patterns
- ...

(etc.)

## Concepts by phase

### planning
- ...

(etc.)

## Concepts by tag

### context-management
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)

(etc.)

## Sources

### YouTube
- [Vibe-Coding to Vibe-Engineering](sources/youtube/pocock-vibe-engineering-2025.md)

<details>
<summary>Deprecated (0)</summary>
(none yet)
</details>

<details>
<summary>Warnings</summary>
(none)
</details>
```

## Caveats

- This skill is purely deterministic — no LLM judgment in the index itself. The cleanest implementation is a script; this skill describes the contract.
- Run after every triage session and before any commit-bump that touches frontmatter.
```

- [ ] **Step 2: Commit**

```bash
git add skills/build-index.md
git commit -m "feat(skills): add build-index regeneration skill"
```

---

## Task 14: `.claude/settings.json` — skill permissions

**Files:**
- Create: `.claude/settings.json`

- [ ] **Step 1: Write `.claude/settings.json`**

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/main/schemas/settings.schema.json",
  "permissions": {
    "allow": [
      "Read(concepts/**)",
      "Read(playbooks/**)",
      "Read(sources/**)",
      "Read(_inbox/**)",
      "Read(.schemas/**)",
      "Read(CONTEXT.md)",
      "Read(README.md)",
      "Read(INDEX.md)",
      "Edit(concepts/**)",
      "Edit(playbooks/**)",
      "Edit(sources/**)",
      "Edit(_inbox/**)",
      "Edit(INDEX.md)",
      "Write(concepts/**)",
      "Write(playbooks/**)",
      "Write(sources/**)",
      "Write(_inbox/**)",
      "Write(INDEX.md)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(mv:*)",
      "Bash(rm _inbox/**)"
    ]
  }
}
```

- [ ] **Step 2: Remove `.claude/.gitkeep`**

```bash
rm .claude/.gitkeep
```

- [ ] **Step 3: Commit**

```bash
git add .claude/settings.json
git commit -m "chore: add .claude/settings.json with skill permissions"
```

---

## Task 15: Generate first `INDEX.md`

**Files:**
- Create: `INDEX.md`

- [ ] **Step 1: Manually generate `INDEX.md`** following the contract in `skills/build-index.md`

This first generation is by hand; subsequent regenerations call the skill. Write to `INDEX.md`:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add INDEX.md
git commit -m "docs: generate initial INDEX.md"
```

---

## Task 16: Set `AI_KB_PATH` env var (user-side, not in repo)

This step is performed by the user in their shell profile, not committed to the repo.

- [ ] **Step 1: Add `AI_KB_PATH` to PowerShell profile**

In PowerShell, run:

```powershell
$repoPath = (Resolve-Path "C:\Users\tnigr\OneDrive\Documents\GitHub\ai-dev-knowledge").Path
Add-Content -Path $PROFILE -Value "`n`$env:AI_KB_PATH = '$repoPath'" -Encoding utf8
```

Then reload the profile or restart the shell:

```powershell
. $PROFILE
$env:AI_KB_PATH
```

Expected: prints the repo path.

- [ ] **Step 2: (Optional) Add to bash profile if you also use bash**

```bash
echo 'export AI_KB_PATH="/c/Users/tnigr/OneDrive/Documents/GitHub/ai-dev-knowledge"' >> ~/.bashrc
source ~/.bashrc
echo $AI_KB_PATH
```

Expected: prints the repo path.

(No commit — this lives in user shell config, not the repo.)

---

## Task 17: Smoke test — invoke `kb-search`

This task validates the end-to-end flow without writing any code. The success criterion is that an agent invocation of the `kb-search` skill returns expected results from the seeded content.

- [ ] **Step 1: Invoke `kb-search` from inside the KB**

In Claude Code (or equivalent), from the KB directory, ask:

> Use the kb-search skill to find concepts tagged `context-management`.

Expected output: a list including `smart-zone-vs-dumb-zone`, `compacting-vs-clearing`, `push-vs-pull-context`. Each with one-line summary and frontmatter chips.

- [ ] **Step 2: Invoke `kb-pull` for one of the results**

Ask:

> Use the kb-pull skill to fetch `smart-zone-vs-dumb-zone`.

Expected output: full markdown of `concepts/smart-zone-vs-dumb-zone.md` including frontmatter.

- [ ] **Step 3: Verify cross-project consumption**

From a different repo on disk, ask Claude Code:

> What does the AI dev knowledge base at `$env:AI_KB_PATH` say about reviewing AI-generated code?

Expected: agent searches `concepts/` for the topic and returns content from `clean-context-reviewer.md` (likely also `push-vs-pull-context.md` and `smart-zone-vs-dumb-zone.md`).

- [ ] **Step 4: If smoke tests pass, mark phase complete**

Append a note to `README.md` under "Spec & design":

```markdown
- Phase 1+2 implementation completed: 2026-05-06.
```

Commit:

```bash
git add README.md
git commit -m "docs: mark Phase 1+2 implementation complete"
```

If smoke tests fail, file the failure as a follow-up issue (skill prompt tuning is the most likely fix) and iterate before declaring complete.

---

## Self-review notes

**Spec coverage** — every section in the spec is mapped to a task:
- Repo shape → Task 1
- CONTEXT.md (ubiquitous language + curation rules + frontmatter schemas) → Task 2
- JSON Schemas → Task 3
- README → Task 4
- Seed source → Task 5
- 12 starter concepts → Task 6
- Playbook stub → Task 7
- 6 core skills (kb-search, kb-pull, add-source, distill-concept, triage-inbox, build-index) → Tasks 8–13
- `.claude/settings.json` → Task 14
- Initial INDEX.md → Task 15
- `AI_KB_PATH` env var → Task 16
- Smoke test → Task 17

Phase 3 (`/update-playbook`, `/review-staleness`), Phase 4 (Astro Starlight site), and Phase 5 (RAG chat, scheduled sweepers, plugin packaging) are deferred to future plans, as called out in the spec's "Out of scope" section.

**Type consistency** — concept slugs used in Task 6, Task 7's playbook frontmatter, Task 15's INDEX.md, and Task 8's example output all use the same vocabulary: `smart-zone-vs-dumb-zone`, `compacting-vs-clearing`, `grilling-alignment`, `vertical-slices`, `ralph-loop`, `clean-context-reviewer`, `push-vs-pull-context`, `deep-modules`, `afk-vs-hitl`, `doc-rot`, `three-route-prototype`, `ubiquitous-language`. Phase vocabulary (`planning | decomposition | implementation | review | qa`) and concept-type vocabulary (`mental-model | principle | technique | tool | framework | anti-pattern | workflow`) are consistent across CONTEXT.md, the JSON Schemas, frontmatter, and INDEX.md sections.
