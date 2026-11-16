# ADR 0002 — Frontend boundary and v2 plan reconciliation

Status: Accepted architecture, implementation pending; 2026-11-13.
Supersedes no runtime ownership decisions in ADR 0001.

## ADR-FE-001: Ecosystem application

One TypeScript/React Ecosystem Web App, with Research as the first feature.
Audit found no existing frontend; target path is apps/web. Framework, package
manager and exact dependency versions will be selected and verified in FE-01.
No empty workspace or pretend frontend build is added during this audit.
No microfrontends, second Research UI or global orchestrator.

app/bootstrap wires routes/providers/features. features/research owns presentation
and feature API hooks. Features cannot import each other's internals. Shared
primitives stay inside the app until two real consumers justify extraction.
The source tree in the design is a target, not a directory creation checklist.

## ADR-FE-002: Contract and transport

Retain contracts/openapi/research.v1.json as the single authoritative OpenAPI
source. JSON and YAML serialize the same OpenAPI model; do not create a second
research.v1.yaml just to match the design illustration. FE-02 generates the typed
client from this existing file and checks drift in CI. Generated code lives in
the app initially; no shared package before a second consumer exists.

Components call the feature API layer, never ad-hoc HTTP endpoints. Transport is
configurable for direct Python API or optional Go gateway. No Python/ORM imports,
DB credentials or backend workflow logic in browser code. Python installation
and tests never require Node, the frontend, Go or a native Rust build.

## ADR-FE-003: Authoritative state

Research run state belongs to Python. Browser renders server status, including
PARTIAL, cancellation requested and overload; it does not run another business
state machine. Event IDs support replay/deduplication, bounded reconnect and
poll fallback. A disconnected browser does not cancel a backend task.
An in-memory fake demo cannot claim durable acceptance or completed R0 research.

## ADR-FE-004: Authentication and telemetry

Auth/session mode remains open until the real API/transport slice; no cookie or
bearer scheme is assumed implemented. Direct Python mode must enforce server
identity, resource authorization and appropriate CORS/CSRF protections.
No long-lived tokens in URLs. Browser OTel is metadata-only and fails open for
telemetry outages; never record prompts, source text or secrets. Run IDs belong
in logs/traces, not metric labels.

## Enforcement and remaining work

Current CI protects Python domain/application imports, prohibits Python-to-web
imports throughout the package, and guards the single contract source. FE
import rules and generated-client compatibility require the actual TS workspace
and will ship with FE-01/02. These rules are accepted, not falsely marked tested.
