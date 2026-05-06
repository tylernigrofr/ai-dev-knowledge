---
title: "The Unreasonable Effectiveness of an LLM Agent Loop with Tool Use — Philip Zeyliger @ sketch.dev"
type: article
url: https://sketch.dev/blog/agent-loop
author: Philip Zeyliger
published: 2025-05-15
captured: 2026-05-06
status: extracted
concepts_seeded:
  - agent-loop-simplicity
  - feedback-loop-ceiling
  - ralph-loop
---

# The Unreasonable Effectiveness of an LLM Agent Loop with Tool Use

Short post from a co-creator of the Sketch AI programming assistant. The central surprise: the core agent loop is shockingly simple (~9 lines), and a single general-purpose tool (bash) covers a wide range of real tasks.

## Load-bearing claims

### The 9-line loop
The entire architecture is a tight while-loop: call LLM → print output → if tool calls, handle them and feed results back; else, get next user input. "There's some pomp and circumstance to make the above work ... but the core idea is the above 9 lines."

```python
def loop(llm):
    msg = user_input()
    while True:
        output, tool_calls = llm(msg)
        print("Agent: ", output)
        if tool_calls:
            msg = [ handle_tool_call(tc) for tc in tool_calls ]
        else:
            msg = user_input()
```

The `llm()` function sends the system prompt, conversation history, and next message to the API. That's all. The loop is the architecture.

### Bash as the universal tool
With just `bash`, Claude 3.7 Sonnet can "nail many problems, some of them in one shot." Replaces: esoteric git lookups, manual merge resolution, type-checker error triage. The agent adapts: installs missing deps, adjusts to different command-line options, handles conditionals.

### Tool minimalism then specialization
Bash is the starting point. Sketch added more specialized tools and found they "improve the quality, speed up iterations, and facilitate better developer workflows." Tools that let the LLM edit text correctly are "surprisingly tricky" — the LLM struggling with `sed` one-liners reaffirms why visual editors exist.

### The shortcutting failure mode
Agents can be "infuriating" — "Oh, this test doesn't pass... let's just skip it." Persistent loops with weak feedback (no failing-test signal that halts progress) create a shortcut path where the agent removes the obstacle rather than fixing it.

### The future: custom throw-away loops
Prediction: "more custom, ad hoc, throw-away LLM agent loops in our `bin/` directories." The gap between general-purpose tools and brittle custom automation will be filled by bespoke agent loops for specific workflows. Correlating stack traces with git commits is the worked example.

## Contested / caveats

- The article uses Claude 3.7 Sonnet (2025-era). The "one bash tool is enough" claim may shift as tasks grow more complex.
- The post is written from a SaaS product builder's perspective (Sketch). The simplicity claim applies to the *core loop*, not to production hardening (auth, cost limits, safety rails, etc.).
- Zeyliger doesn't address multi-agent or parallel patterns — this is single-threaded interactive agent use.
