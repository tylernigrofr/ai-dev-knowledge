---
title: "mattpocock/skills — Skills For Real Engineers"
type: repo
url: https://github.com/mattpocock/skills
author: Matt Pocock
published: 2026-01-01
captured: 2026-05-06
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
