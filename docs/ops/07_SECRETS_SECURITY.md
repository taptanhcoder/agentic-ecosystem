# 07 — Secrets, Identity and Supply-Chain Security

## Secret classification

- Development: local .env files excluded by .gitignore, non-production credentials only.
- CI: read-only GITHUB_TOKEN for tests. Avoid third-party secrets on fork PRs.
- Staging/prod: GitHub Environments, protected secret store/identity-based access; never commit values.
- Model provider keys, database URIs, SSH keys, GHCR PATs, JWT signing keys and OAuth client secrets are secrets; mask and rotate on exposure.
- Research raw source content, downloaded skills and prompts can be sensitive; treat as untrusted data and apply logging redaction.

## GitHub Actions

- Workflow-level permissions: contents: read. Grant packages: write only inside a dedicated approved publish job.
- Prefer OpenID Connect to long-lived cloud credentials when supported by deployment platform.
- Pin GitHub Actions using verified full commit SHA or repository action lockfile.
- Do not execute untrusted pull request code with privileged workflow context (especially pull_request_target).
- Explicitly scope environments/branches/approvals for staging and production.
- Use immutable container digests, SBOM, vulnerability and dependency checks before promotion.

## Runtime

- Enforce authn/authz in Research API even when Go Gateway exists.
- Separate database roles, least privilege, migrations principal versus runtime principal.
- Validate user URLs/downloads against SSRF/private-network access; bound content sizes and timeouts.
- Review/allowlist scientific skills; no unrestricted execution of downloaded scripts or shell commands.
- Restrict outbound model/storage/data access; define content retention and deletion.
- Record sanitized audit events for privileged changes; avoid storing credentials or entire prompt/source in traces.

## Secret incident

Stop affected deployment/action, rotate credential, invalidate tokens, scrub public artifacts when possible, audit access and document impact. Rewrite Git history only as an incident response with explicit owner approval and a coordinated response, not as a routine cleanup.
