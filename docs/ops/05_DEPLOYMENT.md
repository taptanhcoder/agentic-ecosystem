# 05 — Deployment Design: Local → Staging → Production

**Status: design/template only.** No Research runtime image or production deployment currently exists.

## Environment boundaries

| Environment | Purpose | Data | Trigger |
| --- | --- | --- | --- |
| local (WSL2 + Docker Desktop) | Development and bounded PoCs | synthetic/local | Manual |
| ci | Isolated contract/unit/integration test runners | synthetic/ephemeral | PR |
| staging (future) | Full vertical slice incl. DB, worker, traces, gateway | sanitized, independent | Manual after release candidate |
| production (future) | User-facing Research domain | protected persistent | Manual G5 + GitHub Environment approval |

## First deployable topology (single host; only when implementation exists)

    HTTPS reverse proxy / TLS termination
                   |
              Research API
                   |
           PostgreSQL (separate persistent volume/managed DB)
                   |
           Research Job Worker
                   |
        Provider models / scoped artifact storage
                   |
           OTel Collector / trace backend

Go Gateway is optional and must NOT be required for Research standalone. Rust parser can run in-process via an audited adapter or as a separately deployed service after benchmark. No Global Orchestrator.

## Deployment template

deployments/templates/compose.production.yaml defines Research API and Worker using externally built **immutable images**; it intentionally does not provision a database, model or secret manager. It is NOT runnable until images, API/Worker entrypoints, networks, persistence and credentials are implemented/tested.

Only loopback port binding is illustrated for API; place an authenticated TLS reverse proxy in front. Never expose PostgreSQL or OTLP publicly.

Test syntax without deploying:

    docker compose --env-file deployments/templates/production.validation.env -f deployments/templates/compose.production.yaml config --quiet

The validation env contains fake values for static checking ONLY. DO NOT use it to start containers.

## Production prerequisites

- Dockerfiles for Python API/Worker, package/build tests, non-root runtime and bounded resources.
- Image vulnerability scan + license review + SBOM and immutable release digests.
- Real Research API health probes: liveness ≠ readiness; worker lifecycle/readiness contract.
- PostgreSQL migrations with expand/contract, backup and restore drill; scoped DB roles.
- External secret injection; no raw secrets in compose YAML, Actions or GitHub issues.
- Bound job/model/parser concurrency, backpressure, observability and alerts.
- TLS/hostname/firewall and DNS validation; access control at Research API.
- Staging load/chaos/recovery tests and release approval.

## Staging promotion

Build once, promote the same digest from staging to production after results and owner approval; do not rebuild a different image under the same release tag. Record commit SHA, digests, migration version, config revision and observed health.

Sources: https://docs.docker.com/compose/how-tos/production/
