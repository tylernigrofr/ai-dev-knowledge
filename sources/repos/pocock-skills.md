---
title: "mattpocock/skills — Skills For Real Engineers"
type: repo
url: https://github.com/mattpocock/skills
author: Matt Pocock
published: 2026-01-01
captured: 2026-05-06
recaptured: 2026-09-24   # v1.2.3, see bottom section
status: extracted
concepts_seeded:
  - diagnose-loop
  - triage-state-machine
  - zoom-out
  - handoff-docs
  - adr-discipline
  - three-route-prototype
  - deep-modules
  - grilling-alignment
  - mock-at-boundaries
  - design-it-twice
  - dependency-categories
  - agent-brief-format
  - out-of-scope-knowledge-base
  - tdd-for-afk
  - integration-testing-bias
---

# mattpocock/skills

Pocock's working `.claude/` directory, published as a reusable skills pack. Installed via `npx skills@latest add mattpocock/skills` and bootstrapped per-repo with `/setup-matt-pocock-skills`.

## Framing — the four failure modes (from README)

Pocock organizes the skills around four common agent failure modes:

1. **Misalignment** — agent didn't do what you wanted. → `/grill-me`, `/grill-with-docs`.
2. **Verbosity / jargon mismatch** — agent uses 20 words where 1 will do because there's no shared language. → `CONTEXT.md` glossary built up via `/grill-with-docs`.
3. **Code doesn't work** — feedback loops are weak. → `/tdd`, `/diagnose`.
4. **Ball of mud** — agents accelerate software entropy because they don't care about design. → `/to-prd` quizzes about modules touched, `/zoom-out` forces broader perspective, `/improve-codebase-architecture` rescues drifting codebases.

## Engineering skills (canonical list)

| Skill | Purpose |
|-------|---------|
| `/grill-with-docs` | Grilling that updates `CONTEXT.md` and ADRs inline |
| `/to-prd` | Synthesize current conversation into a PRD (no interview, just summary) |
| `/to-issues` | Decompose a plan/PRD into independently-grabbable issues, vertical slices |
| `/triage` | State-machine triage of issues through canonical roles |
| `/tdd` | Red-green-refactor loop with mocking/refactoring sub-docs |
| `/diagnose` | Disciplined six-phase debug loop |
| `/improve-codebase-architecture` | Find deepening opportunities; uses architecture vocabulary |
| `/prototype` | Throwaway prototype — bifurcates into logic (terminal) vs UI (multi-route) |
| `/zoom-out` | Force agent up a level of abstraction over unfamiliar code |
| `/setup-matt-pocock-skills` | Per-repo scaffold: issue-tracker choice, triage labels, doc paths |

## Productivity / misc skills

`caveman` (compressed comms), `grill-me` (non-code grilling), `write-a-skill`, `git-guardrails-claude-code`, `setup-pre-commit`, `handoff` (in-progress).

## Load-bearing extracted insights

### From `/diagnose`
- **Phase 1 (build a feedback loop) is the skill.** Everything else is mechanical. Spend disproportionate effort here.
- 10-tier ranked menu of feedback-loop construction, from "failing test" to "HITL bash script" as last resort.
- For non-deterministic bugs: don't aim for a clean repro, aim for a higher reproduction *rate*. Loop the trigger 100×.
- Generate **3–5 ranked falsifiable hypotheses** before testing any. Show the list to the user — they often re-rank instantly.
- Tag every debug log with a unique prefix like `[DEBUG-a4f2]` so cleanup is one grep.
- Write the regression test before the fix — but only if there's a *correct seam*. If not, that absence is itself the architectural finding.
- Post-mortem asks "what would have prevented this?" After the fix, hand off to `/improve-codebase-architecture` if the answer is structural.

