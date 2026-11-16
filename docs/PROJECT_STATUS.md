# Project status — evidence ledger

Updated 2026-11-16 (Asia/Saigon). Active reference: user-supplied
AI_AGENT_ENGINEERING_GUIDE.md in the handoff bundle; not yet copied into repo.

AUD-00: VERIFIED audit completed; setup acceptance PARTIAL.
See [full audit and proposed TECH-01A](SETUP_BASELINE.md) for exact commands,
versions, limitations, risks and rollback. Historical docs/implementation baseline
is retained; it is not current evidence.

- VERIFIED: existing scaffold; Python 7 architecture + 1 unit tests; OpenAPI
  validation; Go compilation with no test files; Docker daemon now reachable.
- IMPLEMENTED_UNVERIFIED: Rust scaffold and hosted CI configuration.
- BLOCKED: current Rust checks (cargo absent); uv lock validation (uv absent).
- PROPOSED: Research API, domain lifecycle, PostgreSQL persistence/jobs, worker,
  MAF/model integration, parser, frontend, tracing, evidence/reports and memory.
- UNKNOWN: association/health/schema of existing Docker services for this project;
  model profile, credentials policy and hardware capacity. No secrets inspected.
- OPEN: frontend selection; older React ADR conflicts with active guide. No UI
  rewrite or decision made. Runtime/model/parser/auth/checkpoint choices unverified.
- DEFERRED: Global Orchestrator and real second domain.

Git update 2026-11-16: source committed and pushed to origin/main (99b8a6a);
operations policy merged via PR #1 (8d92a75). Solo Git setup is on
`codex/solo-git-workflow`, pending PR/hosted CI verification.
VERIFIED locally: 7 architecture tests + 1 Python unit test, workflow YAML parse.
IMPLEMENTED_UNVERIFIED: revised hosted Foundation workflow; remote protection
settings have not been configured by this setup. Historical AUD-00 findings below
and in SETUP_BASELINE.md remain audit snapshots.
G0–G5: NOT PASSED. R0 durable foundation, R1 useful Research, R2 operational
readiness follow active guide; no release is implemented by this scaffold.

Next proposed ticket: TECH-01A bounded model/runtime probe, subject to verified
model/profile and resource policy. Not executed or approved as a production choice.

Change log: AUD-00 created only SETUP_BASELINE.md and this ledger. No framework
installations, reinitialization, refactor, feature, migration or service changes.
