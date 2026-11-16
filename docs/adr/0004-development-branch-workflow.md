# ADR 0004 — Development and release branches

Date: 2026-11-16. Status: ACCEPTED by owner request; implementation delivered by PR.
Scope: Git workflow only; no deployment or application architecture changes.

The owner wants a separate integration branch and stable milestone branch for solo
AI engineering. The previous main-only recommendation does not meet that requirement.

Keep main and dev permanently. Task branches start from dev and target dev. Feature
branches use feature/*; commits retain feat as the type. Squash task PRs. Promote
dev or optional release/* branches to main with merge commits and synchronize main
back to dev. Hotfixes start from main and follow the same synchronization rule.
Do not squash long-lived branch promotions or require linear history.

CI must cover both permanent branches and release stabilization. Full Foundation
checks run for main promotion; path filters remain for ordinary integration work.
Branch protections remain a separate remote setting, not implied by committed YAML.

Trade-off: two permanent branches require explicit promotion and synchronization.
Avoid permanent feature/release branches and automatic deletion of dev. No deployment
is triggered by this policy. This supersedes the main-only guidance and refines ADR 0003.

Rollback: return to main-only by a reviewed policy/CI change after all dev work is
accounted for. Do not delete unmerged branches or rewrite shared history.
