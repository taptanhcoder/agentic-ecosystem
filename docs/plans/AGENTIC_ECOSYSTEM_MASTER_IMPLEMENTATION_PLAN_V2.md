# AGENTIC ECOSYSTEM — MASTER IMPLEMENTATION PLAN v2.0

> **Document ID:** PLAN-ECO-002  
> **Date:** 2026-11-13  
> **Status:** Updated execution plan; setup **reported completed by project owner**, not independently verified  
> **Supersedes:** `AGENTIC_ECOSYSTEM_MASTER_IMPLEMENTATION_PLAN_V1.md`  
> **Architecture:** Polyglot v3.0 + Runtime v3.1 + Frontend v3.2  
> **First delivery:** independently usable RESEARCH domain, with ecosystem-grade contracts, orchestration, capacity and tracing.

## 0. Executive changes vs v1

1. **No bootstrap restart.** Existing repository, language toolchains, workspace and initial setup are assumed to be present as reported. The project must be audited before changing them; there is no new `git init`, `uv init` or blanket overwrite.
2. **Frontend is a separate workstream (WS-08), not a late UI ticket.** The Ecosystem Web App has its own build, design system, domain-feature boundaries, typed API client, E2E and browser observability.
3. **Preserve language ownership.** Python = Research business + MAF + jobs; Go = optional edge and future ecosystem coordination; Rust = deterministic processing; TypeScript = Frontend. No second business state machine in Go or browser.
4. **Delivery is vertical-slice and contract-first.** A mock-enabled Research UI and Python fake task may be demonstrated before full AI research quality, but cannot be called R0 research-complete.
5. **R0 and R1 quality gates remain intact.** Restore/cancel, citation provenance, overload, tracing and security are not deferred for UX polish.
6. **Only Research is a full domain in Release 1.** No Global Orchestrator, shared Knowledge domain, other Agents, micro-frontends or Kafka/Kubernetes.

## 1. Baseline audit — do not recreate setup

The owner confirmed setup has been done; no repository/commit/build logs were accessible in this planning session. Treat the rows below as **audit-to-accept**, not completed verification claims.

| Baseline item | Planning status | Evidence to capture | Action |
|---|---|---|---|
| Repository / Git history / chosen root | Owner reports setup completed | `git status`, branch/commit, directory tree | Preserve existing root; never re-init |
| Python package & toolchain | Unverified | `uv.lock`, `pyproject.toml`, Python version, test run | Audit versions / adapt only |
| Go module & gateway skeleton | Unverified | `go.mod`, `go test ./...`, actual location | Do not scaffold duplicate app |
| Rust cargo workspace | Unverified | `Cargo.lock`, `cargo test`, actual engine path | Keep existing crate layout |
| Frontend workspace | Unverified | `package.json`, workspace config, build/test, current framework | Integrate with existing FE, do not assume installed |
| Docker/Postgres/pgvector/model | Unverified | compose manifests, DB health, active migrations | Preserve volumes/secrets |
| OpenAPI/auth/tracing | Unverified | schema, existing middleware, collected trace | Extend where gaps exist |
| CI lint/tests | Unverified | workflow files + latest logs | Add only missing jobs |

**Audit output:** `docs/implementation/SETUP_BASELINE.md` records current paths, versions, passed checks, known gaps, and which backlog items truly already exist. Completed setup tasks are marked **DONE** only after repo evidence is recorded. This is a quick inventory, not a repeat of setup.

## 2. Release scope

### R0 — Working Research Vertical Slice

- Submit/inspect Research Run through Python API (optionally Go gateway), durable job acceptance and worker lifecycle.
- Source search, acquisition, parsing, evidence, verifiable citations, report and `PARTIAL` handling.
- Local OpenTelemetry and bounded resource controls; direct Research execution independent of gateway/frontend/Rust.
- **Frontend R0:** ecosystem shell, Research form, progress state/event stream, report with references; works against mock contract and real API. UI need not include full history/knowledge exploration yet.

