# First Engineering Mission — RES-CORE-01 (Human Code, Codex Review)

Status: HANDS-ON TASK BRIEF. No source code is authored by this file or by Codex.

## Objective

Implement the **ResearchRun Domain Model and explicit lifecycle state machine** without Agent Framework, HTTP, database or external services. Learn DDD entity/aggregate invariants, Python dataclasses/types and systematic failure testing.

## Baseline

Existing source: domains/research/src/agentic_research/domain/__init__.py (empty scaffold).
Existing application port: domains/research/src/agentic_research/application/ports.py describes DocumentProcessor only.
Existing architecture checks: tests/architecture/test_boundaries.py and tests/architecture/test_repository_contracts.py.
Draft API authority: contracts/openapi/research.v1.json currently /health/live only.
Do not create new repo, install new framework or overwrite scaffold.

## Design exercise (before code)

The engineer writes a one-page note answering:
1. Is ResearchRun an Entity/Aggregate Root? What invariant does it protect?
2. What is ResearchRunId identity versus ResearchGoal value object?
3. Which states are needed? Candidate QUEUED, RUNNING, PARTIAL, COMPLETED, FAILED, CANCEL_REQUESTED, CANCELLED.
4. Explicit transition table: what is legal/illegal? Are terminal statuses immutable? Can FAILED be retried within same Run or through an Attempt?
5. Cancellation-versus-completion race and how to serialize/resolve it (pure domain rule before DB concurrency).
6. How to inject clock and identifiers for deterministic tests?
7. Should the domain know anything about LLM, PostgreSQL, HTTP or KB? Answer should be NO.
8. What facts does it need to report to the application layer without leaking SDK/ORM objects?

## Expected human-owned implementation

Small, necessity-driven domain modules under domains/research/src/agentic_research/domain/ and corresponding tests under domains/research/tests/. Example names research_run.py, value_objects.py, errors.py, test_research_run.py are suggestions only. Do not create empty files to match a speculative directory diagram.

## Unit test design

- Construct valid run, reject invalid research goal/id.
- QUEUED → RUNNING → COMPLETED.
- QUEUED → CANCELLED (or cancellation requested policy, clearly defined).
- RUNNING → CANCEL_REQUESTED → CANCELLED; conflicting late completion.
- RUNNING → FAILED; no illegal transition from terminal states.
- Duplicate completion/cancel behavior is explicit, not accidental.
- Timestamps monotonic/injected; no sleep/time mocking hardwired to wall clock.
- Illegal transition returns domain error with safe diagnostics.
- Domain import/architecture tests remain green.

## Existing commands (verify availability before running)

From the repository root in WSL/Linux, and only if toolchain is installed:

    python3 -m unittest discover -s tests/architecture -v
    PYTHONPATH=domains/research/src python3 -m unittest discover -s domains/research/tests -v

If uv exists, follow docs/runbooks/LOCAL.md for locked checks. This text does not claim the commands have been executed today.

## Definition of Done

- Human can explain state machine, OOP tradeoffs, failure paths and how tests isolate the domain.
- Tests cover meaningful positive/negative cases, not only import/smoke.
- No domain→Framework/ORM/HTTP import; no cross-domain DB coupling.
- Clean reviewable diff, locally observed test output, Codex findings addressed by human.
- Branch from dev, PR into dev; no AI-generated source by default.

## Next ticket after verification

RES-APP-01: use cases + ports + in-memory/fake adapters. Only then HARNESS-01 (minimal necessary abstractions); Research API and durable jobs come later. Don't introduce KB or Second Brain code this week.
