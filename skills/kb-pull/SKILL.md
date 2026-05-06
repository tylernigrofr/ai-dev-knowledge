---
name: kb-pull
description: Use when an agent needs the full contents of a specific concept, playbook, or source from the AI dev knowledge base. Given a slug or path, returns the full markdown including frontmatter. Convenience wrapper around file read.
---

# kb-pull

Return the full contents of a single KB file.

## Inputs

- `slug` — the file slug (e.g. `smart-zone-vs-dumb-zone`) or full relative path (e.g. `concepts/smart-zone-vs-dumb-zone.md`).
- `kind` (optional) — `concept | playbook | source`. Used to disambiguate slug-only inputs.

## Procedure

1. Resolve `$AI_KB_PATH`.
2. If `slug` is a full path, read it. Else search:
   - `concepts/<slug>.md` if `kind` is concept or unspecified.
   - `playbooks/<slug>.md` if `kind` is playbook or unspecified.
   - `sources/*/<slug>.md` if `kind` is source or unspecified.
3. If multiple matches, list them and ask the caller to disambiguate.
4. Return the full file contents (frontmatter + body).

## Output format

Return raw markdown. The caller can render or excerpt as needed.

## Caveats

- For multi-file retrieval, call `kb-search` first.
- Deprecated entries are still pullable; the caller is responsible for noting the status.
