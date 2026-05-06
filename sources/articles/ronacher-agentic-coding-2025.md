---
title: "Agentic Coding Recommendations — Armin Ronacher"
type: article
url: https://lucumr.pocoo.org/2025/6/12/agentic-coding/
author: Armin Ronacher
published: 2025-06-12
captured: 2026-05-06
status: extracted
concepts_seeded:
  - feedback-loop-ceiling
  - agent-safe-tooling
  - generate-over-depend
---

# Agentic Coding Recommendations — Armin Ronacher

Armin Ronacher (creator of Flask, Rye, uv-adjacent tooling) shares his June 2025 agentic workflow. Uses Claude Code + Sonnet on a $100/month Max plan, full-permission mode, minimal interruptions. Explicitly flags the post may "age very poorly" within months.

## Load-bearing claims

### Language choice matters for agentic work
Go outperforms Python for agentic coding, for reasons that generalize:
- Structural (implicit) interfaces mean type conformance is predictable, not surprising.
- Backwards-compatibility guarantee keeps training data current — agents don't generate deprecated APIs.
- Test invocation is simple and unsurprising; agents don't misunderstand `go test ./...`.
- Python's "magic" (pytest fixtures, async event loops) creates agent confusion; slow interpreter startup degrades iteration speed when agents spawn subprocesses.

The underlying principle: **ecosystem stability and low-magic syntax reduce agent surprise**. The specific language conclusion (Go) is contested — see caveats.

### Speed is existential; hangs are fatal
"Quick, clear tool responses are vital." Crashes are acceptable (they give error text). Hangs are fatal (no signal, context burns). Slow compilation and slow test startup directly cap agent productivity. The prescription: write throwaway "vibe-coded daemons" with hot-reload rather than restart-on-change pipelines when iteration speed matters more than code quality.

### Tools must be agent-proofed
Three properties Ronacher treats as non-negotiable for any tool an agent uses:
1. **Friendly errors** — communicate clearly what went wrong and what to do next.
2. **Chaos-monkey protection** — protect against an LLM using the tool wrong (double-spawn guards, idempotent ops, etc.).
3. **Observability** — logs to files so agents can self-diagnose without asking for help.

Concrete example: Makefile-based dev setup with process manager that guards against double-spawning and always writes logs to disk. Email verification links log to stdout in debug mode so agents can complete auth flows unaided.

### Simplicity is an agent multiplier
Code patterns that degrade agent performance: inheritance hierarchies, "clever hacks," permission checks hidden in config/middleware, deeply nested logic. Patterns that improve it:
- Long descriptive function names over class hierarchies.
- Plain SQL (agents match generated SQL against logs easily; ORMs add indirection).
- Permission checks inline and locally visible.
- Straightforward control flow over abstraction layers.

### Fewer dependencies, more generated code
Stable libraries (Go stdlib, Flask) beat fashionable ones. Frequent library churn means agents leave breadcrumbs that go stale quickly. Ronacher's contrarian prescription: **generate more code yourself rather than adding dependencies** — you know what the code does, the agent knows what the code does, and neither has to load an evolving third-party mental model.

### Parallelization requires isolation
Individual agents are not fast; running many in parallel is the throughput lever. But shared mutable state (filesystem, database) creates conflicts. Segmentation (separate DB schemas, isolated containers) is required. Tools like container-use (Dagger) enable per-agent Docker environments for safe parallel experimentation.

### Refactoring threshold awareness
Don't over-refactor, but know the threshold. A component library scattered across 50 files makes agent redesigns regress repeatedly. The right refactor moment is when the cognitive overhead of the current layout costs more agent cycles than the refactor would.

## Contested / conditional claims

- **Go > Python for agents** — specific to Ronacher's use cases (backend services, CLIs). TypeScript/Node is equally fast-startup and widely used for agentic work (see Pocock corpus). The underlying principle (low-magic, stable ecosystems) is sound; the language preference is personal.
- **More generated code, fewer deps** — contrarian to the mainstream "use a library for anything non-trivial." Applies when the dependency is fast-moving or poorly documented; not universal.
- **Hang > crash as failure mode** — aligns with feedback-loop-ceiling but is a sharper framing. Worth surfacing as a caveat there.
