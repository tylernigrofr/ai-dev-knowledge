---
title: "My AI adoption journey — Mitchell Hashimoto"
type: article
url: https://mitchellh.com/writing/my-ai-adoption-journey
author: Mitchell Hashimoto
published: 2026-02-01
captured: 2026-09-24
status: extracted
concepts_seeded:
  - rules-to-checks
---

# Hashimoto — harness engineering (summary via research subagent, 2026-09-24)

- **Harness engineering:** when an agent makes a mistake, don't just correct it; build something (a script, check, or tool the agent can run) so that class of mistake can't recur. Fixes accumulate in the environment, not in conversation.
- Related: Pocock's in-progress `retro` skill (2026-08) proposes environment changes after a session: mechanical rules become lint/hook/CI checks, and `CODING_STANDARDS.md` is reserved for judgment calls. Anthropic's "Harness design for long-running application development" (2026-03-24) warns that assumptions encoded in a harness go stale as models improve.

Captured second-hand (research summary); re-read the original before quoting.
