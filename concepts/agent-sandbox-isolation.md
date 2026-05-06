---
title: Agent sandbox and environment isolation
type: principle
phase: [implementation]
tags: [safety, sandboxing, prompt-injection, credentials, infrastructure]
sources: [sources/articles/willison-designing-agentic-loops.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Run agents in isolated environments — local containers or throwaway cloud infra — so that mistakes and prompt-injection exploits are bounded to infrastructure you can blow away.

## Why it matters
Agents execute tools in a loop with minimal human oversight. A compromised or confused agent can delete files, exfiltrate secrets, or run commands on production systems. Isolation doesn't make agents smarter — it caps the blast radius of the mistakes they inevitably make. This is a prerequisite for AFK delegation, not an afterthought.

## How to apply
Three viable stances, in order of safety:
1. **External cloud infra** (preferred) — run agents in GitHub Codespaces, ChatGPT Code Interpreter, or similar. Mistakes are bounded to a throwaway environment; reset is cheap.
2. **Local container sandbox** — Docker or Apple's container tool. Protects the host machine; adds some friction.
3. **Unsandboxed with disciplined review** — acceptable only for low-stakes local work with a human in the loop. Not suitable for AFK night-shift runs.

Additional hygiene:
- Point agents at test/staging environments, not production.
- Set spending limits on any API key the agent can use.
- Create isolated org accounts for experimental agent work — separate from credentials that touch real user data.

## Caveats
- External infra adds latency and egress cost. For fast iteration loops, a local container may be preferable.
- No sandbox fully protects against a sufficiently sophisticated prompt injection that exfiltrates data through allowed network calls. Assume some residual risk.
- "Unsandboxed + catch mistakes" is workable for personal projects; do not generalize to team or production contexts.

## Related
- [afk-vs-hitl](afk-vs-hitl.md) — sandboxed environments are what make AFK delegation safe
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — isolation should not slow the feedback loop
- [ralph-loop](ralph-loop.md) — the loop that benefits from safe isolation
