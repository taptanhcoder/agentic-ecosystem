# ENGINEER-LED BUILD ROADMAP — Agentic AI Ecosystem

**Version:** 1.0 — 2026-11-16
**Status:** PROPOSED ENGINEERING PLAN — NOT EXECUTION EVIDENCE
**Authoring model:** Solo Engineer owns ALL source implementation; AI acts as teacher, research assistant, reviewer, auditor and verifier by request only.
**Repository:** taptanhcoder/agentic-ecosystem
**Base:** feature branches from dev; PR to dev; milestone promotion dev → main (ADR-0004).
**Languages:** Python, Go, Rust. Frontend framework is OPEN pending ADR; do not silently mandate TypeScript.
**Release roadmap:** R0 Durable Foundation → R1 Useful Research → R2 Advanced/Ecosystem Readiness.

> IMPORTANT: This document is a development contract and a learning roadmap, not permission for any AI agent to implement the described code. The human engineer writes and runs application code, chooses dependencies, makes architecture decisions and approves merges. AI remains read-only unless the owner gives specific, scoped authorization.

## 0. Verified starting point and scope constraints

Verified on the existing GitHub repo on 2026-11-16:
- Python research package, application document-processing Protocol and unit/architecture tests exist as scaffolding.
- Draft OpenAPI JSON exposes /health/live but has no running Research API.
- Go gateway main compiles as scaffold; no HTTP router/proxy; Rust document-core is empty.
- No Research persistence, durable queue, Worker, MAF execution, citation/evidence pipeline, memory, frontend app or production deployment has been verified.
- Existing CI, PR workflow, ops docs and two permanent branches exist; setup should be audited and *reused*, not recreated.
- Environment-specific gaps recorded in docs/SETUP_BASELINE.md (missing uv/cargo in old WSL audit) must be rechecked on current machine, never assumed unchanged.
- docs/implementation/ROADMAP.md and an older frontend ADR mention React/TypeScript, but owner-selected three-language policy leaves the frontend choice OPEN. Resolve with ADR before frontend build.
- Research must run independently of optional Go Gateway and Rust engine. There is no Global Orchestrator in Release 1.

Evidence authority: actual source + test logs > approved ADR/contracts > latest PROJECT_STATUS + SETUP_BASELINE > planning docs. Do not rewrite history or fabricate completed gates.

## 1. Engineer-led collaboration agreement

### 1.1 Human responsibilities

The human engineer must:
1. Write a short design before implementation, including domain objects, data flow, APIs and expected errors.
2. Write ALL application source code and initial tests manually, reviewing all dependencies and SDK behaviors.
3. Execute build/tests locally; collect objective evidence from console/CI/traces.
4. Diagnose a failing case first and formulate a falsifiable hypothesis before seeking AI assistance.
5. Decide on technical choices by comparing alternatives and accepting/rejecting ADRs.
6. Make Git commits, PR decisions, production approvals and deployments personally.

### 1.2 AI permissions by default

Allowed (READ-ONLY unless scoped): explain theory, read existing source/diffs/logs, ask design questions, identify invariants, compare alternatives, critique code, suggest minimal pseudocode, propose additional test cases, analyze performance logs and review ADRs.

Not allowed by default: generating entire feature/module files, bulk refactoring, editing local or remote code, installing or adding dependencies, applying patches, creating commits/PRs or deploying. A specific request to implement a narrowly scoped correction overrides read-only only for that correction and never grants general autonomy.

Preferred escalation: Hint 1 (concept) → Hint 2 (design) → Hint 3 (pseudocode) → Hint 4 (targeted code correction, only explicitly requested). AI should not paste complete solutions before the engineer tries.

### 1.3 Required learning artifact per ticket

Every ticket produces: (a) design note, (b) authored code + tests, (c) execution evidence, (d) review findings, (e) engineering journal entry. The engineer explains why the implementation meets the invariants without relying on an AI-generated summary.

## 2. Delivery methodology

