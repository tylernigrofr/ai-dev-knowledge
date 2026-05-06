---
name: build-index
description: Use when concepts or playbooks have been added, modified, or deprecated and INDEX.md needs to be regenerated. Produces a multi-axis index (by type, phase, tag, status) reading from frontmatter. Hides deprecated entries by default.
---

# build-index

Regenerate `INDEX.md` from frontmatter.

## Procedure

1. **Read** all `concepts/*.md` and `playbooks/*.md`. Parse frontmatter.
2. **Validate** each frontmatter against `.schemas/concept.schema.json` and `.schemas/playbook.schema.json`. Collect errors but do not abort — emit a warnings section at the end of the index.
3. **Build sections**:
   - **Playbooks** (top of index, all playbooks alphabetically by title, with one-line summary).
   - **Concepts by type** — one subsection per `type` (mental-model, principle, technique, tool, framework, anti-pattern, workflow). Within each, alphabetical.
   - **Concepts by phase** — cross-cut. One subsection per phase with concepts that include it.
   - **Concepts by tag** — one subsection per tag, listing concepts. Tags appearing in only one concept can collapse to a "Misc tags" footer.
   - **Sources** — by type, alphabetical, link only. Source content is for citation, not browsing.
   - **Deprecated** (collapsed `<details>`) — concepts with `status: deprecated`, with their `superseded_by` link.
4. **Append a generation timestamp** at the bottom: `_Generated: YYYY-MM-DD HH:MM_`.
5. **Append warnings section** if any frontmatter validation failed.
6. **Write** `INDEX.md`.

## Output format

```markdown
# Index

_Last generated: 2026-05-06 14:30_

## Playbooks

- [AFK night-shift implementation loop](playbooks/afk-night-shift.md) — `draft`

## Concepts by type

### Mental models
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — ...

### Principles
- ...

### Anti-patterns
- ...

(etc.)

## Concepts by phase

### planning
- ...

(etc.)

## Concepts by tag

### context-management
- [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md)
- [Compacting vs clearing context](concepts/compacting-vs-clearing.md)
- [Push vs pull context](concepts/push-vs-pull-context.md)

(etc.)

## Sources

### YouTube
- [Vibe-Coding to Vibe-Engineering](sources/youtube/pocock-vibe-engineering-2025.md)

<details>
<summary>Deprecated (0)</summary>
(none yet)
</details>

<details>
<summary>Warnings</summary>
(none)
</details>
```

## Caveats

- This skill is purely deterministic — no LLM judgment in the index itself. The cleanest implementation is a script; this skill describes the contract.
- Run after every triage session and before any commit-bump that touches frontmatter.
