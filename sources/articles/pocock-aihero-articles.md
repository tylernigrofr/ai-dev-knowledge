---
title: "Matt Pocock — aihero.dev articles (Jan–Mar 2026)"
type: article
url: https://www.aihero.dev
author: Matt Pocock
published: 2026-03-23
captured: 2026-05-06
status: extracted
concepts_seeded:
  - deep-modules
  - vertical-slices
  - doc-rot
  - feedback-loop-ceiling
  - ubiquitous-language
  - three-route-prototype
  - integration-testing-bias
  - just-in-time-docs
  - grilling-alignment
---

# aihero.dev — consolidated extraction

Six Pocock posts read together: *5 Agent Skills I Use Every Day*, *How To Make Codebases AI Agents Love*, *Tracer Bullets: Keeping AI Slop Under Control*, *9 Ways AI Coding Has Rewired My Brain*, *My 'Grill Me' Skill Went Viral*, *Skills Changelog: Ubiquitous Language → /grill-with-docs*.

## Load-bearing claims

### Codebase shape dominates
- "Your codebase, way more than your prompt or your AGENTS.md, is what determines whether AI works well." Codebase > prompt > agent doc.
- Bad codebases cost you in three ways: feedback delay, navigation difficulty, and the developer manually patching AI/codebase mismatches.
- AI is "a new starter with no memory" stepping into your codebase like the guy from Memento. Designing for them = designing for ~20+ daily new starters.

### Grey-box modules and progressive disclosure
- A deep module's interface creates a **natural seam**. Tests lock down behaviour. You *can* look inside (to apply taste, influence outcomes, improve performance) but don't *need* to as long as tests pass.
- Pocock's term: **"grey-box module"**. Not opaque (black-box), not transparent (white-box) — peer-able when needed, hidden by default.
- Codebase becomes "designed for progressive disclosure of complexity": interface at top, implementation only when needed.
- Cognitive load result: maintainer holds 7–8 chunks instead of hundreds of interrelated modules. The AI manages internals.

### AI sycophancy → "outrunning headlights"
- AI's natural inclination is sycophancy — wants to please by producing complete solutions in one leap.
- Concrete failure: asked to build "DB service + API," AI builds all CRUD endpoints, request/response models, error middleware, auth, rate limiting, logging — *then* tries to connect to the DB and the connection string is wrong.
- Pragmatic Programmer term: **"outrunning your headlights"**. Building too much in the dark.
- Fix: tracer bullets / vertical slices. Force the AI to build one tiny end-to-end slice, get feedback, then expand.
- Pocock's prompt insertion: explicit "## Tracer Bullets" section in the Ralph loop or build-feature skill.

### Integration testing for AI
- "Way more time thinking about integration testing." Pocock's CLI tool example: previously manual QA, switched to end-to-end test suite + temporary Git environment utility, ran the entire suite on every AI change.
- "Raising test boundaries lets you catch more bugs and work more comfortably with AI agents running code automatically."
- Pair with grey-box modules: test *at the boundaries*, leave implementation to the AI. The interface becomes the contract.

### Friction is desirable
- Pre-commit hooks, CI, strong types — every AI change should trigger them.
- "The more immediate the feedback, the better decisions the agent can make."
- Friction here = signal density. Strip it and the agent flies blind.

### Doc rot, and the positive prescription
- "Lots of people stuff their repos with markdown docs. Every time the LLM searches for something, it finds docs that might be outdated."
- Outdated docs are worse than missing docs because the LLM can't tell which to trust.
- **Positive prescription**: "Let the AI generate its own docs during the exploration phase instead. Those docs never go out of date because they're just-in-time generated."

### UI prototyping (n=5, not 3)
- "Ask the LLM for five different options for the UI change. Put them on throwaway routes." (Vs. the talk's "three.")
- Iterate on prototypes without touching real code. Once you land on something, AI implements properly.
- Same multimodal-blindness justification as in the talk.

### Effect / DI for grey-box modules (TypeScript)
- Pocock recommends Effect's `services` concept — reusable components that encapsulate common tasks. "Complex, deep modules with simple interfaces."
- Specific to TypeScript backend; not load-bearing for the general principle.

### Bounded contexts in CONTEXT.md
- The deprecated `/ubiquitous-language` skill became `/grill-with-docs` — and now supports **multiple bounded contexts** (DDD pattern).
- Single-context repo: `CONTEXT.md` at root.
- Multi-context repo: `CONTEXT-MAP.md` at root pointing at per-context `CONTEXT.md` files (e.g. `src/ordering/CONTEXT.md`, `src/billing/CONTEXT.md`).
- Per-context `docs/adr/` directories alongside.

### Architecture vocabulary, slightly expanded
From the changelog post — Module / Interface / Implementation framing:
- **Module** is "deliberately scale-agnostic" — applies equally to function, class, package, or tier-spanning slice.
- **Interface** = "everything a caller must know to use the module correctly. Includes type signature, but also invariants, ordering constraints, error modes, required configuration, and performance characteristics." (Performance is explicit here vs. our current concept.)
- **Adapter** distinction: "a thing can be a small adapter with a large implementation (a Postgres repo) or a large adapter with a small implementation (an in-memory fake)."

### Grilling — calibration and framing
- Typical session length: ~45 minutes.
- Historical framing: "Before AI came along, devs called this rubber ducking — talking through your idea until you figured out all the permutations."
- The "provide your recommended answer" line was added late and dramatically sped up sessions — user can just say "yes" instead of explaining everything.
- Two-skill split: `/grill-me` (productivity, general use) and `/grill-with-docs` (engineering, updates `CONTEXT.md` and ADRs inline).

### Meta-programming framing
- "I'm always thinking about how to make my agent run automatically. This means defining my own processes and figuring out what I do."
- Building features is rote (add tests, build, run, commit). The interesting frontier is *everything else*: triaging issues, backlog pruning, task prioritization. Delegate or automate, retain control.

## Misc useful framings

- "Bad code is the most expensive it's ever been." (Site-wide thesis.)
- "AI has no taste for UI. AI has no taste for software architecture." Both must be supplied by the human.
- Skill quality is not length. The grill-me skill is three sentences and is Pocock's most impactful.
