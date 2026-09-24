---
name: rebuild-frontmatter
description: Recompute the computed `referenced_by` back-citation field on every AI dev KB concept after concepts or playbooks are added, renamed, linked, or deprecated.
---

# rebuild-frontmatter

Run from the live KB repo (never the plugin cache):

```bash
python3 scripts/kb.py refs    # rewrites only the referenced_by block of each concept
python3 scripts/kb.py lint
```

It scans `concepts:` / `concepts_used:` lists and inline `(slug.md)` / `(../concepts/slug.md)` links across concepts and playbooks, drops self-references, and writes a sorted `concept:<slug>` / `playbook:<slug>` list. It touches nothing else: not `last_reviewed`, not author-curated fields (`audience`, `activate_when`, `counter_to`, `cluster`), not bodies. Follow with `build-index`.