### R1 — Research Domain independently usable

- Technical/GitHub/deep/comparison research and Research Memory/continuation.
- Research UI projects, sources/evidence explorer, history, artifact export, controlled settings.
- Go gateway auth/routing/streaming integration, Rust parser adapter (if benchmark justifies) or explicitly retained fallback.
- Browser-to-domain trace correlation, independent FE delivery, load/chaos/security/eval/restore tests.
- Mock second-domain contract probe (no full second domain).

## 3. Workstreams and ownership

| ID | Workstream | Primary work | Technology |
|---|---|---|---|
| WS-01 | Architecture & Contracts | Public contracts, ADRs, source dependency boundaries | OpenAPI, schemas, CI |
| WS-02 | Research Intelligence | Prompt/Context/Loop/Memory/Tools/Harness, MAF and skills | Python |
| WS-03 | Data & Retrieval | Research DB, provenance, RAG, artifacts | Postgres, pgvector |
| WS-04 | Execution & Capacity | Admission, durable queue, worker/LLM/provider limits | Python, Go |
| WS-05 | Native Processing | Parser parity, benchmark, optional acceleration | Rust, Python |
| WS-06 | Observability & Reliability | OTel, tracing, SLO/eval/security/recovery | All services |
| WS-07 | Platform Edge & Release | Go gateway, container release, runbooks | Go, Docker |
| **WS-08** | **Frontend Platform & UX** | Shell, design system, Research UI, API SDK, SSE and browser telemetry | **TypeScript / React** |

For a small team, roles may overlap, but **FE deliverables and gates are independent** of Research backend ownership.

## 4. Source boundaries

```text
agentic-ecosystem/
├── apps/
│   ├── web/                          # TS/React independent frontend app
│   │   └── src/{app,features/research,shared}/
│   └── gateway-go/                   # optional Go edge
├── packages/frontend/{ui,design-tokens,api-client,observability}/
├── contracts/openapi/research.v1.yaml
├── domains/research/                 # Python domain + API + worker + jobs
├── engines/document-rs/             # Rust deterministic processing
├── deployments/{frontend,gateway,research,observability}/
├── tests/{architecture,e2e,load,chaos,cross-language}/
└── docs/{adr,implementation,plans,runbooks}/
```

This is **target structure**; map onto the actual setup first. `apps/research-web` can remain a working app and need not be renamed. Do not create shared FE packages until at least two consumers justify extraction. Reference architecture: `AGENTIC_ECOSYSTEM_FRONTEND_ARCHITECTURE_V3_2.md`.

## 5. Delivery roadmap — updated milestones, not redo setup

A 2-week sprint remains a **planning unit**, not a deadline. Schedule starts from **post-setup audit**; delivery can overlap by owner. Gate status is unverified until actual evidence is collected.

| Phase | Back-end / AI lane | Frontend lane | Quality / operations lane | Exit evidence |
|---|---|---|---|---|
| **P0 — Setup audit** | Inventory Research code/DB/SDK, identify already implemented modules | Audit current frontend framework/workspace | Capture locks, builds, CI, ADR baselines | `SETUP_BASELINE.md`; no repeated bootstrap |
| **P1 — Contracts & vertical slice** | Domain DTOs, fake executor, Research API `POST/GET` | FE-01 shell, FE-02 generated SDK, mock-backed Run form | OPS-00 trace bootstrap, architecture and contract CI | Browser sends fake research, status via API |
| **P2 — Durable execution** | Research jobs, workers, leases, cancel, SSE stream | FE-03 task form + FE-04 progress timeline/replay/poll | CAP-00 quotas, ORCH-00 crash/reclaim | Browser → API → DB → worker, recoverable job |
| **P3 — Source intelligence** | Scholarly search, PDF parser, source identity/versioning | Sources list & document/excerpt preview | Parser fixtures/SSRF guards/OTel | Source/locator can be viewed end to end |
| **P4 — Research quality (R0)** | MAF research loop, skills, evidence, citation and report | FE-05 report + citations + evidence drilldown | G3 goldens, failed/partial/warnings UI tests | **R0 live Research demo** |
| **P5 — Advanced / continuity** | GitHub/deep/comparison, retrieval and memory | FE-06 history, continuation, research memory | Reindex/recovery/scope+auth regression | Run B reuses evidence from Run A |
| **P6 — Polyglot & UX hardening** | Gateway route, Rust optional adapter and parity | FE-07 browser OTel, permissions, accessibility, E2E | GO/RUST/OBS cross-service tests | Direct vs gateway equivalence; FE independent build |
| **P7 — Release** | Security/reliability fixes and deployment | Final FE release, docs, UX regression | Load/chaos/restore, mock-domain compatibility | **G5 Go/No-Go evidence pack** |