Small, evidence-driven, vertical increments. Each PR should be one reviewable responsibility; typically 1–3 focused engineering sessions, but time is estimated after technical reconnaissance. Never mix experiments with production code until approved.

For every ticket follow:

    Inspect current implementation → Define behavior + constraints
    → Compare design options → Write contracts/tests
    → Implement manually → Run tests → Inspect traces/perf
    → Ask AI to audit → Fix manually → Record evidence + ADR
    → PR to dev → Verify hosted CI → Merge

No status is inferred from a README or passing mock alone. Use four states:
- PROPOSED: design/plan only
- IMPLEMENTED_UNVERIFIED: source exists; required validation incomplete
- VERIFIED: required tests/evidence executed successfully
- BLOCKED: prerequisite/technical uncertainty prevents acceptance

## 3. Architecture boundaries

| Boundary | Source owner | Must NOT depend on |
| --- | --- | --- |
| Python Research Domain Core | domains/research/src/agentic_research/domain | FastAPI, SQLAlchemy, MAF, PostgreSQL, network/tool adapters |
| Python Application | application | HTTP framework, concrete ORM, concrete LLM SDK |
| Python Adapters | adapters (create when needed) | Cross-domain database access or bypassed authorization |
| Python Agent Runtime | agentic (create when validated) | Direct global task state; duplicate business lifecycle |
| Go Gateway | apps/gateway-go | Research-owned database writes or MAF internals |
| Rust Processing | engines/document-rs | Research orchestration or direct Research database writes |
| Frontend | independent application, technology OPEN | Research ORM/MAF/internal domain entities |
| Contracts | contracts/openapi/research.v1.json | Implementation-specific serialized objects |

Owners and public contracts are stable goals; directory additions are done only when a ticket needs them.

## 4. Stages / checkpoints

| Stage | Objective | Human source deliverable | Quality gate | Release |
| --- | --- | --- | --- | --- |
| S0 | Verify environment and technological hypotheses | isolated probes, reproducible baseline | G0 Technical Feasibility | pre-R0 |
| S1 | Public contracts + pure domain core | contracts, entities, state machine | G1 Domain & Contract Correctness | R0 |
| S2 | Standalone HTTP API and use cases | API, DI, fake executor, error mapping | G2A API Integrity | R0 |
| S3 | Data durability and worker execution | migrations, job runner, idempotency, fencing | G2B Durable Vertical Slice | R0 |
| S4 | Source/discovery/document integrity | adapters, normalized documents, source/version registry | G3A Source Integrity | R1 |
| S5 | Bounded Research Agent runtime | model/tool/context/MAF adapters, trace | G3B Agent Reliability | R1 |
| S6 | Evidence-driven synthesis and reporting | claims, citation validation, reports | G3C Research Quality | R1 |
| S7 | Independent UX application | Frontend ADR, workspace, progress/report UI | G4 Usable Product | R1 |
| S8 | Memory + retrieval + continuation | PostgreSQL/pgvector search, scoped memories | G4B Continuity | R1/R2 |
| S9 | Deep/technical Research | advanced workflows, repo analysis | G4C Advanced Quality | R2 |
| S10 | Polyglot optimization and platform edge | optional Go gateway, Rust bounded engine | G5A Optional Component Parity | R2 |
| S11 | Load, security, recovery and ecosystem test | test harnesses, runbooks, second fake domain | G5 Release Readiness | R2 |

Parallelism: OTel trace identifiers, security, evaluation fixtures and capacity limits begin S1–S3 and mature throughout. S7 design mock can begin after S2 contracts. Rust benchmark can be investigated during S0, but its integration must not block R0/R1.

## 5. S0 — Technology/Environment Validation (research gate)

### S0.1 REC-01: re-audit current baseline, do not redo setup

**Inspect:** Git origin/main/dev status, branch history, clean worktree; Python/uv, Go, Rust/cargo/rustfmt, Docker/Compose; existing tests, workflows, lockfiles. Compare docs/SETUP_BASELINE.md as a historical snapshot. No destructive commands or framework installations without an approved need.

