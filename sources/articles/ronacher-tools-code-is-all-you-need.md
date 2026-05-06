---
title: "Tools: Code Is All You Need"
type: article
url: https://lucumr.pocoo.org/2025/7/3/tools/
author: Armin Ronacher
published: 2025-07-03
captured: 2026-05-06
status: extracted
concepts_seeded:
  - code-first-automation
---

# Tools: Code Is All You Need — Armin Ronacher (July 2025)

Ronacher argues that LLM-generated code beats MCP tool calls for agentic automation, using a real blog migration project as the primary example.

## Load-bearing claims

### 1. MCP is not truly composable
MCP relies on inference to compose tool calls at runtime — the LLM has to reason about what to call next. Code composes deterministically. Ronacher's position: "code generation just is the better choice because of the ability to compose," even for non-programming specialized tasks.

### 2. MCP demands too much context
Comparative test: completing GitHub tasks with the `gh` CLI tool consumed context far more efficiently than using GitHub's MCP implementation. Each MCP tool call burns context for schema loading, response parsing, and decision-making that a shell script handles in one line.

### 3. Inference costs should scale with iterations, not volume
Once a script is written, it runs on N files with zero additional inference. MCP requires inference per tool invocation. Ronacher's blog conversion: three scripts ran across hundreds of RST files; only the iterative refinement required inference — not the bulk execution.

### 4. Code generation enables reviewing the approach, not just the output
The blog conversion used three scripts: (1) parse RST → AST → Markdown, (2) compare old and new HTML, (3) analyze differences for refinement. Trust came from being able to review and debug the scripts themselves, not just accept or reject their outputs. "I actually trusted this process...because I could review the approach."

### 5. Separation of execution from judgment
Better agentic automation: generate code that runs in bulk first, then apply LLM judgment to the results afterward. Don't mix per-operation inference with per-operation execution. This lets the LLM's role be editorial rather than operational on every step.

### 6. Human-debuggable scripts beat inference-dependent tool calls
"I'm a human, not an MCP client. I can run and debug a script, I cannot even figure out how to reliably do MCP calls." The human can step through, fix, and re-run generated code. MCP calls are opaque invocations.

## Misc framings

- Playwright-via-MCP is acceptable for exploring *unknown* interfaces; explicit scripts are better for *known* environments you'll run repeatedly.
- The vision: "LLMs can do so much more if you give them the power to write code."
- Future direction: better sandboxes and API abstractions for bulk code execution, with LLM judgment applied afterward.
