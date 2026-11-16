# 04 — CI/CD Architecture, Current State & Evolution

## Existing CI — KEEP, DO NOT REPLACE

.github/workflows/ci.yml currently defines a Foundation workflow with change detection and distinct Python, Go, Rust, contract and architecture jobs. Architecture checks run unconditionally; others use path filters. The repository audit has NOT demonstrated a successful hosted GitHub Actions run for all jobs. Do not claim they passed.

Current core entrypoints:
- Python: uv sync --locked --all-packages; unit tests under domains/research/tests.
- Architecture: Python unittest discovery under tests/architecture.
- Contract: scripts/validate_openapi.py.
- Go: go test ./..., go vet ./..., gofmt.
- Rust: cargo test --locked --workspace, cargo fmt --check.

## New operations CI

.github/workflows/ops-validation.yml validates repository operations docs and the Compose template. It performs NO deployment, image pull, secret access or service startup. It is safe to run on PRs from forks with read-only token.

## Delivery stages

    Commit / PR
      → static checks + language tests + contract + architecture
      → integration / database / recovery when runtime exists
      → AI golden evaluation + security checks + performance baseline
      → build reproducible OCI images (AFTER Dockerfiles/runtime exist)
      → scan images & generate SBOM/provenance
      → push immutable image digest to GHCR (release tag, write:packages only)
      → staging deploy + health/integration smoke
      → manual G5 production approval
      → production deploy + rollback/trace evidence

## Required gate mapping

- PR: correct formatting; unit/contract/architecture; no secrets.
- R0: durable API→job→worker→artifact tests, idempotency, recovery and trace propagation.
- R1: report evidence/citation quality and browser/progress test when frontend chosen.
- R2/G5: stress/recovery/security, backup/restore drill, supply chain, operational runbooks and release decision.

## Required pipeline hardening (separate PR)

1. Record versions and audit third-party actions; introduce lockfile/pin verified SHAs.
2. Confirm dorny/paths-filter works on push/PR and does not hide contract-breaking shared changes.
3. Ensure required statuses always report even if a language job is skipped; use aggregate gate if needed.
4. Add DB-backed integration jobs when migrations and API exist.
5. Add dependency scanning, artifact retention policy and trusted build provenance.
6. Add image publishing only after tested Dockerfiles; use immutable digests; never build fake images from stubs.

## Current limitation

The repo has NO running Research API/Worker or production Dockerfiles. There is therefore no truthful automatic production deployment workflow. The template in deployments/templates is validated as configuration only, not released or executed.

See: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax and https://docs.github.com/en/actions/reference/security/secure-use

## Branch workflow update

See [ADR 0004](../adr/0004-development-branch-workflow.md). Both workflows cover
main, dev and release branches. Foundation uses the pushed branch as its comparison
base for push change detection; PR detection uses the PR diff. Main-targeted PRs,
main pushes and manual runs execute all language/contract jobs. Ordinary dev/task
work retains path filtering. No automatic deployment is introduced.