**Critical path:** setup audit → API+contract → durable job → source+evidence → verified report. FE proceeds in parallel against mocks, then against the real API. Go Gateway and Rust acceleration cannot block standalone Research R0.

## 6. Updated PR backlog

### 6.1 Setup and Architecture

| PR | Action after setup | Tests / completion |
|---|---|---|
| `ECO-00` | **Do not rerun.** Audit already-set-up workspace; mark DONE only after evidence | Build/test each present workspace; preserve history, volumes and secrets |
| `ARCH-01` | Document actual boundaries and FE app entry; add missing constraints | No feature→feature imports; no Research domain → FE imports |
| `RD-00` | Run only missing feasibility probes, not reinstall all toolchains | Pinned MAF/model/K-Dense/pgvector/provider smoke evidence |
| `RD-01` | Domain Core, public DTOs and fake Research executor | API/contract and architecture tests |
| `OPS-00` | OTel correlation baseline across available services | Trace linking and sensitive-field redaction |

### 6.2 Research Runtime and Reliability (retain v1 scope)

| PR | Scope | Must-pass acceptance |
|---|---|---|
| `RD-02` | DB migrations, job enqueue/outbox, API, progress SSE | 202 after atomic commit; idempotency, status/event replay |
| `CAP-00` | Queue and model/provider/parser quotas | 429/503 overload; no unbounded workers |
| `ORCH-00` | Lease, heartbeat, fencing, retry, cancel | Worker crash/recovery; no stale-worker overwrite |
| `RD-03` | Scholarly API search and canonical source identity | Source provenance/429/semantic errors |
| `RD-04` | Asset fetch, parse, version, chunks and locators | Source passage traceable to original version |
| `RD-05` | MAF, prompt/context/loop, curated skills & tool policies | Bounded loop, structured result, skill permissions |
| `ORCH-01` | Checkpoints and workflow stage event mapping | Resume tests, DB remains business source of truth |
| `RD-06` | Evidence, claim support, citations, report | Golden report checks and PARTIAL fallback |
| `RD-07` | GitHub/docs, deep and comparative research | Commit/path citations and bounded replan |
| `RD-08` | Memory/retrieval, continuation | Two-run recall and provenance |
| `GO-00` | Gateway auth/proxy/SSE/trace | Direct/gateway behavior parity |
| `RUST-00/01` | Deterministic parser prototype, optional Python adapter | Fixture parity/bench + safe fallback |
| `OBS-01` | Trace & metric dashboards, operational runbooks | Identify stalled jobs and bottlenecks |
| `EVAL-00` | Golden sets and evaluation harness | Reproducible source/citation/support metrics |
| `SEC-00` | Auth, tool/file/network permissions | No known critical access bypass or unauthorized tool in tests |
| `REL-00` | Release, backup, restore, load tests | Actual recovery/restore evidence |
| `ECO-01` | Fake second domain capability/contract probe | No Research internal changes to add another domain |

