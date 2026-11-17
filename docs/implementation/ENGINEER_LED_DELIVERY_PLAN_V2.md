# Engineer-Led Build & Release Plan v2 — Four-Context Ecosystem

Version: 2.0 | Date: 2026-11-17 | Status: PROPOSED | Driver: Solo human engineer | Codex: reviewer/auditor by default.

## Strategy

**Design for four contexts → implement Research first, with minimum Harness mechanisms → make Research useful standalone → implement standalone KB query service → integrate Research↔KB → implement Second Brain → generalize proven shared Harness capabilities.**

Do not build all domains in parallel or block the first usable Research release on KB/GraphRAG/Second Brain. Shared architecture is early; actual shared implementation is late. RESEARCH and KB are independently deployable within their respective product scopes.

## Milestone release plan

| Milestone | Proposed version | Main deliverable | Concrete acceptance | Scope boundary |
| --- | --- | --- | --- | --- |
| M0 — Boundary decision | No runtime release | Approved ecosystem context map, contracts, ADRs and threat model | No overlapping state/DB owners; outage paths documented | Docs only |
| M1 — Research foundation | v0.1.0 internal | ResearchRun Domain + use cases/fakes + minimal execution policy + API + PostgreSQL durable Worker | API→atomic job→fake worker→persisted artifact; retries, cancel, lease/fencing and traces actually tested | KB/SB not needed |
| M2 — Useful Research | v0.2.0 alpha | Real source acquisition, bounded model/tool loop, evidence and grounded report | User question→verifiable source/version/locator→report; golden citation and no-support cases | Domain-local source handling, no full shared KB |
| M3 — Standalone KB | v0.3.0 alpha | KB Space/Document registry + ingestion + scoped Knowledge Query API + ContextBundle | KB starts without Research; authorized query/no-result/revocation tested | Hybrid/vector optional by evidence |
| M4 — Research + KB | v0.4.0 preview | Read-only KB tool/application adapter + approved Research publication | Publication idempotent, partial outage, permission/revocation and provenance tested | No SB required |
| M5 — Second Brain | v0.5.0 alpha | Personal memory/decisions/continuation, KB reference/query | Owner can inspect/approve/delete memories, scoped recall, knowledge refs | No automatic write-back to KB |
| M6 — Ecosystem integration | v1.0.0 candidate | Cross-domain tests, proven Harness extraction, security/recovery/load, docs/release automation | Trace/budget/auth/recovery and staging/rollback evidence; owner-approved release | No full Global Orchestrator |

Version numbers are **suggestions**, not tags, deployed versions or claims of existing implementation.

## Critical path / concurrency

M0 (conceptual decision) → Research Domain Core → Application use cases + fake adapters → minimal Harness mechanisms → API → durable job/worker → source/evidence/report → KB independent Query MVP → Research KB adapter/publication → Second Brain → ecosystem security/reliability gates.

Parallel possible: technology PoCs, frontend technology ADR and independent UX mocks, telemetry/security review, Rust parser benchmark. No feature should declare GATE PASSED from a diagram or mock.

## Numbered build tickets and explicit human ownership

| Order | Ticket | Human writes/designs | AI role | Evidence for closure |
| --- | --- | --- | --- | --- |
| 01 | ARCH-CTX-01 | Domain context map, boundaries/ADR + data ownership | Challenge cycles/ownership/conflicts | Owner accepted ADR; no code required |
| 02 | REC-01 | Re-audit current Git/uv/Go/Rust/Docker/CI locally | Review evidence/gaps | Exact commands/versions, known blockers |
| 03 | RES-CORE-01 | ResearchRun aggregate/IDs/status/invariants | Challenge DDD state model/test cases | Pure unit tests; forbidden imports absent |
| 04 | RES-APP-01 | Application Create/Cancel/Get use cases + Protocol/fakes | DI review, failure tests | All fake use-case tests independent of HTTP |
| 05 | HARNESS-01 | Minimal ModelPort/ToolPort/ExecutionPolicy/ExecutionContext when Research proves needed | Challenge premature abstraction | Contract tests; no extra scheduler |
| 06 | TECH-01 | Bounded model/framework PoC isolated from production | Review fair tests/security | ADR, model/tool behavior evidence |
| 07 | RES-API-01 | OpenAPI run lifecycle, HTTP mapping/auth/errors | Contract/negative review | API contract tests, fake executor |
| 08 | RES-JOB-01 | DB migrations, atomic enqueue, leases/fencing/worker/recovery | Transaction/concurrency audit | Two workers + crash recovery tests |
| 09 | RES-AGENT-01 | One bounded research workflow and tool registry | Prompt/context/loop critique | Budget, invalid output, timeout, cancellation |
| 10 | RES-DATA-01 | Sources, fetch, parser baseline, chunks and locators | Provenance/security audit | Versioning and invalid-source tests |
| 11 | RES-EVIDENCE-01 | Claim/evidence/report/version/citation checks | Faithfulness/eval design | Golden findings + false citation rejection |
| 12 | KB-CORE-01 | KnowledgeSpace/Document/Version, permissions | Aggregate review | Idempotency/version/ACL tests |
| 13 | KB-QUERY-01 | KB API, query scope, fake then real lexical/exact retriever | Security/port review | Standalone KB + scoped/no-result tests |
| 14 | KB-CONTEXT-01 | Source-backed ContextBundle | Token/citation audit | Budget/revoked-source tests |
| 15 | KB-INTEG-01 | Research KB read Tool/API adapter + publication outbox | Review event/timeout/races | Duplicate publish + outage tests |
| 16 | SB-CORE-01 | MemoryRecord, Decision, learning lifecycle | Privacy/governance review | Approval/revocation/version tests |
| 17 | SB-INTEG-01 | KB reference/Context adapter | Scope/cross-domain audit | Recall quality, cross-project tests |
| 18 | ECO-HARNESS-02 | Extract shared primitives only after second consumer | API/version compatibility review | Consumer parity, dependency fitness |
| 19 | ECO-REL-01 | Load/security/recovery/backup/staging | Audit release evidence | Actual metrics, restore, approval |

