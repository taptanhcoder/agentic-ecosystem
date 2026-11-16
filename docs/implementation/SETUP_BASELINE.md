# Setup baseline — P0 / FE-00, Master Plan v2

Audit date: 2026-11-13. Actual workspace: `/mnt/d/ai_agent` (`D:\ai_agent`).
Master Plan v2 supersedes v1; Frontend Architecture v3.2 adds WS-08. The user
requested source alignment; the documents are design inputs, not evidence of
completed implementations or authorization to execute the entire roadmap.

## Preservation and inventory

- Git branch `main`, no commits, no remotes. Existing files were untracked before
  this change. No git init, reset, clean, install or environment recreation run.
- No applicable AGENTS.md found. Existing files were inspected before edits;
  pre-edit copies of modified files are at `/tmp/eco-before-v2` for this session.
- Existing `.venv`, uv.lock, Cargo.lock, manifests and language source retained.
- `domains/research`: Python package, domain/application boundary, document port,
  one fake-adapter unit test. No HTTP server, business entities, worker or queue.
- `apps/gateway-go`: standard-library build scaffold, no proxy or behavioral tests.
- `engines/document-rs`: empty optional core crate, no parser, FFI or parity tests.
- `contracts/openapi/research.v1.json`: draft liveness contract only; no live API.
- No frontend app, package.json, JS lock, node_modules or frontend build existed.
- No deployment manifests, database migrations, model config or telemetry runtime.
  Docker daemon is unavailable; no volumes or secrets were touched.

## Toolchains and rerun evidence

| Check | Actual result |
| --- | --- |
| Python | 3.12.3; existing `.venv` reused |
| `python3 -m unittest discover -s tests/architecture -v` | PASS: 7 tests |
| `.venv/bin/python -m unittest discover -s domains/research/tests -v` | PASS: 1 fake-adapter test |
| `.venv/bin/python scripts/validate_openapi.py` | PASS |
| uv 0.9.10 under `/tmp`, `uv lock --check` | PASS: resolved 21 packages, no lock change |
| Windows Go 1.26.10, `go test ./...` and `go vet ./...` | PASS; no Go test files |
| Rust 1.85.0 under `/tmp`, `cargo check --locked --workspace` | PASS |
| `cargo test --locked --workspace` | FAIL: missing linker `cc`; no test execution |
| `cargo fmt --all -- --check` | PASS |
| Windows `C:\Program Files\nodejs\node.exe --version` | v22.12.0; Linux `node` absent from PATH |
| npm/pnpm | Windows launchers found; versions/install/build not verified |
| `docker info --format '{{.ServerVersion}}'` | FAIL: `/var/run/docker.sock` unavailable |
| CI YAML parse | PASS: six jobs; architecture job independent of path filters |
| Hosted CI / client generation / browser E2E | NOT RUN; no remote or frontend yet |

Go commands use `'/mnt/c/Program Files/Go/bin/go.exe' -C D:/ai_agent/apps/gateway-go`.
Rust commands use `RUSTUP_HOME=/tmp/eco-rustup`, `CARGO_HOME=/tmp/eco-cargo` and
`/tmp/eco-cargo/bin` on PATH, with `--manifest-path engines/document-rs/Cargo.toml`.
uv uses `/tmp/uv-x86_64-unknown-linux-gnu/uv`, cache `/tmp/eco-uv-cache`.
These are session tools, not claims of permanent Linux toolchain installation.

## Applied reconciliation

1. Stored exact v2/v3.2 source documents in docs/plans and docs/architecture;
   retained historical ECO-00 evidence unchanged.
2. Added ADR 0002 covering FE-001 through FE-004. Auth and frontend dependency
   choices remain pending verification rather than being invented by the audit.
3. Retained existing JSON OpenAPI source; added duplicate-source guard. No YAML
   copy, generated SDK, handwritten client DTOs or fake API endpoints were added.
4. Added repository-wide Python-to-frontend import guard. Existing inner-layer
   checks remain in place. Static checks do not detect arbitrary dynamic imports.
5. Split architecture into an always-running CI job so changes in future frontend
   or contract paths cannot silently bypass existing backend boundary checks.
   Frontend feature-import checks and SDK drift checks await FE-01/02.
6. Added frontend generated-output ignore rules, README/local guidance and an
   implementation map. No speculative shared frontend packages or empty apps.

## Status and next work

P0 inventory and FE-00 audit recorded. ECO-00/G0 acceptance remains incomplete:
resolve the C linker and verify hosted CI. ARCH-01 is partial until actual frontend
boundaries are enforced. G0 now refers to v2 setup acceptance, not v1 feasibility.
No G1–G5 gate has passed.

Next: resolve baseline gaps, run missing RD-00 feasibility probes, define RD-01
run/error/status/event contracts, then FE-01/02 shell + generated client and
OPS-00 correlation. Backend and frontend progress independently toward the durable
fake-artifact demonstration described in ROADMAP.md. Full Research remains out
of scope for this alignment change.
