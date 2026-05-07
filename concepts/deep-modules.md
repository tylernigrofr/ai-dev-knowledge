---
title: Deep modules over shallow modules
type: principle
phase: [planning, implementation]
tags: [architecture, ousterhout, testability, module-design, vocabulary]
sources:
  - sources/youtube/pocock-vibe-engineering-2025.md
  - sources/repos/pocock-skills.md
  - sources/articles/pocock-aihero-articles.md
  - sources/articles/gemini-ousterhout-for-ai.md
status: stable
superseded_by: null
last_reviewed: 2026-05-07
referenced_by:
  - concept:define-errors-out-of-existence
  - concept:dependency-categories
  - concept:design-interfaces-delegate-implementation
  - concept:design-it-twice
  - concept:diagnose-loop
  - concept:feedback-loop-ceiling
  - concept:integration-testing-bias
  - concept:mock-at-boundaries
  - concept:pre-ai-fundamentals
  - concept:strategic-programming
  - concept:systems-thinking-three-questions
  - concept:ubiquitous-language
audience: [implementer, reviewer]
activate_when: "Designing or refactoring module boundaries."
cluster: decomposition
---

## Summary
Prefer deep modules (small interface, lots of functionality inside) over shallow modules (interface nearly as complex as the implementation); deep modules give you leverage at the call site, locality for maintenance, and a real test surface — and agents accelerate software entropy, so caring about depth is now a daily, not occasional, practice.

## Why it matters
From Ousterhout's *A Philosophy of Software Design*. Shallow modules force you into mocking hell or testing nothing meaningful — and AI agents amplify the cost because they reason worse about scattered, tightly-coupled code. Deep modules give you a stable interface to test against, a small surface for the AI to reason about, and the ability to refactor internals without consumer changes. Pocock's framing: agents radically speed up coding *and* radically speed up entropy, so "invest in design every day" (Beck) is now operational, not aspirational.

**Ousterhout's roots.** Complexity comes from two architectural flaws: **dependencies** (code that can't be understood or modified in isolation) and **obscurity** (information that is hidden, unintuitive, or poorly named). Deep modules attack both — a narrow interface is a dependency-reduction tool, and rich-but-hidden internals only stay hidden if the interface names what they do. The need for sprawling external documentation is itself a red flag that the design is obscure.

**Codebase shape dominates prompt and agent doc.** Pocock's claim is that your codebase determines AI quality more than any prompt or `AGENTS.md`/`CLAUDE.md`. Three failure modes when shape is wrong: feedback delay (AI doesn't know if its change worked), navigation friction (AI can't find files or work out how to test), and manual patching (you end up holding AI and codebase together). With the right shape, your maintainer cognitive load drops to ~7–8 chunks instead of hundreds of interrelated modules — the AI manages internals, you manage interfaces.

**Grey-box modules.** A deep module's interface is a natural seam where tests can lock down behaviour. You *can* peer inside (to apply taste, influence outcomes, improve perf) but don't *need* to as long as tests pass. Not black-box (opaque) and not white-box (transparent) — peer-able when needed, hidden by default. The whole codebase becomes "designed for progressive disclosure of complexity": interface at top, implementation only when needed.

## Architecture vocabulary

Use these terms exactly. Drift to "component / service / boundary" loses the precision.

- **Module** — anything with an interface and an implementation (function, class, package, slice). **Deliberately scale-agnostic** — applies equally to a function and to a tier-spanning slice.
- **Interface** — *everything a caller must know to use the module*: types, invariants, error modes, ordering, config, **and performance characteristics**. Not just the type signature.
- **Implementation** — the code inside.
- **Depth** — leverage at the interface; lots of behaviour behind a small interface. Deep = high leverage. Shallow = interface nearly as complex as the implementation.
- **Seam** — where an interface lives; a place behaviour can be altered without editing in place. (Use this, not "boundary.")
- **Adapter** — a concrete thing satisfying an interface at a seam. The size of the adapter and the size of its implementation are independent: a small adapter can have a large implementation (Postgres repo) and a large adapter can have a small implementation (in-memory fake).
- **Leverage** — what callers get from depth.
- **Locality** — what maintainers get from depth: change, bugs, knowledge concentrated in one place.

## How to apply

- For each cluster of related code, identify the smallest reasonable public interface and hide everything else.
- **Deletion test** — imagine deleting the module. If complexity vanishes, it was a pass-through. If complexity reappears across N callers, it was earning its keep. A "concentrates" answer is the signal you want.
- **The interface is the test surface.** Tests against pure-function extractions that the real bugs bypass are a smell. If extracted helpers are testable but the calling chain isn't, you have locality without leverage.
- **One adapter = hypothetical seam. Two adapters = real seam.** Don't add interfaces speculatively — wait for a second concrete implementation before declaring a seam exists.
- Design interfaces yourself; delegate implementation (see [design-interfaces-delegate-implementation](design-interfaces-delegate-implementation.md)). This keeps your mental map intact.
- Run `/improve-codebase-architecture` periodically (Pocock recommends every few days) to surface deepening opportunities. The skill is informed by `CONTEXT.md` (names) and ADRs (decisions not to re-litigate).
- Maintain a canonical interface doc (e.g. `MODULES.md` or a section of `CONTEXT.md`) and treat divergence as a bug.

## Skills are deep modules

Agent **skills** are the canonical deep-module pattern for agentic action. A skill directory has two layers, and the split is exactly the deep/shallow distinction:

- **Discovery layer** — a tiny `SKILL.md` (name + one-paragraph "when to invoke"). This is the *only* thing in the agent's active context. It is the interface.
- **Execution layer** — detailed reasoning steps, scripts, helpers, fixtures. Loaded on trigger, never paid for in tokens until needed.

The anti-pattern is **toolitis**: dozens of shallow atomic endpoints (`get_user`, `update_record`, `fetch_balance`) all in the system prompt. The agent burns context just deciding which to call, KV-cache shreds, and hallucination risk multiplies. A small suite of deep skills replaces a wide menu of shallow tools.

## Caveats
- "Deep" is not "huge." A 5000-line file is rarely a good module. The metric is interface narrowness vs. internal richness, not raw size.
- Forced consolidation across genuinely independent concerns creates worse coupling than the shallow case it replaces.
- The deletion test can be misleading for true facade modules whose value is *only* the unified API. Use judgment.

## Related
- [ubiquitous-language](ubiquitous-language.md) — what module names should match
- [push-vs-pull-context](push-vs-pull-context.md) — module map is canonical push content
- [design-interfaces-delegate-implementation](design-interfaces-delegate-implementation.md) — operational counterpart
- [diagnose-loop](diagnose-loop.md) — where missing seams surface as findings
- [pre-ai-fundamentals](pre-ai-fundamentals.md) — Ousterhout, Beck, Fowler reading list
- [strategic-programming](strategic-programming.md) — the daily investment that produces deep modules
- [define-errors-out-of-existence](define-errors-out-of-existence.md) — Ousterhout's information-hiding mandate applied to error paths
