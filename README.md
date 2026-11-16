# Agentic Ecosystem

ECO-00 foundation, reconciled with Master Plan v2 and Frontend Architecture v3.2.
Research-first polyglot modular monorepo; setup is preserved, not recreated.
**No Research API, worker, durable jobs or production parser exists yet.**

- `domains/research`: independent Python package; domain/application boundary and document port.
- `apps/gateway-go`: optional thin-gateway build scaffold, no HTTP listener.
- `engines/document-rs`: optional empty deterministic-engine crate, no FFI.
- `contracts/openapi/research.v1.json`: authoritative draft HTTP contract.
- `tests/architecture`: executable import-boundary checks.
- `docs/adr`: ownership decisions; `docs/runbooks/LOCAL.md`: local checks.

Python owns Research lifecycle and future MAF integration. Go must not own Research
state. Rust is optional behind a port with a Python fallback. PostgreSQL/pgvector
and OpenTelemetry are selected architecture targets, not verified integrations.
No Global Orchestrator is included.

See [local guide](docs/runbooks/LOCAL.md), [ADR](docs/adr/0001-architecture-boundaries.md)
and [ECO-00 evidence](docs/plans/ECO-00.md).

## Active plan and frontend

[Master Plan v2](docs/plans/AGENTIC_ECOSYSTEM_MASTER_IMPLEMENTATION_PLAN_V2.md)
supersedes v1; [Frontend v3.2](docs/architecture/AGENTIC_ECOSYSTEM_FRONTEND_ARCHITECTURE_V3_2.md)
adds the TypeScript/React workstream. No frontend workspace exists yet.
The planned `apps/web` builds independently and consumes the public OpenAPI
through a generated client; Python remains usable without the browser or gateway.
Shared frontend packages are deferred until two consumers justify them.

See [current baseline](docs/implementation/SETUP_BASELINE.md),
[implementation map](docs/implementation/ROADMAP.md) and
[frontend ADR](docs/adr/0002-frontend-boundaries.md). The existing JSON contract
remains authoritative; no duplicate YAML contract or speculative dependencies.

## Git workflow

See [solo Git workflow](docs/runbooks/GIT.md) for branches, commits, PRs, and releases.
