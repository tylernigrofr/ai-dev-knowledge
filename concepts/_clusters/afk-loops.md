---
name: afk-loops
description: Running agents unattended — the loop, the tests that keep it honest, and the failure modes that compound.
type: cluster
members:
  - ralph-loop
  - tdd-for-afk
  - agent-loop-simplicity
  - error-compounding-in-agents
  - afk-vs-hitl
  - orchestrator-worker-dispatch
  - agent-sandbox-isolation
  - agent-brief-format
  - triage-state-machine
last_reviewed: 2026-09-24
---

## Seam

The shared concern: the agent runs without a human in the smart zone, so every safeguard has to be *structural*. These concepts describe the loop itself (Ralph, 9-line core), the test discipline that keeps it from cheating (TDD-for-AFK), the failure mode it must survive (error compounding), and the guardrails that contain blast radius (sandboxing, AFK tagging, parallel sand-castle worktrees).

## Members

- **ralph-loop** — the canonical AFK implementation pattern.
- **tdd-for-afk** — non-negotiable: tests are the only ground truth when you're not watching.
- **agent-loop-simplicity** — keep the orchestration core tiny; complexity belongs in tools, not the loop.
- **error-compounding-in-agents** — small per-step error rates explode over long stateful runs; design for it.
- **afk-vs-hitl** — explicit tagging so a human knows which issues can be handed to an unattended agent.
- **orchestrator-worker-dispatch** — one orchestrator drains the issue graph with parallel worktree workers and a scripted merge gate (supersedes sand-castle-parallelization).
- **agent-sandbox-isolation** — credentials, network, FS isolation so a runaway loop can't exfiltrate or destroy.
- **agent-brief-format** — When an issue moves to `ready-for-agent`, post a structured comment — the *agent brief* — that becomes the contract the AFK agent works from.
- **triage-state-machine** — Run every incoming issue through a small canonical state machine — two category roles (`bug`, `enhancement`) and five state roles (`needs-tr.
