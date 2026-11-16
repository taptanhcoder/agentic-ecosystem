# 01 — Repository Structure, Ownership & Documentation

## Identity
- GitHub: https://github.com/taptanhcoder/agentic-ecosystem
- Name: agentic-ecosystem
- Default branch: main
- Approach: polyglot modular monorepo, RESEARCH-first, autonomous domain boundaries.
- The repository on GitHub already contains a scaffold; do not recreate or overwrite it.

## Verified high-level layout on GitHub main

    apps/gateway-go/           Optional Go gateway scaffold; not a running proxy
    domains/research/          Python package with domain/application boundaries
    engines/document-rs/      Rust workspace/core stub; not production extraction
    contracts/openapi/        Research OpenAPI draft
    tests/architecture/       Executable architecture checks
    .github/workflows/ci.yml  Existing language-oriented CI definition
    docs/                     ADR, audit, status, local guidance and plans
    scripts/                  Current OpenAPI validator

Do not assume apps/web, Research API, migrations, active queues, frontend or deployed services exist until verified.

## Ownership and allowed dependencies

| Owner | Responsibilities | Must not own |
| --- | --- | --- |
| Python Research | Research state, API, durable domain jobs, MAF adapter, evidence, memory | Gateway identity policy; cross-domain global jobs |
| Go Gateway | Routing, admission/auth edge and future platform services | Direct Research database writes or Research planning |
| Rust document-core | Deterministic document normalization behind a port | Research DB, Agent workflow or business lifecycle |
| Frontend (OPEN) | UI/presentation, client streaming, typed API consumer | Backend domain models or Research state authority |
| contracts | Versioned language-neutral interfaces | Concrete SDK/ORM/framework objects |
| docs/ops | Engineering governance, delivery and operational evidence | Claims of executed tests absent run logs |

## Documentation precedence

1. Actual code, pinned manifests, executed tests and recorded evidence (facts).
2. Current approved ADRs and API contracts (intended rules).
3. docs/PROJECT_STATUS.md, docs/SETUP_BASELINE.md (verified and known gaps).
4. docs/ops (repository operational policy).
5. Historical plans (rationale, not an automatic mandate).

If documents disagree, write down the conflict, propose an ADR and avoid silently refactoring.

## Repository hygiene

- Existing README.md, Makefile, .github/workflows/ci.yml, Git history and lockfiles are preserved by default.
- Commit Python uv.lock, Rust Cargo.lock, Go manifests; review diffs and use reproducible dependency updates.
- Keep artifacts, local model weights, virtualenvs, .env, credentials, datasets with distribution restrictions and trace payloads out of Git.
- Place test fixtures under tests/ and sanitized examples under docs/; avoid sensitive source material in a public repo.
- New domain requires a public contract + architecture test, not cross-domain imports.
