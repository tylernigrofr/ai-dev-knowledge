---
name: kb-search
description: Use when the user or another agent needs to find concepts or playbooks in the AI dev knowledge base by tag, type, phase, or freetext. Returns a ranked list of matching files with one-line summaries. The main agent-facing retrieval verb of the KB.
---

# kb-search

Query the AI dev knowledge base at `$AI_KB_PATH` (or the current repo if invoked from inside the KB itself).

## Inputs

The user supplies one or more of:
- `query` — freetext keyword(s)
- `tag` — frontmatter tag (e.g. `context-management`)
- `type` — concept type (`mental-model | principle | technique | tool | framework | anti-pattern | workflow`)
- `phase` — lifecycle phase (`planning | decomposition | implementation | review | qa`)
- `kind` — `concept | playbook | source` (default: concept + playbook)

## Procedure

1. Resolve `$AI_KB_PATH`. If unset and not inside a KB repo, error with the message: "Set AI_KB_PATH or run from inside the KB repo."
2. List candidate files based on `kind` (default: `concepts/*.md` and `playbooks/*.md`).
3. Filter by frontmatter:
   - `tag` matches if it appears in the `tags` array.
   - `type` matches if `type:` equals (concepts only).
   - `phase` matches if it appears in the `phase` array.
   - Exclude `status: deprecated` unless explicitly requested via `include_deprecated: true`.
4. If `query` is provided, score remaining candidates by:
   - Title match (highest weight)
   - Tag match
   - Body match (Summary + Why it matters sections preferred)
5. Return top 10 results as a markdown list. Each item:
   - `[Title](relative/path.md)` — one-sentence summary (the Summary section).
   - Frontmatter chips: `type · phase · status`.

## Output format

```markdown
## kb-search results (N matches)

1. [Smart zone vs dumb zone](concepts/smart-zone-vs-dumb-zone.md) — Every LLM session has a smart zone (~100k tokens) where attention is clean, then degrades.
   `mental-model · planning,implementation,review · stable`
2. ...
```

## Examples

- "Find concepts tagged `context-management`" → filter by tag.
- "What does the KB say about reviewing AI code?" → freetext "review" + phase=review.
- "Show me all anti-patterns" → type=anti-pattern, no query.

## Caveats

- For deep retrieval (full content), use `kb-pull` after picking a result.
- This skill does not synthesize across results; it retrieves. Synthesis is the caller's job.
