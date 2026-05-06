---
title: Own your planning stack (don't outsource to frameworks)
type: principle
phase: [planning, implementation]
tags: [tooling, observability, framework-lock-in]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Keep your skills, prompts, and loops in your own repo as plain files you can edit — frameworks like TaskMaster that hide the pipeline leave you blind when something fails, and AI workflows fail constantly.

## Why it matters
The pipeline *is* the product when you're doing AI engineering. If a third-party framework owns your prompt structure, your context-assembly logic, and your loop control flow, every failure mode becomes a black box: was the prompt wrong? Was context truncated? Did a hook misfire? You can't tell, you can't fix it, and you can't evolve it as your understanding sharpens. Owning the stack means failures are debuggable, and improvements compound — your skills get better with every project.

## How to apply
- Keep skills as plain markdown files in your repo or `~/.claude/skills/`.
- Keep loop scripts (Ralph loop, planner, reviewer) as readable bash/python you can `cat`.
- Avoid frameworks that bundle prompt + execution + state into an opaque CLI.
- When evaluating a tool, ask: "If this fails at 3am, can I read the source and fix it?"
- Borrow patterns from others (see Pocock's [skills repo](https://github.com/mattpocock/skills)), but copy them in — don't depend on a vendored framework.

## Caveats
- This applies to your *planning/orchestration* layer. For genuinely commodity infrastructure (LLM SDK, vector DB client) frameworks are fine.
- Solo experimentation can use a framework; don't ship a team workflow on one.

## Related
- [ralph-loop](ralph-loop.md) — the kind of loop you should own
- [push-vs-pull-context](push-vs-pull-context.md) — your context strategy is yours to tune
