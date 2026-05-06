---
title: "Designing Agentic Loops — Simon Willison"
type: article
url: https://simonwillison.net/2025/Sep/30/designing-agentic-loops/
author: Simon Willison
published: 2025-09-30
captured: 2026-05-06
status: extracted
concepts_seeded:
  - afk-vs-hitl
  - feedback-loop-ceiling
  - agent-sandbox-isolation
---

# Designing Agentic Loops — Simon Willison

Published: 2025-09-30. Willison's working definition: an LLM agent is "something that runs tools in a loop to achieve a goal." The article covers safety, tool selection, credential hygiene, and which problems are worth delegating.

## Load-bearing claims

### 1. Agent definition: tools + loop
An agent = LLM running tools in a loop toward a goal. The key design levers are: (a) which tools are exposed, (b) how the loop is structured, and (c) what the success condition is.

### 2. Sandbox/isolation as the primary safety lever
Agents can execute harmful commands or fall victim to prompt injection. Three viable stances:
- **Sandbox locally** — Docker or Apple's container tool isolates the agent from the host.
- **Delegate to external infrastructure** — GitHub Codespaces, ChatGPT Code Interpreter. Damage is bounded to a throwaway cloud environment.
- **Run unsandboxed and catch mistakes** — least safe; acceptable only with disciplined review.

Willison's preference: external systems (Codespaces) where mistakes are cheap to blow away, over local sandboxes which add friction.

### 3. Tool selection: prefer shell + AGENTS.md over heavy MCP
Modern LLMs already know tools like Playwright, FFmpeg, and most Unix utilities. Rather than wiring up complex MCP integrations, expose shell access and drop an `AGENTS.md` file that documents available tools and conventions. Simpler integration surface = less failure surface.

### 4. Credential and environment hygiene
- Use test/staging environments over production.
- Set spending limits on any API key that can incur costs.
- Create isolated organizational accounts for experimental agent work.
These are operational safety nets that don't depend on agent capability.

### 5. Task-selection heuristic: variation-heavy problems
Agentic loops are best suited to problems with:
- Clear success metrics (automated tests, benchmarks, measurable outcomes).
- Iterative trial-and-error character — the agent needs to try many variations.
- Strong automated test suites to provide feedback.

Willison's signal phrase: **"Ugh, I'm going to have to try a lot of variations here."** That feeling = readiness for agentic delegation. Examples: debugging, performance optimization, dependency upgrades, container optimization.

### 6. Automated tests as the force multiplier
A strong test suite doesn't just catch bugs — it creates the feedback loop the agent uses to improve. Without it, the agent iterates blind. This reinforces that investing in tests is investing in agent leverage, not just software quality.

## Contested / nuanced points
- "Unsandboxed + catch mistakes" is presented as viable. This conflicts with a risk-averse stance and should be read as context-dependent (low-stakes local projects, not production work).
- AGENTS.md approach vs. MCP: Willison is pragmatist / minimalist; others (e.g., Pocock) lean harder into structured skill files. Both are compatible; this is a tooling preference, not a contradiction.