**Human task:** run read-only inventory and the existing test commands. Explicitly mark failing or skipped toolchains; do not modify production code to hide an environment error.

**AI review:** identify mismatches, missing verification, unsafe Git operations and minimal safe remediation options.

**Evidence:** docs/benchmarks/REC-01.md with actual versions, exact commands, runtime output, current commit and compatibility blockers.

**Gate:** local reproduction of available Foundation checks OR an evidence-backed blocked status and mitigation plan; do not label G0 passed when gaps remain.

### S0.2 TECH-01A: model/tool-use probe

**Design problem:** Does the selected local/remote model support structured output, tool calls, invalid schema recovery and bounded timeouts for Research? Local 8GB VRAM/16GB RAM baseline is a constraint to verify, not a performance claim.

**Human implementation:** isolated experiments/tech-01a; direct SDK call → allowlisted fake read-only tool → validated structured result. Measure cold/warm latency, token usage, RAM/VRAM, timeout and failure outcomes. No external write-capable tools.

**AI role:** evaluate test design, data leakage risks and the difference between supported API contracts and observed behavior. Do not write the probe unless explicitly asked.

**Gate:** model/provider matrix + reproducible tests/measurements; unsupported tool calling is a blocker or triggers a different model/adapter.

### S0.3 TECH-01B: choose ONE Python Agent Framework

Compare Microsoft Agent Framework (candidate), LangGraph (fallback), PydanticAI (optional comparative baseline) on exactly the SAME fixture, model and tool contract. Evaluate graph routing, checkpoint restore, tool call validation, tracing, cancellation and maintenance complexity.

**Important:** do NOT nest MAF and LangGraph in the same Research Run. Run isolated PoCs. A framework must provide meaningful value over direct SDK.

**Human task:** implement two minimal independent probes only as needed; draw lifecycle and identify ownership of durable state vs workflow checkpoint.

**AI role:** challenge selection matrix, check fair measurements, review framework leakage. Record ADR before adding dependency to Research runtime.

**Gate:** a candidate chosen conditionally, reproducible interruption/resume or explicit documented limitation; no speculative package install.

### S0.4 TECH-02: Go transport + frontend decision

Compare net/http/Chi and Encore for the actual thin Gateway needs. Compare Go templ+htmx and Rust Leptos (and any owner-approved exception) on Research UI requirements: streaming progress, evidence navigation, graph/trace visualization, accessibility, maintenance cost and deployment independence.

**Human task:** minimal UI/RPC exploratory prototype, not production app; note if JavaScript/TypeScript is necessary for advanced interactivity and seek explicit ADR. Primary three languages remain Python/Go/Rust.

**Gate:** separate Gateway ADR and Frontend ADR; frontend remains OPEN until validated.

### S0.5 TECH-03 / TECH-04 / TECH-05

- TECH-03 Rust document benchmark: baseline Python parser vs Rust-compatible candidate on the same English/Vietnamese PDFs, multi-column layouts/tables/scans; fidelity, offsets, page locator, memory, CPU.
- TECH-04 Postgres queue vs Temporal: choose based on real requirement (single Research domain, leases/recovery vs long-running global workflow); test duplicate processing and restarts before acceptance.
- TECH-05 security/licensing: dependency provenance, license, allowed scientific skills, prompt-injection and tool-policy threat analysis.

**S0 output:** APPROVED/REJECTED/DEFERRED ADR table, benchmark reproducibility sheet, compatibility matrix, pinned versions; source implementation is NOT licensed by a feature list alone.

## 6. S1 — Public contracts and pure Python Domain Core

### CON-01: Research public data contracts

Owner writes OpenAPI changes under contracts/openapi/research.v1.json; avoid duplicate YAML authority. Define:
- Research project/run identifiers, task type, input policy, budget and task idempotency key.
- Run states: QUEUED, RUNNING, PARTIAL, COMPLETED, FAILED, CANCEL_REQUESTED, CANCELLED (or proposed variant justified by ADR).
- Explicit 202 enqueue response, GET status, GET result, GET events/pagination, proper error envelope, version handling.
- Correlation ID, timestamps, retry/error categories, artifact identifiers.
- Access control assumptions by project, user and resource.

