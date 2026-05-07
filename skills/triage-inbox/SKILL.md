---
name: triage-inbox
description: Use when the user wants to process accumulated material in _inbox/ — URLs in urls.md and drop files in drops/. Routes each item to source / seed / junk via add-source and distill-concept, then archives processed drops to _processed/. The batch verb of the KB ingestion pipeline.
---

# triage-inbox

Batch-process the inbox.

## Inputs

None — operates on the contents of `_inbox/` in the current KB.

## Procedure

### 1. Process `_inbox/urls.md`

For each non-comment, non-blank line:
1. Treat the line as a URL. Detect type from the URL (youtube.com / youtu.be → youtube, github.com → repo, x.com / twitter.com → social, else article).
2. Call `add-source` with the URL.
3. On success, remove the line from `urls.md`.
4. On failure (network, paywall, parse), leave the line and append a comment with the error.

### 2. Process `_inbox/drops/*.md`

For each drop file (sorted by filename, oldest first):
1. **Classify** the drop:
   - **Source-shaped** — has a clear external attribution (URL, author, publication). Treat as a pasted-source.
   - **Seed-shaped** — half-formed thoughts, snippets without clear attribution, the user's own ideas.
   - **Junk** — empty, duplicate, or obvious test content.
2. **Route**:
   - Source-shaped → call `add-source` with the pasted text.
   - Seed-shaped → extract the load-bearing claim(s) and call `distill-concept` directly with `source: <drop-path>`. (For seeds, the drop file *is* the source — copy it to `sources/social/` or `sources/other/` as appropriate before distilling.)
   - Junk → delete.
3. **Archive** the drop file:
   - Move to `_inbox/_processed/YYYY-MM/<original-filename>` where YYYY-MM is the drop's month.
   - Append a routing-header line at the end of the file: `<!-- routed: → concepts/foo.md, sources/youtube/bar.md -->`

### 3. Report

After the batch, output a triage report covering:
- URLs processed (✅ / ❌ with reasons)
- Drops processed (counts by route: source / seed / junk)
- Concepts created / refined / superseded / rejected
- Any items requiring user review (e.g. flagged `status: contested`)

## Output format

```markdown
## Triage report — 2026-05-06

### URLs (3 processed, 1 failed)
- ✅ https://youtu.be/X → sources/youtube/foo.md (refined 2 concepts)
- ✅ https://example.com/article → sources/articles/bar.md (created concepts/baz.md)
- ❌ https://paywalled.com/x — paywall, left in queue

### Drops (5 processed)
- 3 source-shaped → 3 sources, 7 concept refinements
- 1 seed → 1 concept refinement
- 1 junk → deleted

### Needs user review
- `concepts/old-thing.md` flagged `status: contested` — new source contradicts current claim
```

## Caveats

- Run incrementally. A 50-drop inbox in one session will exceed the smart zone — process in batches of ~10.
- After triage, run `rebuild-frontmatter` to refresh `referenced_by` across concepts.
- If a drop is clearly mis-categorized, fix the classification rather than forcing it through.