### 6.3 **NEW — Frontend PR lane (replaces monolithic `UI-00`)**

| PR | Deliverable | Implementation and tests |
|---|---|---|
| **FE-00 / Audit** | Reuse existing web setup | Inspect actual React/Next/Vite choice, workspace, lint, tests; **no reinitialization** |
| **FE-01** | Ecosystem App Shell | Navigation, auth-aware shell, layout, Research route; component tests and mock build |
| **FE-02** | Typed Research API Layer | OpenAPI generation/check, transport injection, normalized errors; mock contract tests |
| **FE-03** | Research Projects and Submit | Forms, idempotency key and server validation; E2E create/run flow |
| **FE-04** | Progress / SSE / Task Lifecycle | Reconnect, last event ID, dedupe, poll fallback; latency/disconnect E2E |
| **FE-05** | Reports / Sources / Evidence | Citations, verifiable source link/locator, artifact read; auth/error tests |
| **FE-06** | History / Memory / Continuation | Project scoping, search, continuation and PARTIAL history | 
| **FE-07** | Observability / Accessibility / FE Release | Browser tracing with redaction, component/E2E/accessibility + independent deploy |

**Rule:** No new frontend HTTP endpoint is hand-coded in components. All domain communication passes through the typed client/feature API layer. UI does not import Python schema internals or share database credentials.

## 7. Core API contracts and frontend-state agreement

| Public API | FE consumer | Semantics |
|---|---|---|
| `POST /api/v1/research/runs` | Submit flow | Idempotent enqueue; `202` only after durable commit |
| `GET /api/v1/research/runs/{id}` | Run page | Server-authoritative stage/status, progress |
| `GET /api/v1/research/runs/{id}/events` | SSE hook | Replayable event ID, bounded reconnect; polling fallback |
| `GET /api/v1/research/runs/{id}/result` | Report | Completed/partial/pending semantics explicit |
| `GET /api/v1/research/runs/{id}/sources` | Source viewer | Stable IDs, access status, locators |
| `GET /api/v1/research/runs/{id}/evidence` | Evidence viewer | Source version and passage linkage |
| `GET /api/v1/research/artifacts/{id}` | Export/view | Authorized, content type/disposition controlled |
| `POST /api/v1/research/memory/search` | Memory | Scoped retrieval, no cross-domain direct DB access |

**Frontend semantics:** browser disconnect != backend task cancel; `PARTIAL` is not `FAILED`; token/auth errors differ from backend overload; show actual statuses, not an invented browser-side state machine. If using `EventSource` for SSE, credential/CSRF policy must fit auth design; avoid long-lived access tokens in query strings.

## 8. Capacity, orchestration and tracing requirements (unchanged)

- Python accepts work only through bounded admission and durable DB job commit; worker pool has lease/heartbeat/retry/fencing, cancellation and backpressure.
- Go limits HTTP load and forwards trusted authenticated context; Python independently enforces resource authorization; no duplicate Research task state in Go.
- MAF orchestrates Research workflow and bounded Agent loops; checkpoint is NOT equivalent to Research database transaction.
- Rust is a deterministic processor behind `DocumentProcessorPort`, can be unavailable without taking down Core Research when Python fallback supported.
- OpenTelemetry is propagated across browser request, Go (if present), Python API, job enqueue, Worker and Agent/Tool spans; asynchronous job can use linked traces. Run IDs live in traces/logs, not high-cardinality metric labels.
- Browser telemetry has redaction. OTel outage cannot block Research task or frontend availability.

## 9. Verification and gates

