---
title: Code-first automation over MCP tool calls
type: principle
phase: [implementation, decomposition]
tags: [mcp, tool-use, automation, composability, inference-cost, verification]
sources:
  - sources/articles/ronacher-tools-code-is-all-you-need.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
When an LLM needs to automate a repeatable task, generating and executing code beats invoking MCP tool calls: code composes deterministically, runs on N inputs without N inferences, and lets humans verify the approach rather than just the outcome.

## Why it matters
MCP tool calls require inference on every invocation — schema loading, decision-making, response parsing. For any task that runs more than once, this compounds into significant context burn and latency. More importantly, MCP composability is inference-dependent: the LLM has to reason about what to call next. Code composes statically. A shell script, a Python transform, or an AST-based converter runs identically on file 1 and file 1000 without additional inference. The inference budget scales with *iterations* (how many refinement rounds you need), not *volume* (how many items you process).

The trust gap is equally important. When an LLM calls MCP tools, you can accept or reject the final output. When it generates a script, you can read, step through, fix, and re-run the approach itself. Ronacher's blog migration succeeded because "I actually trusted this process...because I could review the approach" — three readable scripts that could be debugged, not a black-box sequence of tool calls.

## How to apply
- For any agentic task that will run on many inputs (batch transforms, migrations, bulk analysis), ask the LLM to write a script rather than call tools directly.
- Structure the script in stages: (1) transform/execute, (2) validate/diff, (3) analyze anomalies. This maps neatly to iterative refinement without re-running the full batch each time.
- **Separate execution from judgment.** Let the code run in bulk first. Bring the LLM back for the editorial pass — reviewing diffs, deciding what anomalies matter, tuning the next iteration — not for every individual file.
- Use MCP/tool calls for *exploration of unknown interfaces* (Playwright for a site you're first mapping, `gh` for one-off interactive tasks). Switch to generated scripts once the interface is known and the task is repeatable.
- Make generated scripts human-debuggable: readable variable names, logged intermediates, explicit error handling. You will need to step through them when they fail.
- Prefer CLI tools (`gh`, `jq`, `curl`) over their MCP equivalents for scripted tasks — same capability, lower context overhead, easier to compose in shell pipelines.

## Caveats
- MCP is still appropriate for genuinely interactive, one-shot tasks where the LLM needs to probe an unknown API and the output won't be reused. The cost/benefit flips when the task recurs.
- This is a contested framing in the wider community. MCP advocates argue that well-designed servers abstract complexity the LLM shouldn't need to handle. Ronacher's position assumes the LLM can write correct code — which is increasingly true but not universal for complex domains.
- "Code-first" doesn't mean "no tools." Tool calls to kick off a script (run a subprocess, write a file) are fine; what to avoid is using tool calls as the *execution mechanism* for things code could handle directly.

## Related
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — generated scripts produce faster, more debuggable feedback than tool-call chains
- [vertical-slices](vertical-slices.md) — same "get feedback first" discipline applied to feature decomposition
- [design-interfaces-delegate-implementation](design-interfaces-delegate-implementation.md) — related delegation philosophy: own the design, let code execute
