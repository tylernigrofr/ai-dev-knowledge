---
title: Design module interfaces yourself; delegate the implementation
type: technique
phase: [planning, implementation]
tags: [architecture, delegation, mental-map, metacognition]
sources: [sources/youtube/pocock-vibe-engineering-2025.md]
status: stable
superseded_by: null
last_reviewed: 2026-05-06
referenced_by:
  - concept:code-first-automation
  - concept:deep-modules
audience: [planner, implementer]
activate_when: "Handing implementation to an agent and deciding what to keep."
cluster: decomposition
---

## Summary
Stay personally responsible for the shape of every module's public interface — its name, signatures, and contracts — but delegate everything inside the box to the AI; this preserves your mental map of the codebase while still capturing AI throughput.

## Why it matters
The more you delegate, the less you know your own code. And the less you know your code, the less you can shape it — which means your interface decisions get worse, which means the AI's grey-box implementations land in the wrong places. The rot is self-reinforcing. By owning interfaces, you keep the mental scaffolding intact: you know where things live, what depends on what, and where the seams are. The AI can move at full speed inside the boxes you've drawn.

## How to apply
- Before any AFK delegation, sketch the module's public surface yourself — types, function names, return shapes, error contracts.
- Write the interface file (or its skeleton) by hand or with tight collaboration. Then point the agent at the implementation.
- Resist the temptation to let the AI propose the interface. Its suggestions optimize for "looks reasonable in isolation," not "fits the codebase's joint distribution."
- When reviewing AI work, judge it against your interface decisions, not the other way around.
- Periodically audit which modules you can no longer explain. That's where your mental map has eroded — fix it before adding more.

## Caveats
- Greenfield exploration is an exception: let the AI propose interfaces during prototyping, then redraw them yourself before committing.
- For genuinely throwaway code (one-off scripts), don't bother.

## Related
- [deep-modules](deep-modules.md) — what good interfaces look like
- [improve-codebase-architecture](#) — Pocock's skill for finding modules to deepen
- [grilling-alignment](grilling-alignment.md) — where interface decisions get crystallized