| Gate | Scope / additions from v1 | Evidence |
|---|---|---|
| **G0 — Existing setup accepted** | User-reported done; verify existing app/toolchain/lock/CI without rebuild | `SETUP_BASELINE.md` and successful actual build/test commands |
| **G1 — Architecture** | Domain isolation, OpenAPI + generated client, FE feature boundaries | Backend/FE boundary tests and mock standalone UI |
| **G2 — Durable runtime** | API + Postgres worker + SSE, browser reconnect/polling | Kill/restart job and Browser E2E |
| **G3 — Research R0** | Source/evidence/report quality and user-readable report | Goldens + report viewer click-through |
| **G4 — Polyglot & FE** | Gateway/direct parity, parser parity, independent FE deploy, trace correlation | E2E trace and deployment checks |
| **G5 — R1 Release** | Security/load/restore/quality, FE accessibility and browser error UX | Release evidence pack and Go/No-Go |

Suggested baseline targets remain **provisional**, not measured: verified citation identity 100% for references labeled verified; claim-support ≥90% on a labeled set; recall@5 ≥85% if a representative dataset exists; zero lost committed artifacts in crash test; no unauthorized tool execution in security suite. API and frontend page/streaming performance goals must be established from an actual workload and hardware profile.

## 10. First implementation sequence **after setup**

1. **Inventory / gap audit** of working repo; write `SETUP_BASELINE.md`, mark truly completed items and paths. Do not recreate `.venv`, `node_modules`, containers, DB volumes, or toolchain setups.
2. **Lock contract**: Research OpenAPI v1 + error/status/event schema; ensure Python server tests and generated TS client compile (FE-02).
3. **Run two parallel vertical slices**: Backend RD-01→RD-02 (fake run, durable job, SSE) and Frontend FE-01→FE-04 (shell, mock flow, progress, reconnect).
4. **Integrate Browser → API** (direct in standalone profile, Go through gateway profile), verify identity, task idempotency, status, errors and trace.
5. **Upgrade fake to real Research**: RD-03→RD-06, verify citations with real sources, connect Report/Evidence UI (FE-05).
6. **Finish advanced/release**: RD-07/08, FE-06/07, Rust/Go integrations, load/chaos/restore, mock-domain probe.

The first post-setup integrated demo should be: **React Research form → typed client → Python Research API → durable Postgres job → worker → persisted fake artifact → SSE/reconnect or polling → React result viewer → correlated trace.** Upgrade the fake artifact to a real evidence-based report after the runtime slice passes.

## 11. PR DoR/DoD and release governance

- **Definition of Ready:** existing code reviewed for reuse, owner set, supported API/schema named, tests and failure states defined, dependencies confirmed.
- **Definition of Done:** actual lint/typecheck/tests/build evidence, backwards-compatible contracts, authorization, traces/redaction, schema/migration/rollback notes, reproducible E2E, changed docs and no newly introduced cross-domain imports.
- **Merge controls:** changes to `contracts/openapi/` require FE client compatibility; frontend routes/components cannot import backend implementation; changes to queue/leases need recovery tests; changes to evidence handling need citation/eval tests.
- **Go/No-Go:** release only when quality gates have actual test/build evidence. A 'setup complete' statement alone does not establish production readiness.

## 12. Source references / decision history

- `docs/PROJECT_DESCRIPTION.md` — RESEARCH domain scope.
- `docs/RESEARCH_DOMAIN_TECHNICAL_DESIGN.md` — Research schema/API/workflow.
- `docs/AGENTIC_ECOSYSTEM_POLYGLOT_SOURCE_ARCHITECTURE_V3.md` — Python/Go/Rust ownership.
- `docs/AGENTIC_ECOSYSTEM_RUNTIME_ARCHITECTURE_V3_1.md` — capacity/orchestration/OTel.
- `docs/AGENTIC_ECOSYSTEM_FRONTEND_ARCHITECTURE_V3_2.md` — frontend isolation.
- `docs/AGENTIC_ECOSYSTEM_MASTER_IMPLEMENTATION_PLAN_V1.md` — prior plan, superseded.

> **Operational note:** Actual source repository was not accessed in this planning turn. Treat progress classification as a reconciliation task; do not infer completed PRs merely from draft documents.
