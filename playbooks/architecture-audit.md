---
title: Recurring codebase architecture audit
phase: [review, decomposition]
tags: [architecture, deep-modules, refactoring, audit, subagents]
concepts_used:
  - deep-modules
  - dependency-categories
  - design-it-twice
  - integration-testing-bias
  - adr-discipline
  - ubiquitous-language
  - vertical-slices
tools: [claude-code, mattpocock-skills]
status: stable
superseded_by: null
last_reviewed: 2026-09-24
---

Periodically survey a bounded, recently-churning area for deepening opportunities with `/improve-codebase-architecture`, grill one candidate, and land it as tickets or record the rejection as an ADR.

## Prerequisites
- `CONTEXT.md` and `docs/adr/` are current. The audit names seams in domain language and must not re-litigate settled ADRs.
- The working tree is clean. The audit itself is read-only.

## Setup
- Choose scope **before** scanning (YAGNI). Weight hot spots from `git log`: areas that keep changing are where depth pays back. A whole-repo pass is for milestones. The default is one bounded subsystem.

## Loop
1. **`/improve-codebase-architecture`**, pointed at the chosen area. For a large repo, fan out several read-only explorer subagents (a scripted workflow if there are many), each scoring its area on **current friction × future load**.
2. **Read the report** (HTML, in a temp dir). Each candidate card should show:
   - the modules involved;
   - the problem, in `/codebase-design` vocabulary (depth, seam, leverage, locality);
   - a before/after picture;
   - a strength rating;
   - any ADR conflicts.
3. **Sort the output into four piles:**
   - *Candidates* are each a grilling conversation waiting to happen.
   - *Housekeeping* is mechanical and needs no grilling. File it straight as tickets.
   - *Live defects found in passing* get filed as bugs now.
   - *What is already right: do not touch.* Record it so the next audit doesn't re-propose it.
4. **Pick one candidate** and grill it inside the skill's loop.
   - To explore interface shapes, use `/codebase-design`'s design-it-twice with parallel subagents.
   - Classify each dependency (in-process / local-substitutable / remote-owned / true external) to decide how tests cross the new seam.
5. **Land the decision:**
   - *Accepted:* `/to-spec` → `/to-tickets`, with prefactoring first and expand–contract for wide changes. Then run it through [orchestrated-issue-waves](orchestrated-issue-waves.md).
   - *Rejected for a load-bearing reason:* record an ADR so future audits don't re-suggest it.

## Verification
- Every accepted candidate became tickets whose acceptance criteria are stated as tests through the *new* interface.
- After the refactor lands, the module passes the deletion test: deleting it would scatter complexity across callers.
- The next audit of the same area proposes different things.

## Failure modes
- **Refactor theatre.** A review request isn't a mandate for a broad rewrite. One candidate, one small first slice.
- **Shallow "extract for testability" wins.** These move complexity instead of concentrating it. Apply the deletion test before accepting.
- **Audit drift into style.** Findings without friction evidence (bouncing between files, untestable seams, leaking coupling) get dropped.
- **Ignoring ADRs.** Surface a conflict only when the friction is real enough to reopen the decision, and say so explicitly.