Workloads can be split into smaller PRs. No topological demand to add every described path now. Architecture docs may identify future contracts without implementing them.

## Four initial human coding cycles

### Cycle 0 — Architecture and environment
- Read AGENTS.md, status, existing ADRs and contracts, validate actual Git state.
- Author ARCH-CTX-01 design/decision: ownership, cross-domain data flows, failure isolation, acceptance.
- Inspect existing setup, run available tests and identify toolchain blockers, no rebootstrap.
- Codex: review owner-written ADR/context, identify contradictions, no edits.

### Cycle 1 — Pure Python Research Domain
- Human designs ResearchRun as aggregate root (or documents alternative), RunStatus transition table, ResearchGoal, errors and timestamps.
- Human writes domain Python code; no HTTP/LLM/ORM/Framework.
- Human writes tests: illegal transitions; terminal states; cancel before start; cancel-versus-completion race; idempotent repeat; invalid goal; clock injection.
- Codex: challenge invariants and propose negative cases; **no generated source**.

### Cycle 2 — Application + fake vertical slice
- Human writes CreateRun/GetRun/CancelRun use cases, repository/clock/execution ports, fake adapters; no DB yet.
- Verify dependency rule via existing tests/architecture. Codex reviews DI and transaction assumptions.

### Cycle 3 — Harness Lite + real API contract
- Based on proven Research seam, define bounded ExecutionContext/policy/tool model interfaces.
- Human extends existing **JSON** OpenAPI from /health/live toward run lifecycle and implements fake-backed standalone API after validation.
- Codex reviews HTTP error mapping/auth, tests and controller-to-domain leakage.
- Real durability is the **next** milestone, not inferred from in-memory fake.

## First-week plan (adaptive)

| Day | Human activity | Expected artifact / gate |
| --- | --- | --- |
| Day 1 | Context Map / ADR; reconcile old ownership; inspect repo | Proposed design and owner review |
| Day 2 | State model, transition table and value objects | Design + test matrix |
| Day 3 | Human code ResearchRun transitions | Source diff without framework import |
| Day 4 | Human code transition/error/failure tests | Exact unit output |
| Day 5 | Application service/ports design | Use-case diagram; fake adapter contracts |
| Day 6 | Human code fake vertical slice and use-case tests | Standalone domain/app tests |
| Day 7 | Review/refactor/CI evidence and PR into dev | Scoped PR; reviewer report |

Days are a planning sequence, not a completion guarantee. If requirements need more study, keep the engineering gate.

## Acceptance / quality gates

Every ticket needs:
- Explicit input/output, constraints, non-goals, error and rollback semantics.
- Human-authored source/tests (if any) and reasoning that the human can explain.
- Exact executed test commands and outcomes. Mark skipped as NOT RUN.
- Domain and security boundary tests; negative cases; failures/recovery where relevant.
- Minimal, reviewable branch from dev with PR to dev; proper version/compatibility notes.
- Updated evidence ledger only with observed facts; no fake implementation status.

Hard blockers: credentials leak, unauthorized cross-space retrieval, cross-domain SQL/business import, job data loss, stale worker overwrite, fabricated evidence/citation, unapproved autonomous code/deploy action and undocumented data migration.

## Quality axes

Correctness/invariants (25%), architecture/contracts (20%), behavior/failure tests (20%), security/capacity (15%), observability (10%), maintainability (10%). Ratings are aids, never substitutes for blocking defect rules.

## Prohibited premature commitments

- No second brain or KB implementation in M1.
- No global orchestrator/multi-framework execution engine in M1–M2.
- No mandatory Rust integration or Go Gateway for standalone Research.
- No default GraphRAG/graph DB until measured.
- No broad docs→source refactor to match target directory sketches.
- No frontend framework changes based solely on a proposed future plan.

## Open choices / ADRs

Research framework model/profile, local toolchain readiness, frontend strategy conflict (accepted ADR-0002 vs later OPEN recommendation), API auth, KB graph approach, SB privacy/retention, deployment topology, multi-domain scheduler requirements. Record ADR/benchmark before irreversible implementation.

See ../codex/FIRST_WEEK_MISSION.md for immediate starting ticket.
