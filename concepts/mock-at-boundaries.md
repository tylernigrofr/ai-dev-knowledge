---
title: Mock at system boundaries only (SDK-style interfaces)
type: principle
phase: [implementation]
tags: [testing, mocking, boundaries, sdk, dependency-injection]
sources:
  - sources/repos/pocock-skills.md
status: stable
superseded_by: null
last_reviewed: 2026-05-06
---

## Summary
Mock only at system boundaries (external APIs, time, randomness, sometimes DB/FS) — never your own classes or internal collaborators — and design those boundary interfaces as SDK-style functions (one per operation) rather than a single generic fetcher.

## Why it matters
Mocking internal collaborators is the dominant tell of bad tests: the test breaks the moment internals are refactored even when behaviour hasn't changed, and the assertions ("was `paymentService.process` called with X?") describe how the code is wired rather than what it does. The fix has two parts. First, draw the mock line at things you don't control. Second, make those external boundaries injectable and *granular* — a `getUser`/`getOrders`/`createOrder` SDK is mockable per call site without conditional logic, while a generic `api.fetch(endpoint, opts)` forces every test to recreate routing logic inside the mock.

## How to apply
- **Mock**: external APIs (Stripe, Twilio, SendGrid), time/randomness, sometimes filesystem. Prefer a real test DB over mocks.
- **Don't mock**: your own functions/classes/modules, internal collaborators, anything you can refactor.
- **Inject dependencies** — pass payment client / clock / fs into the function under test rather than constructing them inside.
- **SDK-style boundary interfaces** — one named function per external operation, each independently mockable, returning one specific shape. No conditional dispatch in mocks.
- If you find yourself writing `if (endpoint === '/users')` inside a mock, the boundary interface is wrong, not the test.

## Caveats
- A mocked boundary still needs a contract test against the real service occasionally — pure mocks drift from reality.
- For genuinely owned dependencies across a network seam, prefer a port + in-memory adapter over a mock (see [dependency-categories](dependency-categories.md)).

## Related
- [integration-testing-bias](integration-testing-bias.md) — what to test through instead of mocking internals
- [dependency-categories](dependency-categories.md) — when to use port+adapter vs mock
- [deep-modules](deep-modules.md) — boundary mocks live at the seam
- [tdd-for-afk](tdd-for-afk.md) — TDD with the right mock discipline
