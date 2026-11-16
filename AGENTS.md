# AGENTS.md — agentic-ecosystem

Repository-wide coding agent guidance. Before editing or running deployments:

1. Read docs/PROJECT_STATUS.md and docs/SETUP_BASELINE.md. Repository state and audit evidence take priority over older plans.
2. Read docs/adr/0001-architecture-boundaries.md and 0002-frontend-boundaries.md, then the architecture/implementation documents relevant to the ticket.
3. Read docs/ops/README.md for Git, GitHub, CI/CD, deployment, release and security policy.
4. Inspect git status, branch, commits, dependencies, tests and the files you will change. Do not overwrite uncommitted work.

## Engineering invariants

- Project: multi-domain Agentic AI Ecosystem; RESEARCH is first domain, not the whole ecosystem.
- Primary implementation languages: Python, Go, Rust. Frontend technology remains OPEN until a recorded ADR and UX proof.
- Python owns Research business state and agent workflows; Go owns optional edge/gateway; Rust owns optional bounded data processing.
- Research Domain must run independently of Gateway or a future Global Orchestrator. Do not duplicate research state or write across domain databases.
- Public interfaces must be versioned, and new dependencies/frameworks must be justified by an ADR and technical evidence.
- One authoritative Research run lifecycle; one durable job scheduling owner; bounded retries, timeouts, idempotency and observable failures.
- All external sources, tools and skills are untrusted. No unreviewed script execution or credentials in source, docs, logs or prompts.

## Repository / CI / release policy

- Preserve existing setup; no repository reinitialization, force push, destructive migration or live deployment without explicit authorization.
- Use feature branches and reviewable PRs. Do not claim CI or deployment passed without actual logs/evidence.
- The current GitHub Actions foundation workflow exists; service delivery is NOT production-ready.
- docs/ops/DEPLOYMENT.md and deployments/templates/compose.production.yaml are architecture/templates, NOT a functioning release.
- Never push production secrets; never enable automated production delivery without G5 approval and a reviewed release ADR.

## Every change

Read → Audit → Plan → Small implementation → Tests → Review → Update docs → Report.

Report changed paths, decisions, exact commands run and outputs, skipped checks, risks, rollback and next work item. Use VERIFIED / IMPLEMENTED_UNVERIFIED / PARTIAL / BLOCKED status with supporting evidence.
