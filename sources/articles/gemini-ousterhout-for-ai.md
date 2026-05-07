---
title: "Software Design in the Agentic Era: Applying Ousterhout's Philosophy to AI-Driven Development"
type: article
url: null
author: "Gemini Deep Research (user-commissioned synthesis)"
published: 2026-05-07
captured: 2026-05-07
status: extracted
concepts_seeded:
  - strategic-programming
  - define-errors-out-of-existence
  - deep-modules
  - compacting-vs-clearing
  - aci-tool-design
---

## What this is

A Gemini Deep Research report commissioned by the KB owner (Tyler) that synthesizes John Ousterhout's *A Philosophy of Software Design* (APoSD) and maps each principle directly onto Agentic Software Engineering (SE 3.0). Cites ~74 secondary sources (Pragmatic Engineer, Matt Pocock, Anthropic engineering blog, Martin Fowler, LangChain, Ousterhout's own materials, plus a long tail of 2025–2026 "harness engineering" posts).

Captured as a single document because the value is the synthesis, not any individual cited link — most of those are already represented elsewhere in the KB (Pocock, Anthropic context-engineering, building-effective-agents, multi-agent research, Ronacher) or are derivative blog summaries of APoSD.

## Spine of the argument

1. **Complexity is the core problem.** Ousterhout: complexity = anything making a system hard to understand and modify. Symptoms: change amplification, cognitive load, unknown unknowns. Root causes: dependencies + obscurity. Complexity is incremental — it accumulates through hundreds of tactical compromises, never one bad decision.

2. **Strategic vs tactical programming.** Tactical = "make it work, refactor later." The "tactical tornado" ships fast and leaves wreckage. Strategic = invest 10–20% of every task in design (alternatives, naming, dependency reduction). Ousterhout argues Agile and TDD push toward tactical thinking. (Controversial — KB already has [tdd-for-afk](../../concepts/tdd-for-afk.md) which adopts a different stance.)

3. **Deep modules over shallow.** Module = rectangle: width = interface complexity, height = hidden implementation. Deep = narrow interface / rich internals (Unix file I/O: 5 calls hide disk sectors, locking, caching). Shallow = interface ≈ implementation. Direct rebuttal of Robert C. Martin's *Clean Code* "One Thing Rule" → "classitis" disease.

4. **Information hiding + define errors out of existence.** Don't propagate exceptional conditions to callers; absorb them in the module. Exception handling is one of the largest sources of complexity.

5. **The mapping to LLM agents is exact.**
   - Cognitive load ↔ context window / attention budget / "Lost in the Middle".
   - Obscurity / unknown unknowns ↔ tribal knowledge not in `AGENTS.md` or discoverable by tools → hallucination.
   - Classitis ↔ heavily fragmented codebases force agents into dozens of file reads, exhausting tool/token budget on boilerplate.

6. **Strategic prompting.** System prompt = agent's constitution = invariant policy. Procedural how-to belongs in dynamically-loaded skills, not the system prompt (separating general-purpose from special-purpose code).

7. **Harness engineering = "pull complexity downwards" applied to LLMs.** Five pillars:
   - **Progressive disclosure** — small `AGENTS.md` map; deep docs loaded on demand.
   - **Filesystem as working memory** — externalize state to `progress.md`, reset context, resume from condensed summary.
   - **Define errors out of existence** — feedforward guides (architectural linters, MCP access controls, type systems) restrict the solution space; feedback sensors (sandboxed compile/test loops) force self-correction. Together: a Plan-Execute-Verify loop that masks all intermediate exceptions before they reach the human.
   - **Entropy management** — scheduled cleanup sub-agents enforce conventions, sync drifted docs.
   - **Multi-agent orchestration with context isolation** — orchestrator-worker; sub-agents never share context windows; all synthesis routes through the orchestrator.

8. **Skills = deep modules for agentic action.**
   - Anti-pattern: "toolitis" — dozens of shallow atomic endpoints (`get_user`, `update_record`) blow up KV-cache, induce decision paralysis, multiply hallucination risk.
   - Pattern: skill directory with two layers — (a) lightweight `SKILL.md` metadata (the *interface*, only thing in active context — name + when-to-invoke), (b) execution layer (detailed reasoning steps + executable scripts) loaded only on trigger.
   - **Prefer general-purpose tools** — a sandboxed bash/python execution environment is the deepest possible tool: interface is "execute string"; functionality is Turing-complete. Beats hardcoding 50 specialized endpoints.
   - **Constitutional constraints** — deterministic rules embedded in the skill's executable layer that the LLM cannot override (e.g. compliance score must be computed by a bash script; LLM is forbidden from recalculating). Information hiding enforces structural reliability against people-pleasing drift.

## Insights worth distilling

| # | Insight | Distillation route |
|---|---------|---------------------|
| 1 | Strategic vs tactical programming + tactical tornado + 10–20% design investment | **Create** `strategic-programming` |
| 2 | Define errors out of existence (Ousterhout principle, mapped to harness PEV loops + constitutional constraints) | **Create** `define-errors-out-of-existence` |
| 3 | Ousterhout roots of deep modules: dependencies + obscurity; skill = deep module with two-layer SKILL.md pattern | **Refine** `deep-modules` |
| 4 | Filesystem as agent working memory (progress.md, intercept-summarize-reset pattern) | **Refine** `compacting-vs-clearing` |
| 5 | Prefer one general-purpose deep tool (bash sandbox) over fat menus of shallow specialized endpoints — "toolitis" | **Refine** `aci-tool-design` |
| 6 | LLM context window = cognitive load = working memory; "Lost in the Middle" | **Reject** — duplicate of [smart-zone-vs-dumb-zone](../../concepts/smart-zone-vs-dumb-zone.md) |
| 7 | Critique of Clean Code / classitis hostile to AI navigability | **Reject** — already covered in [deep-modules](../../concepts/deep-modules.md) |
| 8 | System prompt as constitution; policy not procedure | Rejected for now — overlaps with [own-your-planning-stack](../../concepts/own-your-planning-stack.md) and skills pattern; revisit if it surfaces again |
| 9 | Multi-agent orchestrator-worker with strict context isolation | **Reject** — covered in [subagents-as-delegation](../../concepts/subagents-as-delegation.md) and [clean-context-reviewer](../../concepts/clean-context-reviewer.md) |

## Caveats on the source

- It's a Gemini-authored synthesis, not a first-party text. Treat APoSD claims as authoritative; treat the agentic-mapping claims as well-sourced commentary (Pragmatic Engineer, Anthropic, Martin Fowler are the load-bearing citations there).
- Some cited URLs date to 2026 and may not all be stable. The KB depends on the *ideas*, not the link integrity.
- The author leans heavily on the "harness engineering" framing popular in 2026. That framing is consistent with Anthropic's own [equipping-agents-with-skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) and Pocock's writing — so it's not idiosyncratic.
- Ousterhout's hostility to TDD is genuinely contested; KB takes a more nuanced position (TDD-for-AFK is useful as an agent oracle, even if it can encourage tactical thinking in a human-only setting).
