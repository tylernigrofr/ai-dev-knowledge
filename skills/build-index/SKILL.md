---
name: build-index
description: Regenerate INDEX.md and lint the AI dev knowledge base after concepts, playbooks, or sources are added, changed, or deprecated.
---

# build-index

Run from the live KB repo (never the plugin cache):

```bash
python3 scripts/kb.py refs    # recompute referenced_by first
python3 scripts/kb.py lint    # frontmatter, citations, broken links, clusters, 200-line cap
python3 scripts/kb.py index   # rewrites INDEX.md; lint warnings are embedded at the bottom
```

Fix lint problems before committing. INDEX.md is generated — never hand-edit it.
