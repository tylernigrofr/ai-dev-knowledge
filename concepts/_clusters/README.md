---
title: Concept clusters
type: cluster-index
last_reviewed: 2026-05-07
---

# Clusters

Clusters are thin module-level interfaces over the flat `concepts/` list. Each cluster file names a "seam" — the shared problem or design tension that binds a handful of atomic concepts — and lists its members with one-line roles.

## How to use

- Agents pull the **cluster file first** to discover the relevant concept bundle without scanning every atomic note.
- A cluster is an *index*, not a summary: the atomic concepts remain canonical. Pull them via `@skills/kb-pull.md` once you've narrowed down.
- Membership is single-assignment. A concept lives in its dominant cluster only. Some concepts belong to no cluster — that's fine; clusters aren't a partition.
- Cluster files are deliberately thin (~80 lines). If a cluster grows fat, split it.

## Adding a cluster

New clusters require justification. Prefer absorbing a concept into an existing cluster over inventing a new one — same curation gate as concepts themselves.
