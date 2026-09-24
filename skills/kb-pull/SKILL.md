---
name: kb-pull
description: Read the full contents of a specific AI dev knowledge base concept, playbook, or source by slug or path. Use after kb-search picks a result.
---

# kb-pull

`$KB` = `$AI_KB_PATH` if set, otherwise two directories up from this skill's base directory.

Given a slug, read the first that exists: `$KB/concepts/<slug>.md`, `$KB/playbooks/<slug>.md`, `$KB/sources/*/<slug>.md`. Given a relative path, read `$KB/<path>`.

Return the file as-is. If it's `status: deprecated`, say so and pull its `superseded_by` instead unless the caller asked for the old one. Follow `Related` links only when the caller needs them — pull on demand, don't preload.
