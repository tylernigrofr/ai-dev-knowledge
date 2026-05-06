---
title: Dependency categories for deepening (in-process / local-substitutable / remote-owned / true external)
type: principle
phase: [planning, implementation]
tags: [architecture, dependencies, ports-adapters, seams, testing]
sources:
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Before deepening a cluster of shallow modules, classify each dependency into one of four categories — in-process, local-substitutable, remote-but-owned, true external — because the category dictates how the deepened module is tested across its seam.

## Why it matters
"Just merge these modules" is naive when one of them touches Stripe and another touches a Postgres call. The merge is fine; what changes is whether you need a port + adapter, an in-memory stand-in, a mock, or nothing at all. Picking the wrong strategy gives you either over-abstraction (a port for something that never varies) or under-abstraction (a hard dependency on Stripe in the test suite). The four categories are the cheat sheet.

## The four categories

1. **In-process.** Pure computation, in-memory state, no I/O. Always deepenable — merge and test the deepened module's interface directly. No adapter needed.
2. **Local-substitutable.** Has a real local stand-in (PGLite for Postgres, in-memory FS, fake clock). Deepen and run the stand-in inside the test suite. The seam is *internal* to the module — no port at the external interface.
3. **Remote but owned (Ports & Adapters).** Your own services across a network boundary (microservices, internal APIs). Define a port at the seam; the deep module owns the logic; transport is an injected adapter. Production = HTTP/gRPC/queue adapter; tests = in-memory adapter. Recommendation shape: *"Define a port, implement an HTTP adapter for prod and an in-memory adapter for tests, so the logic lives in one deep module even though it's deployed across a network."*
4. **True external.** Third-party services you don't control (Stripe, Twilio, SendGrid). The deepened module takes the external dep as an injected port; tests use a mock adapter. See [mock-at-boundaries](mock-at-boundaries.md).

## Seam discipline
- **One adapter = hypothetical seam. Two adapters = real seam.** Don't introduce a port unless ≥2 adapters are justified (typically prod + test). A single-adapter "seam" is just indirection.
- **Internal vs external seams.** A deep module can have internal seams (private to its implementation, used by its own tests) *and* the external seam at its interface. Don't expose internal seams through the interface just because tests use them.
- **Replace, don't layer.** Old shallow-module unit tests become waste once tests at the deepened interface exist — delete them. The interface is the test surface.

## Caveats
- Local-substitutable looks like an in-memory adapter but lives one layer in — the substitute *replaces the dependency*, not the deepened module's interface.
- "Remote but owned" tempts you to expose the network boundary at the deep module's interface. Resist — the network is an adapter detail, not part of the contract.

## Related
- [deep-modules](deep-modules.md) — the architecture vocabulary this builds on
- [mock-at-boundaries](mock-at-boundaries.md) — category 4 in detail
- [integration-testing-bias](integration-testing-bias.md) — testing through the deepened interface
- [design-it-twice](design-it-twice.md) — sub-agent 4 specializes in cross-seam designs
