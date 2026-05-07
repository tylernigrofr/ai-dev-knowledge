---
title: Jagged frontier of AI capability
type: mental-model
phase: [planning, implementation, review]
tags: [model-capability, judgment, literacy, evaluation]
sources: [sources/youtube/hak-only-skill-left-2026.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-07
audience: [planner, implementer, reviewer]
activate_when: "Deciding whether to delegate a task to an AI agent, or noticing the model is unexpectedly confident-and-wrong on something it 'should' handle."
counter_to: null
cluster: null
referenced_by: []
---

## Summary
"Jagged frontier" (Harvard Business School, Dell'Acqua et al.) names the fact that AI is sharp on some tasks and surprisingly dull on adjacent ones — sometimes within the same session. Knowing where the edges sit for the model you're using is now a core developer skill.

## Why it matters
The frontier isn't a smooth contour. A model that one-shots a complex refactor will, minutes later, hallucinate an API that doesn't exist or miss a trivial off-by-one. Treating capability as uniform — "if it can do X, it can do the easier-looking Y" — produces silent failures. The skill is empirical: you have to map the jagged edge for *this* model on *this* class of task in *this* codebase, and re-map when the model changes. Without that map, delegation decisions are guesses, and "it usually works" is the worst possible feedback signal because it discourages verification.

## How to apply
- Maintain a personal/team list of *known sharp* and *known dull* zones for the models you use. Update it when the model version changes.
- For tasks near a known dull edge, raise verification effort (more tests, more grilling, smaller diffs).
- When a model is confidently wrong, log it — that data point shifts the frontier in your map.
- Pair with [llm-not-a-trustworthy-abstraction](llm-not-a-trustworthy-abstraction.md): the jagged frontier is *why* the abstraction isn't trustworthy.
- For non-technical builders shipping with Lovable/Bolt/Cursor, this skill is the substitute for "learning to code" — knowing when to call in someone who speaks code.

## Caveats
- The frontier shifts every few months as models update. A stale map is worse than no map because it gives false confidence.
- The edges are partly task-shaped and partly context-shaped — same task in a different codebase can land on a different side.

## Related
- [llm-not-a-trustworthy-abstraction](llm-not-a-trustworthy-abstraction.md)
- [feedback-loop-ceiling](feedback-loop-ceiling.md) — how good your eval signal is bounds how well you can map the frontier.
- [pre-ai-fundamentals](pre-ai-fundamentals.md) — the theory you need to recognise the dull zones.
