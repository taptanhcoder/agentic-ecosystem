# Repository Engineering & Operations

**Status: policy/reference baseline; NOT evidence of production readiness.** Updated 2026-11-16.

This directory governs the repository, Git workflow, GitHub settings, CI, release and deployment for the Research-first Python + Go + Rust ecosystem.

| Document | Purpose |
| --- | --- |
| [01_REPOSITORY.md](01_REPOSITORY.md) | Verified source tree, ownership, documentation authority |
| [02_GIT_WORKFLOW.md](02_GIT_WORKFLOW.md) | Local WSL Git, branching, rebasing, commit/PR practices |
| [03_GITHUB_GOVERNANCE.md](03_GITHUB_GOVERNANCE.md) | GitHub repository governance and settings |
| [04_CI_CD.md](04_CI_CD.md) | Current CI, quality gates, planned build/publish/rollout |
| [05_DEPLOYMENT.md](05_DEPLOYMENT.md) | Deployment topology and environment design |
| [06_RELEASE_ROLLBACK.md](06_RELEASE_ROLLBACK.md) | Release, backup, migration, rollback, incident response |
| [07_SECRETS_SECURITY.md](07_SECRETS_SECURITY.md) | Credentials, supply chain, authorization and secret handling |
| [08_OPERATIONS_CHECKLIST.md](08_OPERATIONS_CHECKLIST.md) | Engineering evidence and go/no-go checklist |

## Evidence versus proposal

Verified from GitHub main, 2026-11-16: monorepo scaffold, Research Python package, Go gateway scaffold, Rust document-core scaffold, OpenAPI draft, tests, Makefile, .github/workflows/ci.yml. See [project status](../PROJECT_STATUS.md) and [actual audit](../SETUP_BASELINE.md). GitHub main may evolve; inspect it each time.

Not verified/implemented: Research API, async Research worker, durable jobs, migrations, production image/Dockerfiles, Rust parser, frontend application, deployed environments or release gates G0-G5. Do not treat diagrams or sample Compose as running services.

## Repository principle

Docs and operations must track tested implementation. Keep active docs close to source, historic plans separate, and reconcile contradictory guidance via ADR. The existing status ledger is authoritative for evidence; never replace it with assumed progress.

## Implementation order

OPS-REPO-01 (docs, governance) → OPS-CI-01 (validate docs/templates and harden existing CI) → OPS-IMAGE-01 (reproducible containers once runtime exists) → OPS-DEPLOY-01 (staging after tests) → OPS-RELEASE-01 (production after G5 and manual approval).
