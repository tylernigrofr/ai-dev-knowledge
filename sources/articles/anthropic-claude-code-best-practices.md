---
title: "Best practices for Claude Code — Anthropic Engineering"
type: article
url: https://www.anthropic.com/engineering/claude-code-best-practices
author: Anthropic
published: 2025-01-01
captured: 2026-05-06
status: extracted
concepts_seeded:
  - smart-zone-vs-dumb-zone
  - compacting-vs-clearing
  - push-vs-pull-context
  - clean-context-reviewer
  - tdd-for-afk
  - sand-castle-parallelization
---

# Best practices for Claude Code — Anthropic Engineering

Official Anthropic guide. Published on `anthropic.com/engineering`; redirects to `code.claude.com/docs/en/best-practices`. No named author or precise date; assumed current/evergreen as of capture.

## Load-bearing claims

### Context window is the single most important resource

"LLM performance degrades as context fills. When the context window is getting full, Claude may start 'forgetting' earlier instructions or making more mistakes." The context window holds every message, file read, and command output — a debugging session or codebase exploration can burn tens of thousands of tokens fast.

### Verification criteria is the highest-leverage input

"The single highest-leverage thing you can do" is giving Claude a way to verify its own work: run tests, compare screenshots, validate outputs. Without success criteria the model produces plausible-looking output that doesn't actually work, and the human becomes the only feedback loop.

Concrete upgrade patterns:
- Spec + test cases in the prompt instead of vague task descriptions
- Screenshot-based UI verification ("take a screenshot, compare to the original, list differences, fix them")
- Pipe actual error output rather than describing the symptom; require the fix to pass, not suppress

### Explore → Plan → Implement → Commit workflow (plan mode)

Use plan mode to separate research from execution:
1. **Explore**: Claude reads files without editing (plan mode)
2. **Plan**: ask for a concrete implementation plan, edit it in-editor with `Ctrl+G`
3. **Implement**: exit plan mode, Claude codes against the plan with tests
4. **Commit**: Claude commits and opens a PR

Skip planning when the change fits in one sentence; add it when scope is unclear, multi-file, or you're unfamiliar with the code.

### CLAUDE.md must be short to work

A bloated CLAUDE.md is an anti-pattern: important rules get lost in the noise and Claude ignores them. Heuristic: *"Would removing this cause Claude to make mistakes?"* If not, cut it. Signs of bloat: Claude keeps doing the thing you told it not to, or asks questions answered in the file.

What belongs: Bash commands Claude can't guess, non-default code style, test runner instructions, repo etiquette, env-var quirks, known gotchas.

What doesn't belong: things Claude can infer from code, standard language conventions, detailed API docs, file-by-file codebase descriptions, frequently-changing info.

CLAUDE.md is push context (always loaded). Skills are pull context (loaded on demand). Use CLAUDE.md for always-needed persistent context; use skills for domain knowledge that only applies sometimes.

### `/clear` between unrelated tasks; restart after two failed corrections

Two failure patterns: (1) kitchen-sink sessions mixing unrelated tasks accumulate irrelevant context; (2) repeated corrections compound noise. In both cases, `/clear` and a better prompt outperform continuing the long session.

"After two failed corrections, `/clear` and write a better initial prompt incorporating what you learned. A clean session with a better prompt almost always outperforms a long session with accumulated corrections."

### Subagents keep main context clean

When Claude investigates a codebase (reads lots of files), all those files fill the main context. Subagents explore in a separate context window and report back summaries. Use them for: codebase research, code review after implementation ("use a subagent to review this code for edge cases"), or anything investigation-shaped.

### Writer/Reviewer parallel sessions

Fresh context improves code review since Claude won't be biased toward code it just wrote. Two-session pattern: Session A implements, Session B reviews with no prior context. Equivalent to the clean-context-reviewer principle but now Anthropic-native via the parallel sessions / worktrees feature.

### Let Claude interview you (AskUserQuestion pattern)

For larger features, start with a minimal prompt and ask Claude to interview you using `AskUserQuestion`. Claude asks about implementation, UX, edge cases, and tradeoffs you might not have considered. When done, Claude writes a spec to `SPEC.md`. Then start a fresh session to execute it.

This is effectively a Claude-native version of the grilling-alignment technique.

### Hooks for must-happen-every-time actions

Unlike CLAUDE.md instructions (advisory), hooks are deterministic. Use them for: linting after every edit, blocking writes to sensitive directories. "Claude can write hooks for you."

### Non-interactive mode for CI/automation

`claude -p "prompt"` runs headless. `--output-format stream-json` for streaming. `--allowedTools` to scope permissions for batch operations. Fan out with a shell loop for large migrations (generate file list → loop `claude -p` per file → test on 2–3 first).