Design 4xx/5xx semantics and no-availability behavior (e.g. no sources) separately from infrastructure failure.

**Human code:** contract examples, schema validation, intentional compatibility rules.
**Tests:** valid/invalid payloads, unknown fields, idempotency key requirement, status serialization, OpenAPI checker.
**AI review:** schema evolution, version compatibility, leakage, naming drift.
**Exit:** contracts are testable without API implementation.

### RD-01: Domain entities and state machine

Human implements immutable or controlled ResearchTask, ResearchProject, ResearchRun, RunStatus and transition rules using Python stdlib/dataclasses/value objects. Keep domain import graph framework-free.

Practice: value vs entity identity; state transitions; invariants; explicit error types; time modeling; pure functions and unit-test isolation.

**Tests:** illegal transitions, terminal state immutability, repeated completion, retry-after-failure semantics, cancellation-before/after-start, malformed input, deterministic clock injection.
**AI review:** domain invariants, too much inheritance, accidental transport/db coupling.
**Exit:** state machine is fully covered by behavior-focused unit cases; architecture import checks remain green.

### RD-02: Application use cases and ports

Human creates command/query application services (CreateRun, GetRun, CancelRun, GetArtifact) with Protocol-based ports for repositories, job submission, clock, identifier, model/tool executor and event stream. First adapters are in-memory fakes.

**Tests:** idempotency service behavior, project boundary authorization, fake repository errors, cancellation paths, errors mapped to domain types.
**AI review:** dependency direction, transaction boundaries, test seam quality.
**Exit:** use cases run completely without HTTP, SQL, MAF, Go or Rust.

### G1 check

Human can explain domain vs application vs adapter; demonstrate ports being swapped without changing domain. CI architecture tests and contract tests pass; no unauthorized new framework.

## 7. S2 — Standalone API vertical slice

### API-01: Python HTTP API

After TECH ADR: create FastAPI candidate composition root, health liveness/readiness, typed request/response mapping, create/status/cancel/result endpoints backed by fake application adapters.

**Human code:** routing, dependency injection, error translation, auth context and request ID middleware. No Research business logic in HTTP routes.

**Tests:** 202 semantics, 400/401/403/404/409/422/429, error schema, authorization, timeouts, fake executor contract. Avoid falsely labeling 200 liveness as DB readiness.

### API-02: Integration + contract parity

Human writes provider/consumer contract tests verifying public OpenAPI vs real responses; supply fake event replay/poll UX test data. Add backwards-compatibility checks as consumers grow.

### OPS-00 (first slice): trace & logging

Introduce stable run_id, trace IDs and sanitized structured events at API + application boundaries. Observe fake runs locally; exporter failure must not fail business path.

**G2A:** POST → fake service → status/result + expected error and auth behavior; API runs standalone with no Go Gateway.

## 8. S3 — PostgreSQL + Durable Jobs (R0 milestone)

### DB-01: Research schema and migration

Human models ResearchRun, Job, JobAttempt/lease, Artifact, Outbox or event-log tables as justified. Review indexes, unique constraints, timestamps and per-project scopes. Keep ORM in persistence adapters; use Alembic only after ADR. No Go writes.

**Tests:** migrate on empty db; forward migration; unique idempotency constraint; transaction rollback; cross-project query protection.

### ORCH-01: atomic enqueue

Use one transaction to persist run+job+event; return HTTP 202 only after durable acceptance. Bounded queue/admission, per-project limits and explicit 429/503 on overload. Design queue depth and client retry contract.

**Tests:** DB unavailable, duplicate key, transaction rollback, queue full, negative workload.

### ORCH-02: leasing/worker

Human implements controlled worker startup, polling/notification, lease epoch/fencing, heartbeat, timeout, retry class, attempt limit, graceful shutdown and cancellation request. PostgreSQL SKIP LOCKED is a candidate but NOT exactly-once.

**Tests:** two workers race for same job, stale-worker commit rejected, worker death/recovery, retry backoff, poison job, cancel while running, graceful worker drain.

### ORCH-03: artifacts and event replay

Persist fake results as versioned artifacts. Poll/status and event replay have stable ordering and deduplication; SSE is added only if data semantics are sound.

**Tests:** duplicate delivery does not duplicate committed artifact, replay from last event, out-of-order event does not corrupt state.

### OBS-01: asynchronous trace correlation

API admission trace and long-running worker trace connected via propagated context/span link + run_id. Metrics: queue age, worker busy, attempts, failures, provider latency (when real provider exists). Never use high-cardinality user IDs as metric labels.

**G2B / R0:** REAL PostgreSQL API → durable job → worker → persisted fake artifact → recovery; all test evidence recorded. Go/Rust/Frontend still optional.

## 9. S4 — Research sources, document normalization and provenance

### SRC-01: source registry

Human models SourceIdentity (DOI/URL/repo commit where applicable), SourceVersion, fetched timestamp, content hash, license/rights, access status and evidence locator. Deduplication must not merge different versions silently.

**Tests:** DOI variants, same URL changed content, duplicate source identity, missing full text, revoked/unavailable source, conflicting metadata.

### SRC-02: discovery adapters

Integrate only authorized scholarly/GitHub metadata providers necessary for a working research task; bounded rate/concurrency, backoff/timeout, caching policy, normalization and provider status classification. NO unrestricted web crawling.

**Tests:** 429, timeout, partial provider metadata, 200 with logical failure, no source found, malformed UTF-8, URL safety.

### DOC-01: Python baseline document processor

Implement DocumentProcessorPort adapter; maintain text, sections, page/offset locators, parser version. Preserve original content hash and provenance. Rust not required yet.

**Tests:** small PDF fixtures, tables/multi-column/Unicode, scan limitations, large/invalid files, size limits, unsafe URLs; compare ground-truth extraction.

### DOC-02: deterministic chunking

Chunk using structure/section/offset-aware rules; preserve parent source/version. Study precision vs recall tradeoff and citation boundary drift. Persist derived chunks with parser/chunker versions.

**G3A:** every produced quote or chunk resolves to an existing source version and locator. Unretrievable text is not reported as verified evidence.

## 10. S5 — Agent Runtime: six engineering responsibilities

The six dimensions are responsibilities, NOT six services. Add one primary framework only after S0 approved ADR.

### MODEL-01: ModelPort

Human wraps model provider into a typed model interface with capabilities (structured output, tool calls, context window, token use) and limits. Instrument calls without collecting secrets. Distinguish provider transport failure from invalid LLM output.

### TOOL-01: Tool registry and safe execution

Allowlisted, typed read-only tools first; validate inputs/output; timeout/cancel, retry class, provider response validation; no auto-execution of downloaded skill scripts.

### PROMPT-01: versioned prompt profiles

Write small prompts with testable output contracts; record prompt version per run. Change prompts using regression tests, not intuition.

### CTX-01: bounded context builder

Select source passages based on relevance, recency, authority and token budget. Separate instructions from untrusted source content and require citation mapping.

### LOOP-01: bounded Research workflow

Human implements explicit PLAN → DISCOVER → READ → VALIDATE → SYNTHESIZE stages and conditional routing. Keep stop criteria, max iterations and source budget; detect futile loops. Research Application retains durable business state.

### HARNESS-01: execution policy & checkpoints

Build timeout, budget, cancellation, checkpoint/resume (if proven), step-state telemetry, retries and failure classification; no double scheduling with ORCH-02.

**Tests for all:** fake model, fake tools, schema failure, malicious source instruction, tool timeout, repeated loop, checkpoint mismatch, interrupted job, budget exhausted, partial result, provider unavailability.

**G3B:** identical fixtures produce valid state transitions with bounded work and explicit failures; technical success alone is not research quality.

