---
title: Define errors out of existence
type: principle
phase: [planning, implementation]
tags: [ousterhout, error-handling, harness, constraints, agents]
sources:
  - sources/articles/gemini-ousterhout-for-ai.md
  - sources/articles/ronacher-agentic-coding-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-05-07
referenced_by:
  - concept:deep-modules
audience: [implementer]
activate_when: "Designing error handling or harness behavior."
cluster: decomposition
---

## Summary
The best way to handle an error is to architect the system so the error condition is no longer exceptional — absorb it inside the module instead of pushing branching, defensive code onto every caller (and onto the agent's context window).

## Why it matters
Ousterhout identifies exception handling as one of the largest sources of complexity in software: every thrown exception multiplies into branching defensive logic at every call site. For human callers this is cognitive load; for LLM agents it is worse — every error path the agent has to reason about steals tokens from actual reasoning, and probabilistic models generate plausible-but-wrong handling for edge cases they only half-understand.

In agentic systems the principle scales up into the harness itself. The harness's job is to make the agent appear to have written flawless code on the first attempt — by absorbing all the intermediate failures internally rather than exposing them to the human reviewer. The same Ousterhout principle, applied at a different layer.

## How to apply

**At the module level (Ousterhout's original framing):**
- Before adding a new exception, ask whether the operation can be redefined so the "error" becomes a normal return value (e.g. "delete a missing file" succeeds silently instead of throwing).
- Internalise edge cases. If the common-case caller never wants to think about the edge, the module should swallow it.
- Treat a proliferation of try/catch at call sites as a smell pointing back at the module's interface, not at the callers.

**At the agent-harness level (the SE 3.0 extension):**
- **Feedforward guides** — restrict the solution space *before* the agent acts: type systems, architectural linters, MCP allowlists, sandbox capability limits. Whole classes of invalid actions become structurally impossible.
- **Feedback sensors** — sandboxed compile/test/lint runs that catch the agent's mistakes and feed the formatted error back as a new prompt. The agent self-corrects autonomously; the human sees only the converged result.
- **Plan-Execute-Verify loop** — wrap the agent in a continuous PEV cycle so transient hallucinations and syntax errors are resolved internally, not surfaced.
- **Constitutional constraints in skills** — for any computation the agent must not invent (compliance scores, audit signatures, payment math), put the calculation in a deterministic script the skill executes, and forbid the agent from recomputing it in its output. The error condition "model hallucinates the number" is defined out of existence by removing the model from that path.

## Caveats
- Don't confuse this with "swallow errors silently." The point is to redesign so the condition isn't an error — not to hide a real failure. A `delete()` that "succeeds" on a permission failure is wrong; one that succeeds on "file already missing" is right.
- Defining errors out of existence at the harness level can mask agent failures from the developer. Keep the underlying traces inspectable (always-on logs from [agent-safe-tooling](agent-safe-tooling.md)) so you can diagnose when the harness is hiding a structural bug rather than a transient one.
- The line between "absorb in module" and "leak abstraction" is judgement. If absorbing the edge case forces the module to make a decision the caller actually cared about, surface it.

## Related
- [deep-modules](deep-modules.md) — same principle: hide complexity, simplify the interface
- [agent-safe-tooling](agent-safe-tooling.md) — the operational counterpart for the tools agents call (friendly errors, idempotency, logs)
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — feedback sensors only work if the underlying signal is fast and reliable
- [aci-tool-design](aci-tool-design.md) — poka-yoke argument shapes are this principle applied to tool inputs
- [strategic-programming](strategic-programming.md) — investing in error redesign instead of adding another try/catch
