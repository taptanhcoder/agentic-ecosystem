# ADR 0001 — Research-first polyglot boundaries

Status: Accepted for ECO-00, 2026-11-13.

Python owns Research API, canonical state, durable job manager and worker.
MAF is an outbound workflow adapter, never the owner of business state.
PostgreSQL/pgvector is the future persistence source of truth. These integrations
are not installed or proven in ECO-00; pin tested versions in RD-00.

Domain imports only standard library and domain modules. Application imports
standard library, application ports and domain. Agentic code uses these contracts;
adapters implement them; bootstrap alone wires concrete implementations.
No framework, ORM or model SDK imports in domain/application.

Go is an optional HTTP gateway consuming the public OpenAPI contract, never a
second scheduler or Research database client. No Global Orchestrator until a
concrete second domain and use case justify a new ADR.

Rust handles deterministic documents through DocumentProcessor. Keep a Python
fallback; no Research table writes. Native build must not block Python install.
No parser implementation or FFI bridge is claimed by this scaffold.

contracts/openapi/research.v1.json is the only public HTTP source of truth (JSON
is an OpenAPI serialization). ECO-00 defines liveness only as a future contract;
no HTTP server or run submission is implemented. Extend in RD-01; do not pretend
in-memory acceptance is durable.

OpenTelemetry uses W3C HTTP context and persisted queue context/span links.
Metadata only by default; no prompts, papers, secrets or high-cardinality metric
labels. SDK/Collector wiring starts in OPS-00; no operational tracing claim yet.

Research must install/test/run independently of Go and Rust. Architectural tests
and separate CI jobs enforce the initial import/build boundary. Dynamic imports,
future cross-domain SQL and real runtime equivalence need additional gates.

## v2 / frontend amendment

ADR 0002 adds the TypeScript frontend boundary and preserves all ownership rules
above. Research must also install/test/run without the frontend or Node runtime.
See docs/implementation/SETUP_BASELINE.md for current evidence; the ECO-00 report
is historical and is not a declaration that v2 release gates have passed.
