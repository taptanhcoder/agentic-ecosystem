# 03 — GitHub Governance

Repo: https://github.com/taptanhcoder/agentic-ecosystem (public as observed 2026-11-16).

## Settings baseline (proposed; NOT asserted configured)

- Enable branch ruleset/protection for main and dev. Block force pushes and deletion.
- Require pull request before merge; for a solo owner do not require an impossible independent approval count. Use review checklist and CI as a compensating control until collaborators join.
- Require checks that always run (existing architecture job, and ops-docs job after verified). Do NOT mark path-filtered jobs required if they are not guaranteed to report a status on every PR.
- Keep repository Actions permissions least-privilege; default GITHUB_TOKEN read-only and grant package write only to future, isolated publishing workflow.
- Restrict allowed actions/versions; prefer action dependency lockfiles or verified full commit SHAs.
- Enable Dependabot/security advisories and dependency review according to plan availability; do not install new action scanners speculatively.
- Enable secret scanning/push protection if the repository/account supports it. Never depend on scanners as a substitute for secure handling.
- Configure staging and production GitHub Environments only when real environments exist. Production approvals and branch restrictions should be enforced before real deployment.
- Use labels: type:feature, type:fix, type:docs, area:research, area:platform, area:infra, risk:high.
- Optional: GitHub Projects board with Backlog, Ready, In Progress, Review, Verified, Blocked, Done.

- Allow merge commits for dev/main promotion and squash for task PRs; do not require linear history.
- Keep main as the default branch. Target routine task PRs at dev.
- Keep automatic head-branch deletion disabled to preserve dev; delete merged task branches manually.

## PR protocol

Every PR includes business rationale, exact files, architecture impact, evidence of executed tests, skipped checks, rollout and rollback. Require linked ADR for architecture and new frameworks.

## Repository public visibility considerations

- No customer research source texts unless redistributable.
- No private provider keys, model credentials, SSH keys, tokens, raw prompts with secrets, private traces, internal datasets, database dumps or .env.
- Security policy applies to CI artifacts, logs, issue screenshots and release bundles as well as committed files.

## GitHub environment controls

Development: local only. Staging: manual deployment after functional and security testing. Production: explicit human approval after G5; locked branch/tag and immutable image digest.

The current GitHub repository does not have an approved production deployment. Avoid auto-creating deployments from an illustrative compose file.

Docs: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions
