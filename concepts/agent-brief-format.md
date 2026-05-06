---
title: Agent brief format (durability + behavioral + acceptance + scope)
type: technique
phase: [decomposition]
tags: [triage, agent-brief, afk, issue-tracker]
sources:
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
When an issue moves to `ready-for-agent`, post a structured comment — the *agent brief* — that becomes the contract the AFK agent works from. The brief must be durable to codebase change, behavioral rather than procedural, with concrete acceptance criteria and explicit scope boundaries.

## Why it matters
Issues sit in `ready-for-agent` for days or weeks. By the time an agent grabs one, file paths and line numbers have moved. A brief that says "edit src/foo.ts line 42" is dead on arrival; a brief that says "the `SkillConfig` type should accept an optional `schedule: CronExpression` field" still works. The agent will explore the code fresh and pick the implementation — what it needs from you is *what done looks like*, not *how to get there*.

## The four discipline rules

1. **Durability over precision.** Describe interfaces, types, and behavioral contracts. Never reference file paths or line numbers — they go stale. Don't assume current implementation structure persists.
2. **Behavioral, not procedural.** Describe *what* the system should do, not *how* to implement it.
   - Good: "When a user runs `/triage` with no arguments, they see a summary of issues needing attention."
   - Bad: "Add a switch statement in the main handler function."
3. **Complete acceptance criteria.** Concrete, independently testable items the agent can self-check against. "Triage should work correctly" is not a criterion; "Running `gh issue list --label needs-triage` returns issues that have been through initial classification" is.
4. **Explicit scope boundaries.** State what is *out of scope*. Prevents gold-plating and assumptions about adjacent features.

## Template

```markdown
## Agent Brief

**Category:** bug | enhancement
**Summary:** one-line description

**Current behavior:**
What happens now. For bugs, the broken behavior. For enhancements, the status quo.

**Desired behavior:**
What should happen after the agent's work. Be specific about edge cases and errors.

**Key interfaces:**
- `TypeName` — what changes and why
- `functionName()` return type — current vs desired
- Config shape — any new options

**Acceptance criteria:**
- [ ] Specific, testable criterion 1
- [ ] Specific, testable criterion 2

**Out of scope:**
- Adjacent feature that should NOT be touched
- Related concern that's separate
```

## Caveats
- The original issue body and discussion are *context*; the agent brief is the *contract*. If they conflict, the brief wins — that's why grilling sharpens it before posting.
- For bugs, attempt reproduction *before* writing the brief; the confirmed repro becomes the desired-behavior anchor.

## Related
- [triage-state-machine](triage-state-machine.md) — when in the lifecycle the brief is posted
- [grilling-alignment](grilling-alignment.md) — how the brief gets sharpened
- [prd-discipline](prd-discipline.md) — out-of-scope as definition-of-done at PRD level
- [afk-vs-hitl](afk-vs-hitl.md) — only `ready-for-agent` issues need this format
