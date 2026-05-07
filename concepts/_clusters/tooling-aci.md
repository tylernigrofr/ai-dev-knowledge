---
name: tooling-aci
description: The agent-computer interface — tool descriptions, error messages, and code-first patterns that decide what the agent can actually do.
type: cluster
members:
  - aci-tool-design
  - tool-design-for-agents
  - agent-safe-tooling
  - define-errors-out-of-existence
  - code-first-automation
  - generate-over-depend
  - own-your-planning-stack
last_reviewed: 2026-05-07
---

## Seam

The shared concern: an agent's capability ceiling is set by its tools, not its model. These concepts cover **how to design that surface** — clear tool descriptions and poka-yoke (ACI), friendly errors and idempotency (agent-safe tooling), eliminating error states by design (Ousterhout), preferring code over MCP roundtrips, generating glue over depending on it, and owning the planning stack rather than outsourcing to a framework.

## Members

- **aci-tool-design** — agent-computer interface as a first-class design surface; poka-yoke and clear docs.
- **tool-design-for-agents** — tools shape capability; budget design effort proportionally.
- **agent-safe-tooling** — friendly errors, idempotency, always-on logs so agents can self-correct.
- **define-errors-out-of-existence** — Ousterhout move: redesign so the error condition can't occur.
- **code-first-automation** — prefer scripted automation over chains of MCP tool calls when verifiable.
- **generate-over-depend** — generate glue/SDKs over taking a fast-moving dependency the agent must track.
- **own-your-planning-stack** — keep the orchestration layer in your repo; don't hide it behind a framework.
