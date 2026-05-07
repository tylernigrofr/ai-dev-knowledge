---
name: kb-curation
description: Keeping a knowledge base lean — bias toward refine, fight doc rot, generate docs just-in-time.
type: cluster
members:
  - just-in-time-docs
  - doc-rot
  - out-of-scope-knowledge-base
last_reviewed: 2026-05-07
---

## Seam

The shared concern: committed markdown decays the moment it's written; the only stable docs are the ones generated on demand from live artifacts (code, tests, frontmatter). These concepts together motivate the **curation gate**: prefer refine over create, prune deprecated material, route "not now" ideas to a durable out-of-scope store rather than letting them rot in the main tree.

## Members

- **just-in-time-docs** — generate architecture/system overviews on demand; don't commit them.
- **doc-rot** — committed prose drifts from reality; the failure mode the rest of the cluster fights.
- **out-of-scope-knowledge-base** — durable home for wontfix/later ideas so the active KB stays focused.
