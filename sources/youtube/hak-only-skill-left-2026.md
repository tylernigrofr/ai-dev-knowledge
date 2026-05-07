---
title: "Is this the only skill left? — Hak (AgentiveStack)"
type: youtube
url: https://www.youtube.com/watch?v=7zCsfe57tpU
author: Hak
captured: 2026-05-07
status: extracted
concepts_seeded:
  - llm-not-a-trustworthy-abstraction
  - systems-thinking-three-questions
  - jagged-frontier
---

## Summary
Hak (product engineer turned founder, AgentiveStack) argues that systems thinking — the skill senior devs accidentally built over years — is now the load-bearing skill in agentic engineering. Frames it through Peter Naur's *Programming as Theory Building* (1985): the code is the shadow; the program lives in the programmer's head. AI generates the shadow on demand, but the theory still has to be built deliberately.

## Key claims

- **Naur's theory-building still applies.** AI generates code; it does not generate the theory of why the pieces connect.
- **Prompting is the easy layer; systems thinking is the durable one.** Models keep getting better at intent inference — the differentiator is conducting the orchestra, not playing instruments.
- **LLMs are not a trustworthy abstraction layer like compilers.** Compiler output is deterministic and verifiable without understanding; LLM output is stochastic, can introduce vulnerabilities/race conditions/wrong rules silently. "An LLM is a collaborator you can only trust by understanding what it did."
- **Three diagnostic questions for any system you build with AI:**
  1. Where does state live? (Two pieces both thinking they own truth = bug not yet triggered.)
  2. Where does feedback live? (If nothing tells you it's working, it's pretending to work.)
  3. What breaks if I delete this? (Trace the blast radius before you touch.)
- **Jagged frontier (Harvard).** AI is sharp in some places and dull in others, sometimes in the same session. Knowing where the edges sit is part of the new literacy.
- **Audit anecdote.** Lovable-built product, live with paying customers, ~7,000-line file, no logs, no rate limiting, no error handling. Every failure mode was a systems-thinking failure, not a coding one.
- **Seniority-biased technological change (Hosseini & Lichtinger).** After Q1 2023, junior hiring dropped sharply at GenAI-adopting firms; senior employment kept rising. Early 2026 the pendulum is swinging back (Indeed +11% YoY, IBM tripling entry-level US hiring, Salesforce/Intuit re-hiring). The industry broke the pipeline that turns juniors into seniors.
- **Juniors got robbed of the forcing function.** Pre-AI, hitting a wall meant going through it. AI removed the wrestle, not the pressure. Build the forcing function deliberately.
- **AI collapses the backend/frontend/devops silos.** Generalists who hold the whole picture in their head win; AI handles depth in any single lane.
- **Four "unsexy moves" for training systems thinking:**
  1. Design before you prompt — boxes-and-arrows on paper, mark state and failure surfaces.
  2. Specs as scaffolding — write the what/why before AI writes the how.
  3. Deletion test — pick a recent component, ask what breaks if you delete it. "I don't know" = study list.
  4. Study generated code — push back on the agent ("walk me through this, what alternatives?"); rewrite something by hand weekly.
- **Closing line:** "The skill is learnable. It's just not promptable."

## Notable framing

- Code-as-fast-food analogy: cheap and fast, useful only if you know what a real meal tastes like.
- Fitness analogy: the average is less fit because the environment does less of the work, but elite athletes are the fittest ever — deliberate training compounds. Same trajectory for coding.
- Compiler-vs-LLM: an abstraction is only trustworthy when the layer below is verifiable.
