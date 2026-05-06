---
name: add-source
description: Use when the user provides a single URL or pasted text and wants it added to the KB right now (skipping the inbox). Handles YouTube via Supadata MCP, articles via web fetch, and pasted text directly. Calls distill-concept after the source is captured.
---

# add-source

One-shot ingestion of a single source.

## Inputs

- A URL or pasted text.
- Optional: `type` override (`youtube | article | paper | repo | social | other`). Inferred from URL if not provided.
- Optional: `slug` override. Inferred from title if not provided.

## Procedure

1. **Capture content** based on type:
   - **YouTube**: Use the Supadata MCP `supadata_transcript` tool to fetch the transcript. Capture title, author, URL, published date if available.
   - **Article**: Fetch the page (web fetch). Capture title, author, URL, published date. Strip nav/footer; keep main content.
   - **Paper**: Same as article; flag `type: paper` for academic sources.
   - **Repo**: Capture README + key file paths + install notes. Note what's worth stealing.
   - **Social**: Capture the post text + author + URL. Often short — concept distillation will be the bulk of the work.
   - **Pasted text**: Treat as `type: other` unless overridden. Author = unknown unless provided.
2. **Write source file** to `sources/<type>/<slug>.md` with frontmatter per `.schemas/source.schema.json`.
3. **Extract candidate insights** from the captured content. Each insight should be a single load-bearing claim attributable to one or more concepts.
4. **For each candidate insight, call `distill-concept`**. The curation gate decides Refine / Replace / Supersede / Reject / Create.
5. **Update the source file's `concepts_seeded` array** with all concept slugs that were created or refined.
6. **Report** what was captured, what concepts were touched, and what was rejected.

## Output format

```markdown
## add-source result

**Source:** `sources/youtube/<slug>.md`
**Title:** ...
**Type:** youtube

**Concepts touched:**
- created: `concepts/foo.md`
- refined: `concepts/bar.md` (added "Why it matters" paragraph from new source)
- rejected: 2 candidate insights (duplicates of existing material)
```

## Caveats

- For long sources (full books, multi-hour videos), summarize before distilling — the smart zone applies.
- Paywalled articles: capture only what you have access to; note the limitation in the source body.
- Don't over-extract. Five high-quality insights beat twenty low-quality ones.