## 11. S6 — Evidence, citations, reporting and evaluation

### EVD-01: claim-to-evidence graph

Human models Claim, EvidenceSpan, SourceVersion, Relationship/SupportStatus, conflict handling and verification status. Citation is a structured reference, not invented string in a generated report.

### EVD-02: verifier

Programmatic checks for citation existence, hash/version match, locator bounds, claim support where deterministically checkable; uncertain semantic support routes to quality evaluator/human review.

### REP-01: grounded report

Render structured sections with claim/evidence references, method, scope, limitations and missing sources. Versions report + prompt + model + source manifest for reproducibility.

### EVAL-01: golden corpus

Build 15–30 controlled Research Tasks initially (small acceptance dataset), labeled evidence/expected behavior, quality scoring and adversarial cases. Separate factual/citation correctness from latency and execution success. Target thresholds must be agreed after baseline, not invented as passed results.

**G3C:** a human can open a report, follow evidence to source/version/locator and identify unsupported claims. Record false citations, partials, token cost and regression changes.

## 12. S7 — Independent frontend and usable Research workspace

### FE-00: explicit UI choice ADR

The owner compares Go templ + htmx, Rust Leptos and an explicitly documented alternative only if justified. Prove streaming, accessible interactions, trace/evidence graph usability, browser security, responsive layout and long-term maintenance. No silently introduced mandatory TypeScript.

### FE-01: web shell/auth

Independent app/build and session boundary. No embedded MAF, ORM or Research business state.

### FE-02: research create/status

Typed OpenAPI integration, validation and idempotent submit UX; no double submissions.

### FE-03: progress timeline

SSE reconnect with event IDs + polling fallback; render queued/running/partial/completed/failed/cancelled accurately. Avoid displaying raw prompts/secrets in trace UI.

### FE-04: evidence/report viewer

Citation link opens source + locator, supports unavailable source states; report exports remain immutable/versioned.

**G4 / R1:** Engineer performs a user journey: create project, submit task, observe progress, inspect evidence, read report, resume after browser refresh. Research backend remains usable with web and Go gateway turned off.

## 13. S8 — Research memory, hybrid RAG and continuation

### MEM-01: memory taxonomy

Separate short-lived run state, project notes, persisted research artifacts, reusable reviewed findings and user preferences. Avoid storing raw model chain-of-thought, secrets or unverified claims as authoritative memory.

### RET-01: exact retrieval baseline

PostgreSQL source/citation filtering and lexical search; define evaluation set and Recall@K before adding approximate vector indices.

### RET-02: pgvector & hybrid

Embeddings as replaceable adapter; scope by project/access control, benchmark exact vs HNSW with recall/latency/memory trade-offs. No automatic index choice without measurements.

### MEM-02: continuation

Resume a research question using selected previous artifacts with evidence version/provenance, without mutating old reports. Study stale evidence and conflicting sources.

**G4B:** memory does not leak across unauthorized projects; continuation cites exact source/version.

## 14. S9 — Advanced Research (later)

### ADV-01: deep research

Iterative subquestions, search budgets, stopping conditions, partial result contracts, human review on high-risk steps and quality benchmarking against standard research.

### ADV-02: technical/GitHub research

Analyze repos using fixed commit/ref and allowed read-only APIs. Cite file path, line range and commit; do not silently execute repository code.

### ADV-03: comparative research

Provide structured comparison with normalized criteria, confidence, evidence and unresolved disagreements. No unsupported rankings.

**G4C:** higher quality/capability on benchmark sets with bounded cost and failure behavior; do not add agents merely to make a multi-agent demo.

## 15. S10 — Go/Rust integrations as optional measurable enhancements

### GO-01: Go Gateway

Only after standalone Python Research API is secure and stable: authn at edge, routing, rate limits, request IDs, traceparent, streaming pass-through, circuit breakers. Go must not store Research business lifecycle. Ensure direct-Research API still enforces authz.

