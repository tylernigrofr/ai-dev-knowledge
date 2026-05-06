---
name: distill-concept
description: The KB curation gate. Use when a single insight needs to be routed into the concepts/ tree — decides Refine / Replace section / Supersede / Reject / Create. Called by add-source and triage-inbox; rarely invoked directly. The skill that keeps the KB lean.
---

# distill-concept

Apply the curation gate to a single insight.

## Inputs

- `insight` — a one-paragraph statement of the claim, with attribution to its source file.
- `source` — the source file slug or path the insight comes from.

## Procedure

1. **Find candidate concepts** — call `kb-search` with the insight's keywords + likely tags. Examine top 5 matches.
2. **Decide one of**:
   - **Refine** — the insight is a small clarification, a better phrasing, or a new example for an existing concept. Edit that concept inline. Bump `last_reviewed`. Add the source to `sources:` if not already there.
   - **Replace section** — the insight clearly improves one section (e.g. "How to apply") of an existing concept. Edit that section, preserve the rest. Bump `last_reviewed`. Add source.
   - **Supersede** — the insight is a materially better version of an existing concept's core claim. Mark the existing concept `status: deprecated` and add `superseded_by: <new-slug>`. Create the new concept. Old file stays for link integrity.
   - **Reject** — the insight is a duplicate or weaker than what's already in the KB. Log the rejection with reason in the triage report. Do not modify the KB.
   - **Create** — last resort. Only when no existing concept reasonably absorbs the insight. Justify in the triage report.
3. **Validate frontmatter** for any new or modified file against `.schemas/concept.schema.json`.
4. **Enforce the rules from CONTEXT.md**:
   - One idea per file. If the new file would not summarize in one sentence, decompose first.
   - 200-line soft cap. If a refine would push past it, decompose the existing concept instead.
   - Cite ≥1 source. Always.
5. **Report** the decision and the diff.

## Output format

```markdown
## distill-concept decision

**Insight:** "..."
**Source:** `sources/...`

**Decision:** refine
**Target:** `concepts/smart-zone-vs-dumb-zone.md`
**Change:** appended new "How to apply" bullet about token-count status line.
**last_reviewed:** updated to 2026-05-06
```

## Decision heuristics

- Two existing concepts both partially match → prefer the closer one and refine. Don't split the insight across both.
- Existing concept is older than 12 months and the new source post-dates a relevant model release → bias toward Supersede.
- Insight contradicts an existing concept → mark existing as `status: contested` and surface for human review rather than auto-Supersede.
- Brand-new domain that the KB doesn't cover at all → Create, but verify by searching twice with different keywords first.

## Caveats

- The default action is **Refine**. Create is the rarest outcome in a healthy KB. If you find yourself Creating most of the time, you're probably missing existing concepts in search.
- Refines should be small. A "refine" that touches every section is actually a Replace or a Supersede in disguise.
