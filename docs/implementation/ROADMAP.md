# Active implementation map — Master Plan v2 / Frontend v3.2

The v2 master plan supersedes v1. Runtime v3.1 ownership remains unchanged.
Attached plans describe target work; evidence below determines actual completion.

| Item | Current status | Next concrete deliverable |
| --- | --- | --- |
| P0 / ECO-00 audit | Inventory recorded; acceptance gaps remain | Resolve Rust linker, run hosted CI |
| FE-00 | Audit complete: no frontend exists | Select/test React toolchain in FE-01 |
| ARCH-01 | Backend boundary checks + frontend ADR in place; FE enforcement pending | TS feature import rules with actual frontend |
| RD-00 | Not implemented | Missing MAF/model/provider/pgvector/parser feasibility probes |
| RD-01 | Not implemented; OpenAPI currently liveness only | Run/error/status DTOs, fake executor, standalone API contract tests |
| FE-01/02 | Not implemented | React shell, mocks, generated client from existing OpenAPI JSON |
| OPS-00 | Not implemented | Trace correlation and redaction baseline |
| RD-02 / CAP-00 / ORCH-00 | Not implemented | Atomic jobs, leases/fencing, bounded admission, cancellation/SSE |
| FE-03/04 | Not implemented | Submit/status, replay/reconnect and polling UX |
| RD-03–06 / FE-05 | Not implemented | Real sources, evidence, citations and report viewer |

First integrated runtime demonstration: browser → typed client → Python API →
durable PostgreSQL job → worker → persisted fake artifact → SSE/poll → report
viewer with correlated trace. A mock UI can precede this, but cannot establish
R0 or durability. Go/Rust must not block standalone Research.

G0 in v2 means existing setup accepted; it is not the v1 G0 feasibility label.
No gate is passed merely by importing the plan. Keep docs/plans/ECO-00.md as a
historical evidence record; use SETUP_BASELINE.md for this reconciliation.
