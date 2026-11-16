# ECO-00 — Foundation evidence

Date: 2026-11-13. Scope: user-authorized ECO-00 only. Attached architecture and
master-plan documents are design inputs, not commands to execute their entire roadmap.

## Workspace and preservation

Actual working directory `/mnt/d/ai_agent` maps to `D:\ai_agent`.
Initial `ls -la` showed an empty directory (including hidden files); no Git repo
or applicable ancestor AGENTS.md was present. Read access passed; exclusive
`mktemp` creation and removal in the root confirmed write access. All initial
scaffold files were created with exclusive-create semantics. No old work existed
to overwrite. Git initialized on `main`; no commit or remote was created.
The default command sandbox failed because bubblewrap is absent; checks and
writes used the environment's reviewed execution path.

## Delivered

Independent Python uv workspace, optional Go module and Rust workspace; manifests,
root uv.lock, Cargo lock, ignore rules, environment template, Make targets, local
instructions, ownership ADR, PR template, path-filtered independent CI jobs.
OpenAPI 3.0.3 draft liveness contract has one authoritative JSON file. It is not a
running endpoint. Architecture fitness checks protect static Python imports.
No server, queue, worker, MAF adapter, parser, FFI or global orchestrator exists.

## Actual environment and evidence

- Git 2.43.0; Python 3.12.3 available. `python`, pip, uv, make, Linux Go and Rust
  were absent from PATH initially.
- uv 0.9.10 downloaded under `/tmp`; `uv sync --all-packages` built/installed the
  Research package and resolved 21 packages. `uv lock --check`: PASS.
- Python `unittest discover -s domains/research/tests -v`: PASS, 1 test.
  Uses a fake Python adapter, not a production parser.
- Python `unittest discover -s tests/architecture -v`: PASS, 4 tests, including
  negative fixtures for framework and relative adapter imports.
- `python scripts/validate_openapi.py`: PASS using openapi-spec-validator 0.7.2.
- `python -m compileall -q domains/research/src scripts tests`: PASS.
- Windows Go found at `C:\Program Files\Go\bin\go.exe`, version 1.26.10.
  `go test ./...`: PASS compilation, **no test files**; `go vet ./...`: PASS;
  `gofmt -l`: no output. CI's Go 1.23.6 baseline was not locally exercised.
- Git ignore checks: `.env`, `.venv`, Rust target ignored; `.env.example` and
  uv.lock retained.
- CI YAML parses and has five jobs. GitHub Actions was **not executed**; no remote
  is configured. Static parse does not prove hosted workflow permissions/execution.
- Docker 29.9.2 and Compose v5.6.1 available; `docker info`/image listing FAIL:
  `/var/run/docker.sock` unavailable. No image/container/pgvector test was run.

## Rust verification and overall status

Rust 1.85.0 + cargo/rustfmt installed temporarily under `/tmp/eco-rustup` and
`/tmp/eco-cargo`; system PATH was not changed. Cargo generated Cargo.lock.
`cargo check --locked --workspace`: PASS. `cargo fmt --all -- --check`: PASS.
`cargo test --locked --workspace`: BLOCKED/FAIL at link time: `linker cc not found`.
The crate currently has no behavioral parser tests. Install a system C build
toolchain (e.g. build-essential on Ubuntu) and rerun before closing acceptance.

**Status: scaffold implemented; ECO-00 acceptance is not fully verified** because
Rust tests could not link and hosted CI has not run. Docker is also unavailable,
but it is not required for the independent ECO-00 language checks.

Temporary tools for reproducing this session (not permanent install paths):

```sh
UV_CACHE_DIR=/tmp/eco-uv-cache /tmp/uv-x86_64-unknown-linux-gnu/uv sync --locked --all-packages
export RUSTUP_HOME=/tmp/eco-rustup CARGO_HOME=/tmp/eco-cargo
export PATH=/tmp/eco-cargo/bin:$PATH
(cd engines/document-rs && cargo test --locked --workspace)
'/mnt/c/Program Files/Go/bin/go.exe' -C D:/ai_agent/apps/gateway-go test ./...
```

## Next acceptance work

Do not mark G0 feasibility or G1 runtime architecture passed by this scaffold.
Run hosted CI after configuring a remote. Install normal local toolchains (including
make if desired), enable Docker daemon, then RD-00 verifies pinned MAF, local
model, scholarly providers, pgvector and parser options. RD-01 adds the actual
standalone Python API; OPS-00 adds OTel; RD-02/CAP-00/ORCH-00 add durable jobs.
Lock runtime dependencies only after those feasibility tests.

## Input provenance

Original files were read from `C:\Users\Nghia\Downloads` and left unchanged.

- Runtime Architecture v3.1 SHA256:
  `f64666b51908027a371cdf978373ad4af689e26561813b8d3928f9963c8db821`
- Master Implementation Plan v1 SHA256:
  `a8d61cf185579aa393eed7420cc42edc04019cd11365c8ac8d987c818f5e0558`
