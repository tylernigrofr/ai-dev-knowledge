---
name: kb-search
description: Search the AI dev knowledge base (agentic coding workflows, context management, orchestration, testing, architecture) for concepts and playbooks by freetext, tag, type, or phase. Use before non-trivial planning or when the user asks what the KB says about a practice.
---

# kb-search

Run the deterministic search script — don't grep or rank by hand.

```bash
python3 "$KB/scripts/kb.py" search <terms...> [--tag T] [--type T] [--phase P] [--kind concept|playbook|source] [--all]
```

`$KB` = `$AI_KB_PATH` if set, otherwise two directories up from this skill's base directory.

- Default kinds: concepts + playbooks. Deprecated entries are hidden unless `--all`.
- Terms are OR-scored (title > slug > tags > summary > body). Use 1–3 distinctive words, not sentences.
- Types: `mental-model principle technique tool framework anti-pattern workflow`. Phases: `planning decomposition implementation review qa`.

Output is a ranked markdown list with one-line summaries. Pick the 1–3 most relevant and read them with `kb-pull`. This skill retrieves; synthesis is the caller's job.
