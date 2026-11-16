# 08 — Operational Verification Checklist

Use this checklist with exact links to GitHub run, logs, commit, test output and ADR. Not checked = NOT RUN.

## Repository and Git
- [ ] Local repo origin and history reconciled with GitHub main; no uncommitted work lost.
- [ ] Active AGENTS.md read and relevant ADR reviewed.
- [ ] Change limited to ticket scope; clean diff and no secrets/binaries.
- [ ] PR records checks run, failures/skips, rollback and compatibility.

## CI / Quality
- [ ] Foundation CI completes on GitHub (not merely YAML present).
- [ ] Ops documentation validator and Compose syntax check pass.
- [ ] Python, Go, Rust checks run where relevant; skipped jobs identified.
- [ ] OpenAPI consumer/provider contract tests executed after API implementation.
- [ ] Architecture tests enforce domain independence.

## Runtime gates (unavailable until implemented)
- [ ] R0: POST task → durable job → Worker → persisted artifact.
- [ ] Worker crash recovery and idempotent writes.
- [ ] Bounded capacity/429/503 behavior, cancellation and lease fencing.
- [ ] Trace correlation Browser/Gateway/API/Worker/Tool without sensitive payload.
- [ ] R1: source/evidence/citation evaluation on known golden dataset.
- [ ] Authz/security and external skills/tool allowlist.
- [ ] Backup/restore drill with measured RPO/RTO.

## Deployment go/no-go
- [ ] Approved release ADR and G5 evidence.
- [ ] Reproducible Dockerfiles/images with scan/SBOM.
- [ ] Immutable image digests recorded; staging passed exact digest.
- [ ] DB migration plan and verified backup restore.
- [ ] TLS, firewall, auth, persistent storage and secret management reviewed.
- [ ] Owner manually approves production and knows rollback.
- [ ] Post-deploy health, error rates, queue latency and traces reviewed.

**Current assessment on 2026-11-16: No release-ready Research runtime. Deployment NO-GO.**