**Tests:** direct vs gateway API equivalence, SSE, 429/backpressure, gateway down standalone fallback, auth bypass, identity forwarding.

### RUST-01: Rust core benchmark + adapter

Write deterministic processing against agreed typed DocumentProcessorPort. Compare output parity on same fixtures, page/offset fidelity and malformed input behavior. Use PyO3 if measured overhead/operability suits; otherwise consider process isolation. Rust failure must not corrupt Research state.

**Tests:** Rust/Python parity, invalid encoding, large documents, native crash strategy, memory/CPU, serialization overhead.

### ECO-01: fake second domain probe

Fake Coding Domain consumes Task/Artifact contracts without importing Research code or DB. Prove domain extensibility before implementing a real domain.

**G5A:** Go and Rust can be disabled without breaking standalone Research; versioned contracts enable an independent dummy consumer.

## 16. S11 — Security, load, chaos, supply chain and release

### SEC-01

Project-scoped authorization, threat model, SSRF, untrusted document/tool prompts, secrets hygiene, path traversal, audit trail, dependency/license review.

### REL-01

Crash tests: DB restart, worker killed at different states, provider 429, model timeout, collector outage, invalid PDF, duplicate enqueue, stale lease; verify no committed artifact loss.

### LOAD-01

Baseline fixed workloads: p50/p95/p99, jobs/hour, queue age, peak RAM/CPU/VRAM, API connections, provider token budgets. Increase concurrency until first bottleneck; document bottleneck and safe limits. Worker count is not LLM inference count.

### DEPLOY-01 (only after services exist)

Reproducible non-root images, build/scan/SBOM, staging integration, migrations/backups, restore drill, approved immutable digest, rollback. Existing deployment Compose is a TEMPLATE, not runnable release.

### DOC-01

Update status ledger, ADRs, runbooks and service diagrams. Provide minimal onboarding that starts real API/Worker, passes smoke and documents known limits.

**G5 / R2:** repeatable recovery and quality tests; security acceptance; staging evidence; user-approved release. Do not equate GitHub workflow YAML presence with a passed deployment.

## 17. Cross-cutting engineering exercises (the engineer writes these)

| Study axis | Exercise | Evidence |
| --- | --- | --- |
| Python OOP/DDD | entity/value objects, ports/protocols, dependency inversion | pure unit tests + dependency graph |
| Python async & concurrency | bounded jobs, cancellation, timeouts, resource pool | two-worker race and fault logs |
| Go interfaces/concurrency | context propagation, HTTP middleware, race detector | go test/go vet/race runs |
| Rust ownership | Result/Option, lifetimes, iterator parsing, error types | cargo test/clippy/fmt + malformed inputs |
| Databases | transactions, unique indexes, EXPLAIN, SKIP LOCKED | SQL plans and atomic failure tests |
| RAG | chunking, hybrid search, exact vs HNSW, grounding | recall/latency/faithfulness dataset |
| Agent loops | state, conditional routing, checkpoint, retries | explicit state diagrams and recovery tests |
| Observability | trace context across asynchronous boundaries | correlated trace/span screenshots or IDs |
| Security | SSRF, injection, access scope, skill allowlist | negative tests and threat model |
| Deployment | immutable images, migration, rollback | staged dry run and restore record |

Complete learning exercises only where they solve a real work package, not to create parallel tutorial frameworks.

## 18. Solo workload and scheduling

Use Kanban: BACKLOG → RESEARCH → DESIGN READY → IMPLEMENTING → LOCAL TESTED → AI REVIEW → FIX → CI VERIFIED → DONE.

Limit active application coding WIP to ONE ticket, plus at most one isolated technology research task. This minimizes context switching and half-finished code.

Weekly cadence (adjustable, not a deadline):
- Session A: read requirements, select ticket, state invariants, draw interfaces.
- Sessions B/C: human coding and test-first implementation.
- Session D: run negative/integration checks, inspect failures, AI audit.
- Session E: refactor manually, rerun all impacted tests, PR to dev, document lessons.

