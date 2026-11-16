# 06 — Release, Rollback, Backup & Incident Runbook

## No-Go baseline

G0-G5 are NOT passed as of repository handoff. No Research API, Worker or release image exists. The steps below are procedures for the first future deployable release, not a record of a deployment.

## Release procedure

1. Verify clean Git status, correct commit and approved PR; create immutable release tag only after release decision.
2. Collect exact CI link/results (including skipped checks), contract+architecture checks, DB integration, AI evaluation, recovery and security evidence.
3. Confirm app and DB compatibility; take and verify backup BEFORE migrations; test restore with representative synthetic data.
4. Inspect staged images by digest; verify supply-chain/scanning and security posture; keep old digest available.
5. Deploy to staging. Run live/readiness probes, API→job→worker→artifact tests and trace propagation; watch queues and error rates.
6. Open an explicit production approval window: target commit/image digest, migrations, risk, owner, rollback steps and evidence.
7. On approved manual promotion, deploy the SAME digest with production-only configuration and protected credentials.
8. Watch API p95/error, queue age/dead jobs, worker lease recovery, provider throttling, DB pool and trace flow.
9. Record the release outcome, links, observed metrics and remaining issues.

## Rollback matrix

| Failure | Primary response | Data caution |
| --- | --- | --- |
| API regression | Revert API image digest (compatible contract) | Clients may require compatibility |
| Worker regression | Pause intake/drain jobs, roll back worker image | Preserve leases/idempotent results |
| Migration issue | Restore compatible binary or apply forward fix | Never blindly DOWN migration |
| Model/skill quality issue | Disable capability via config, revert adapter/skill | Preserve provenance and audit |
| Container/host loss | Restore orchestrator config, artifacts and DB backup | Run restore drill first |
| Telemetry outage | Allow core business run; alert and buffer/drop telemetry safely | Do not log secrets |

## Incident severity and communication

P0: data loss, credential leak, unauthorized execution; freeze deploy and contain.
P1: Research API/worker outage, widespread failed jobs; rollback compatible image and preserve data.
P2: degraded latency or citation quality; turn off affected feature, investigate and document.

Capture incident ID, timeline, trace/run IDs (no confidential contents), actions, recovery evidence, root cause and prevention. Add regression tests before re-enabling risky feature.

## Backup policy

Back up PostgreSQL and artifact storage with coordinated retention, encryption and access controls. Restore testing must measure actual RPO/RTO before declaring operational objectives. No unverified claims of backup success.