### From `/triage`
- Two category roles (`bug`, `enhancement`) + five state roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`).
- Every comment posted by AI during triage starts with a disclaimer.
- For bugs, **attempt reproduction before grilling**. A confirmed repro makes a much stronger agent brief; failure to repro is a strong `needs-info` signal.
- `wontfix` for enhancements writes a `.out-of-scope/<slug>.md` durable artifact so future triage doesn't re-litigate.

### From `/improve-codebase-architecture`
- Architecture vocabulary: **Module / Interface / Implementation / Depth / Seam / Adapter / Leverage / Locality**.
- **Deletion test**: imagine deleting the module. If complexity vanishes, it was a pass-through; if complexity reappears across N callers, it was earning its keep.
- **The interface is the test surface.**
- **One adapter = hypothetical seam. Two adapters = real seam.** Don't add interfaces speculatively.
- Skill is *informed* by `CONTEXT.md` and ADRs — domain language names good seams; ADRs prevent re-litigating settled decisions.

### From `/prototype`
- A prototype is **throwaway code that answers a question**. The question decides the shape.
- Two branches: **LOGIC** (interactive terminal app for state/business-logic) vs **UI** (multi-variant route with floating switcher).
- Throwaway from day one and clearly marked. No persistence by default. Skip polish. Surface state on every action.
- The *answer* is the only durable output. Capture in commit / ADR / NOTES.md, then delete the prototype.

### From `/grill-with-docs`
- One question at a time, with a recommended answer. If a question can be answered by exploring code, explore instead of asking.
- Challenge user terms against existing `CONTEXT.md` glossary in real time.
- Stress-test relationships with concrete scenarios that probe boundaries.
- ADR criteria — offer an ADR **only when all three** are true: (1) hard to reverse, (2) surprising without context, (3) result of a real trade-off. Otherwise skip.
- `CONTEXT-MAP.md` at root signals a multi-context repo with per-context `CONTEXT.md` and `docs/adr/` directories.

### From `/handoff`
- Compact the current conversation into a handoff doc at `mktemp -t handoff-XXXXXX.md`.
- Don't duplicate content from PRDs / ADRs / issues — reference by path or URL.
- Suggest skills the next session should use.

### From `/zoom-out`
- Tiny prompt: "Go up a layer of abstraction. Give me a map of all relevant modules and callers, using the project's domain glossary vocabulary."
- `disable-model-invocation: true` — user invokes deliberately, not auto-triggered.

### From `/setup-matt-pocock-skills`
- Per-repo scaffold: pluggable issue tracker (GitHub / Linear / local `.scratch/` files), triage label vocabulary mapping, doc directory layout.
- Issue-tracker abstraction means the same skills run on any backend.

## Misc framing

- "These skills are designed to be small, easy to adapt, and composable. They work with any model. Hack around with them. Make them your own."
- Pocock cites: Pragmatic Programmer, DDD, Philosophy of Software Design, Extreme Programming Explained, TDD by Example.

## Update — v1.2.3 (recaptured 2026-09-24)

Now ships as a Claude Code plugin (`/plugin install mattpocock-skills`, official marketplace, auto-updates) **or** as editable copies via `npx skills@latest add mattpocock/skills`. README: "Pick one: installing both leaves you with every skill twice."

**Renames / removals:** `to-prd` → `to-spec`; `to-issues` → `to-tickets`; `diagnose` → `diagnosing-bugs`; `decision-mapping` → `wayfinder`; in-progress `review` → `code-review`; `write-a-skill`/`writing-great-skills` → `writing-for-agents`. `zoom-out` and `caveman` **removed** ("zoom-out went unused in practice"). `grilling` extracted as the shared interview primitive under `grill-me`, `grill-with-docs`, `triage`, `wayfinder`, `improve-codebase-architecture`. New: `implement`, `wayfinder`, `code-review`, `domain-modeling`, `codebase-design`, `research`, `resolving-merge-conflicts`, `wizard`, `handoff`, `ask-matt` (router), `to-questionnaire`, `wait-what`.

**Main flow (from `ask-matt`):** `/grill-with-docs` → (optional `/prototype` detour, bridged by `/handoff`) → multi-session? `/to-spec` → `/to-tickets` → `/implement` per ticket, `/clear` between tickets : `/implement` in place. `/implement` drives `/tdd` at pre-agreed seams, runs typecheck/single tests often and the full suite once, then `/code-review` (Standards + Spec axes, parallel subagents) before committing.
- Keep grill → spec → tickets in **one unbroken context**; each `/implement` starts fresh from its ticket.
- On-ramps: `/triage` for issues *you didn't create* (don't triage `/to-tickets` output — it's agent-ready by construction); `/diagnosing-bugs` for breakage; `/wayfinder` for efforts too big for one session (produces decisions, not deliverables; hands off to `/to-spec`).
- Codebase health: `/improve-codebase-architecture` "whenever you have a spare moment"; a picked candidate becomes an idea that re-enters at `/grill-with-docs`.

**Smart zone:** "~150k tokens on state-of-the-art models" (was ~100k).

**Phase boundaries (`ask-matt/PHASE-BOUNDARIES.md`):** decide only *at* a boundary; mid-phase, continue or split into subagents ("compacting mid-phase makes the agent lose the thread"). Ordered tree, first yes wins: (1) Continue if the next phase needs this one as a primary source or it fits in the remaining smart zone; (2) `/clear` if the context is irrelevant to what's next; (3) `/handoff` only for a new harness, new directory, a colleague, or forking a side task mid-phase; (4) subagent if the task can run AFK (automated review is the standard case); (5) otherwise `/compact <instruction>` — "the default, not the first reach". Every move except Continue turns a primary source into a lossy secondary source.

**`/to-tickets`:** tracer-bullet tickets, each sized for one fresh context window, each declaring **blocking edges**; on a real tracker, publish blockers-first and use native blocking / sub-issue links, label `ready-for-agent`. Work the **frontier** (tickets whose blockers are all done). Wide refactors are the exception to vertical slicing: sequence as **expand → migrate in batches → contract**. No file paths or code snippets in tickets (they go stale), except decision-rich snippets from a prototype.

**`/prototype`:** logic branch is now a single shareable HTML file (free-play + guided walkthroughs) instead of a terminal app. "Throwaway is a constraint on how the code is written, not a promise to destroy it": the prototype is kept on a `prototype/<name>` branch as a primary source, pointed at from the implementation issue.

**`implement-spec` (in-progress, 2026-08) — Pocock's orchestrator pattern.** Tickets are a task graph with a frontier. One branch + draft PR closing the spec and tickets. An optional exploration subagent writes notes to a directory outside the repo that all later subagents read. One implementer subagent per ticket, each in its own worktree and branch, run in the background for maximum concurrency; a **merger subagent** merges each finished branch into the PR branch; when the frontier changes, dispatch more. Communicate sparsely via **context pointers** (spec, tickets, notes, commits), not duplicated content. At the end: one `/code-review`, one fix subagent, mark PR ready, clean up worktrees.