Estimates are sizing aids, not promised delivery dates. T-shirt sizing:
XS = documentation/small isolated test; S = pure domain behavior; M = adapter+integration; L = durability/multi-service. Split L tickets before coding.

The earlier 360–690h estimate is a planning heuristic, not a verified forecast; re-estimate after S0 and each completed stage. Track focus hours, rework causes and test execution time rather than celebrating lines of code.

## 19. Review scorecard (AI proposes, owner judges)

Score 0–4 (0 missing; 1 flawed; 2 partial; 3 acceptable; 4 excellent), and attach evidence:

- Correctness & domain invariants — weight 25%
- Architecture & contracts — weight 20%
- Test coverage of behavior/failure/recovery — weight 20%
- Security & resource/capacity limits — weight 15%
- Observability/debuggability — weight 10%
- Maintainability/readability — weight 10%

Hard-block a PR regardless of weighted score for credential leak, cross-project auth bypass, missing atomicity on durable jobs, unsupported evidence claims asserted as verified, destructive migration without recovery, cross-domain DB access or unapproved framework ownership conflict.

AI review must return severity, path:line, reproduction/evidence, root cause hypothesis, smallest suggested remedy, test to prove fix, and uncertainty. Do not silently change source files.

## 20. Gate and Definition of Done

A ticket is VERIFIED only if:
1. The actual source is human-authored/reviewed and scoped to approved design.
2. Required tests executed with exact commands and outcome; relevant GitHub CI evidence present.
3. Regression, negative paths and relevant fault cases are covered or explicitly blocked.
4. No unapproved architecture drift/dependency.
5. Source API/contract documentation updated as needed; configuration/secrets safe.
6. Design trade-off and rollback captured; no new unsolved high-severity issue.
7. The engineer can explain flow, invariants, complexity and alternative options.

Gate-specific evidence must be linked, not asserted. A failed tech PoC can close as verified research finding (REJECTED candidate), not a successful production capability.

## 21. First four coding cycles — actionable

### Cycle 1 — REC-01 + TECH-01A

- Recheck real Git/uv/Go/Rust/Docker state and hosted CI; do NOT rebuild setup.
- Read protocol in application/ports.py, Research OpenAPI draft, architecture tests.
- Write a one-page model/tool calling probe design, then manually implement direct SDK fake-tool experiment.
- Capture exact model/version/hardware/data/cost and tests.
- Ask AI to audit methods only; propose ADR.

### Cycle 2 — TECH-01B + CON-01

- Test Agent Runtime candidate isolated from Research source.
- Write a small state diagram and OpenAPI examples for Research runs; contract validation first.
- Review with AI for schema compatibility and checkpoint ownership.
- No agentic business implementation until G0 choice is defensible.

### Cycle 3 — RD-01 + RD-02

- Human implements pure ResearchRun state machine and use cases with fake adapters.
- Prove forbidden dependency imports fail architecture tests; document value/entity rules.
- AI audits correctness, invalid transitions and edge cases.

### Cycle 4 — API-01 + DB-01 design

- Implement a standalone API with fake repositories and contract tests.
- Design PostgreSQL transactions and schema; do not claim durability until S3 integration tests.
- Start cross-process trace plan and capacity constraints.
- Present end-to-end fake API demonstration and review before adding DB.

Do not launch deep research, frontend polish, Rust optimization or global orchestration as substitutes for the durable research foundation.

## 22. References, governance and update policy

Read root AGENTS.md, docs/PROJECT_STATUS.md, docs/SETUP_BASELINE.md, docs/adr/0001–0004, docs/ops, then this plan and current source. Older plans and frontend ADR are historical proposals where conflicting; log a superseding ADR before changing framework/frontend boundaries.

When completing a ticket, update docs/PROJECT_STATUS.md with verified status and evidence; if priorities/ownership change, update this plan through a reviewed docs PR. Never backdate tests or silently relabel a planned component implemented.

The plan is not the code; **the engineer owns the understanding and the implementation**.
