---
name: rebuild-frontmatter
description: Use when concepts or playbooks have been added, modified, renamed, or deprecated and the computed `referenced_by` field across concept frontmatter needs to be recomputed. Scans all citations (`concepts:` / `concepts_used:` lists and inline `(slug.md)` body links) and writes the resulting back-reference list into each concept's frontmatter. Touches nothing else — does not bump `last_reviewed`, does not regenerate INDEX.md.
---

# rebuild-frontmatter

Recompute the `referenced_by` field on every concept by scanning citations across `concepts/` and `playbooks/`.

## What this skill owns

- The `referenced_by` field on `concepts/*.md` frontmatter.

## What this skill does NOT touch

- `last_reviewed` — left alone.
- All other concept frontmatter fields (`audience`, `activate_when`, `counter_to`, `cluster`, etc.) — author-curated, never machine-written.
- Playbook frontmatter — read-only here.
- `INDEX.md` — regenerate separately if needed.
- Concept bodies — read-only.

## Procedure

1. **Collect concept slugs.** `slug = filename without .md` for every file in `concepts/`.
2. **Scan citers.** For each file in `concepts/*.md` and `playbooks/*.md`:
   - Parse frontmatter. Collect slugs listed under `concepts:` or `concepts_used:` that match a known concept slug.
   - Parse body. Collect every markdown link of the form `(slug.md)` or `(../concepts/slug.md)` whose `slug` matches a known concept.
   - Drop self-references.
3. **Build the back-reference map.** For each cited slug, record `concept:<citer>` or `playbook:<citer>` depending on the citer's directory.
4. **Write `referenced_by` per concept.** Sort the list alphabetically. Emit as a YAML list under the `referenced_by:` key. If empty, write `referenced_by: []`.
5. **Preserve everything else.** Strip the existing `referenced_by` block (if any) and re-emit at the same position; do not reorder other keys; do not rewrite the body.

## Output

A diff that touches only the `referenced_by` block of each concept. No commits — leave staging to the caller.

## Caveats

- Pure mechanical scan. No LLM judgment.
- Run after `/triage-inbox`, after `/distill-concept` lands a new or renamed concept, and before regenerating `INDEX.md`.
- Renaming or deleting a concept invalidates inbound `referenced_by` entries elsewhere — re-run this skill to clean them up.
