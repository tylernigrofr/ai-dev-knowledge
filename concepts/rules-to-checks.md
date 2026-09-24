---
title: Turn repeated agent mistakes into checks, not instructions
type: principle
phase: [implementation, review, qa]
tags: [harness-engineering, feedback-loops, claude-md, hooks, guardrails]
sources:
  - sources/articles/hashimoto-ai-adoption-journey.md
  - sources/repos/owner-practice-2026.md
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-09-24
---

## Summary
When an agent makes the same mistake twice, add a deterministic check it can't route around (a script, hook, lint rule or test that pins the policy) rather than another line in CLAUDE.md. Prose is for judgment calls. Mechanical rules belong in code.

## Why it matters
Instructions in CLAUDE.md compete for attention in every turn and get ignored under load. A check fires every time, at zero context cost, and it fails loudly. The pattern is sometimes called *harness engineering*: each fix accumulates in the environment rather than in a conversation that ends. It also shrinks CLAUDE.md, which keeps push context lean for the rules that genuinely need judgment.

## How to apply
- After a correction, ask: "Could a script have caught this?" If yes, write that script and point CLAUDE.md at it. The rule's prose shrinks to one line: "use X; never do Y by hand."
- **Wrap multi-step rituals in one guarded command.** Example: a `merge_guard` that rebases, lints, runs the required tests, reads the verdict from exit codes, and only then merges. Declare it "the only sanctioned way".
- **Pin policies with tests**, including *absences*. Examples: a test that fails if a forbidden CI workflow reappears; a test that the manual matches the CLI surface.
- **Pre-commit hooks** for secrets, gitignored paths and binaries. Never bypass them with `--no-verify`; fix what the hook names.
- **Make silent failures loud.** Examples: a suite that refuses to run when fixture paths are missing, instead of skipping 90 tests and reporting green.
- Keep a short `CODING_STANDARDS.md` or `REVIEW.md` only for what can't be mechanized. Pocock's in-progress `retro` skill does this triage after a session.

## Caveats
- Checks encode assumptions, and assumptions go stale as models improve (Anthropic, 2026). Invariants age well ("a citation must resolve"). Procedures don't ("parse the title block this way"). Delete checks that only encode yesterday's workaround.
- Don't mechanize taste. A check with a high false-positive rate trains agents (and you) to ignore it.

## Related
- [feedback-loop-ceiling](feedback-loop-ceiling.md): checks are feedback loops
- [agent-safe-tooling](agent-safe-tooling.md): checks agents invoke should explain what to do next
- [push-vs-pull-context](push-vs-pull-context.md): what stays in CLAUDE.md
