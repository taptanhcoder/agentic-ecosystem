# Local development (ECO-00)

Run from repository root in WSL/Linux. Python 3.12, uv 0.9.10, Go 1.23+
and Rust 1.85 (cargo/rustfmt plus a C linker, e.g. Ubuntu build-essential) are the scaffold baselines. CI uses Go 1.23.6
and Rust 1.85.0. Docker is optional and not needed for these checks.

```sh
uv sync --locked --all-packages
uv run --locked python -m unittest discover -s domains/research/tests -v
python3 -m unittest discover -s tests/architecture -v
uv run --locked python scripts/validate_openapi.py
(cd apps/gateway-go && go test ./... && go vet ./...)
(cd engines/document-rs && cargo test --locked --workspace && cargo fmt --all -- --check)
```

Or use `make bootstrap check` if make is installed. Individual language commands
have no dependency on other language toolchains. Python source-only checks without uv:
`PYTHONPATH=domains/research/src python3 -m unittest discover -s domains/research/tests -v`.
The OpenAPI validator needs the locked development dependencies.

`uv.lock` is at the monorepo root (one uv workspace). Update intentionally with
`uv lock`, review the diff, then repeat checks. Build backend is pinned in the
Research manifest. Cargo.lock is committed for the workspace. Go has no external
modules, so go.mod is sufficient until `go mod tidy` adds dependencies.

Copy `.env.example` to `.env` only when configuring later runtime slices; ECO-00
does not read these values. Do not commit secrets. There is no local server to
start yet. Next: RD-00 dependency feasibility, then RD-01 API and OPS-00 tracing;
RD-02/CAP-00/ORCH-00 add Postgres jobs. Do not install MAF/DB/OTel speculatively.

Future local profiles: core-dev (Python API/worker + PostgreSQL/pgvector), trace-dev
(add Collector/viewer), polyglot-dev (optional gateway/native adapter). Compose
files will arrive with runnable services; no empty deployments are presented as working.

## Updated plan (v2 / frontend v3.2)

Do not rerun bootstrap to apply the new plan. Reuse the existing environment and
locked dependencies; use the independent checks above. See
`docs/implementation/SETUP_BASELINE.md` for the audited gaps.

No frontend app or JS manifest exists yet. Windows Node was detected, but no
frontend build, package manager or React version has been validated. FE-01 will
select the toolchain; FE-02 generates the client from the existing OpenAPI JSON.
There is no frontend start command yet. Do not infer a running UI from the target
architecture diagram.
