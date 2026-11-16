# ADR-0003 — Repository, GitHub CI/CD & Deployment Policy

- Date: 2026-11-16
- Status: PROPOSED, subject to owner review and runtime evidence.
- Scope: Repository governance; no Research architecture/business state modifications.

## Context

The project is a solo-engineered Python/Go/Rust Research-first ecosystem. A foundation GitHub Actions workflow and source scaffold exist, but no deployable Research API or Worker is built. We must not confuse configuration templates with operational readiness.

## Decision

1. Preserve the existing repository and Foundation CI; add separate docs/template validation without privileged actions.
2. Use short-lived branches, reviewable PRs and protected main. Do not force push or auto-deploy production.
3. Keep one language-independent operations source of truth in docs/ops, referencing verified implementation evidence.
4. Use Docker Compose single-host as a candidate **initial deployment profile**, not an immediate production platform decision.
5. Require immutable OCI images, staged promotion, manual production approval, verified backups, security tests and G5 evidence.
6. Prefer minimal workflow permissions and pinned action dependencies.

## Consequences

Benefits: low solo-maintenance burden, transparent change history, low risk of accidental deployment, upgrade path to multi-domain infrastructure.

Trade-offs: no production automation until functional images, storage, auth and SLO tests exist; extra manual release gate; a single host is not high availability.

## Revisit

When R0/R1 runtime is available, when multiple domains require independent deploys, when availability/SLO requirements exceed single host, or when CI security tooling changes.
