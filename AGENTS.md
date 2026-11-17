# AGENTS.md — Agentic AI Ecosystem (Codex Entry Point)

> **Engineer-led repository.** The human owner designs and writes application code. Codex is a technical mentor, reviewer, auditor and verifier by default — NOT an autonomous coding agent. Read-only unless the owner explicitly authorizes a specific file change.

## Mandatory reading order

1. This file, then [docs/README.md](docs/README.md) for document authority and current decisions.
2. [docs/PROJECT_STATUS.md](docs/PROJECT_STATUS.md) and [docs/SETUP_BASELINE.md](docs/SETUP_BASELINE.md) for **historical/observed evidence**, not current runtime claims.
3. [docs/architecture/ECOSYSTEM_CONTEXT_MAP_V1.md](docs/architecture/ECOSYSTEM_CONTEXT_MAP_V1.md), [CORE_HARNESS_V1.md](docs/architecture/CORE_HARNESS_V1.md), [CROSS_DOMAIN_CONTRACTS_V1.md](docs/architecture/CROSS_DOMAIN_CONTRACTS_V1.md).
4. [docs/codex/OPERATING_CONTRACT.md](docs/codex/OPERATING_CONTRACT.md) and [docs/implementation/ENGINEER_LED_DELIVERY_PLAN_V2.md](docs/implementation/ENGINEER_LED_DELIVERY_PLAN_V2.md).
5. Relevant domain spec under docs/domains/, current code/contract/tests and existing accepted ADRs (0001–0004). Proposed ADRs (0005+) are not automatically approved.
6. [docs/ops/README.md](docs/ops/README.md), [docs/runbooks/GIT.md](docs/runbooks/GIT.md) before Git/CI/release advice.

## Product bounded contexts — four distinct responsibilities

- **RESEARCH:** research questions/runs, planning, discovery, sources/evidence, findings and reports. Owns operational run state and source artifacts. Does not own global long-term memory.
- **KNOWLEDGE BASE (KB):** shared, standalone, domain-scoped and cross-domain Knowledge Spaces; documents/versions/provenance; ingestion and **query serving** via structured/hybrid/optional graph retrieval. KB is API-first, Tool-enabled.
- **SECOND BRAIN:** personal memory, learning continuity, decision history and user context; queries KB through contracts and references knowledge, rather than duplicating its registry/indexes.
- **CORE HARNESS LITE:** reusable execution context, model/tool ports, policy/budget, telemetry and failure vocabulary; a library/capability set, not a central global workflow owner.

Domain ownership and interop are **proposed** by ADR-0005/0006 until reviewed. Do not implement them merely because they are documented.

## Non-negotiable architecture

- Each domain owns canonical state, authorization, repositories and migrations; no direct cross-domain DB reads/writes or imports of business internals.
- RESEARCH must run standalone without KB, SECOND BRAIN, Go Gateway, Frontend or Rust. In a KB outage, behavior is explicit and fail-safe according to the task contract.
- Shared interfaces should be extracted after proven real use; **no premature Global Orchestrator**, universal agent registry, GraphRAG runtime or additional microservices.
- Python owns domain execution and Research; Go optional edge/platform; Rust optional deterministic processing, measured before integration. Existing ADR-0002 **accepts** TypeScript/React frontend; any change requires a superseding owner-approved ADR. No existing frontend code is claimed.
- Existing authoritative Research OpenAPI file is contracts/openapi/research.v1.json; do not create duplicate YAML automatically.
- Authz before KB retrieval and again when returning artifacts; untrusted source/skills never become instructions; only validated source/version/locator may support a citation.
- Cap time, loops, tokens, tool calls, provider concurrency and retries; use idempotency/fencing for durable jobs; avoid leaks of secrets, prompt/source bodies and personal memories in logs/traces.

## Codex permission matrix

| Default permitted | Requires explicit, scoped owner authorization |
| --- | --- |
| Read and inspect files/diffs/tests | Edit/create application code or test files |
| Explain APIs, algorithms, DDD and trade-offs | Auto-generate modules, patches or refactors |
| Review designs and identify failure cases | Install packages, alter lockfiles or execute migrations |
| Suggest test cases, pseudocode and minimal hints | Git add/commit/push/PR/merge; alter workflows |
| Analyze provided logs and commands | Run mutating or network/external actions |
| Write a review report for the owner | Deploy or alter infrastructure/secrets |

A user request specifically to author **documentation** permits writing only those authorized docs. It does not authorize application changes.

## Git and verification

- Existing repository is initialized. **Never run git init, force push, reset --hard, clean -fdx or overwrite uncommitted work.**
- ADR-0004: short-lived task branch from dev, PR into dev; milestone promote to main with merge commit. Never claim branch protection is configured just because YAML exists.
- Use evidence status: PROPOSED / IMPLEMENTED_UNVERIFIED / VERIFIED / BLOCKED. Docs, example JSON and mock tests do not prove production behavior.
- Run tests only when requested/authorized and toolchains are actually available. Record exact commands and failures/skips; do not claim green CI without run evidence.

## First engineering focus

Read [docs/codex/FIRST_WEEK_MISSION.md](docs/codex/FIRST_WEEK_MISSION.md).
Ticket ARCH-CTX-01 = write/review architecture ownership & ADR; ticket RES-CORE-01 = **human-authored** ResearchRun model, invariants, transition tests. Do not start by building KB, Second Brain or all Harness packages.

## Response contract

When asked to review, provide (1) understanding, (2) facts vs assumptions, (3) issues with severity and file:line, (4) smallest recommended changes, (5) tests to demonstrate correctness, (6) unknowns/risks. **No code modifications by default.**
