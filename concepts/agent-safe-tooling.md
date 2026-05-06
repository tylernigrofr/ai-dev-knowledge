---
title: Agent-safe tooling (friendly errors, idempotency, always-on logs)
type: principle
phase: [implementation]
tags: [tooling, observability, dx, error-handling, agents]
sources:
  - sources/articles/ronacher-agentic-coding-2025.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Dev tools that agents invoke (CLIs, Makefiles, dev servers, build scripts) must be designed for autonomous operation: errors that explain what to do next, protection against incorrect invocation, and persistent logs agents can read without human help.

## Why it matters
Agents are not humans. They cannot ask "why is this hanging?", google an error, or intuit that a process was already running. A tool that a human debugs in 30 seconds can trap an agent indefinitely. The investment in agent-proofing tooling directly determines how far agents run before needing a human to unstick them — which is the entire point of AFK delegation.

## How to apply

### Friendly errors
- Every failure should say: what went wrong, what state the tool is in, and what to try next.
- Don't pass raw OS errors through unmodified. `ECONNREFUSED` is less useful to an agent than `"Could not connect to dev server — is 'make dev' running?"`.
- Validate arguments at the tool boundary; reject invalid inputs with explanatory text before doing any work.

### Idempotency and chaos-monkey protection
- Assume the agent will call the tool wrong: bad args, wrong order, twice in parallel.
- Guard against double-spawn — check whether the process is already running before starting.
- Prefer idempotent operations; document which operations are not.
- **Time out rather than hang.** A timeout + error is always better than indefinite blocking. Hangs burn context silently; crashes at least produce text.

### Always-on logging
- Write all output to files, even in dev/local mode. Agents can `cat` a log file; they cannot inspect a daemon that ran and exited.
- Include enough context to reconstruct events: timestamps, inputs, outputs, error codes.
- For auth and verification flows: log tokens, links, or codes to stdout/files in debug mode so agents can complete multi-step flows (e.g., email verification) without human handoff.

### Reference implementation pattern
Ronacher: Makefile-based dev setup + process manager that guards double-spawn, captures all output to rotating logs, and exits non-zero with an explanation on failure. Agents can invoke `make dev`, inspect logs if something fails, and make progress without interruption.

## Caveats
- Logging verification links or auth tokens in debug mode is a security surface. Always gate behind an explicit env flag (`DEBUG=true`) that is **off** in production and CI.
- Over-engineering validation can obscure real errors behind a wall of custom messages. The goal is clarity, not a defensive fortress.
- This applies to the tools agents run, not the tool *descriptions* agents read. For the latter, see [aci-tool-design](aci-tool-design.md).

## Related
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — tool quality determines signal quality; hangs are fatal
- [ralph-loop](ralph-loop.md) — AFK loops depend on tool reliability
- [tdd-for-afk](tdd-for-afk.md) — tests are tools; same design principles apply
- [aci-tool-design](aci-tool-design.md) — the complementary concern: tool *descriptions* and interface design for agent reasoning
