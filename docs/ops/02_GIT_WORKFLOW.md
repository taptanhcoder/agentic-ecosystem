# 02 — Git Workflow (Solo Engineer + AI Coding Agents)

## First reconcile the local repository

The 2026-11-16 AUD-00 report described a local tree at /mnt/d/ai_agent with no commits/remote at that moment. The GitHub repo does have a main branch and commits. These are snapshots from different points in time; do NOT assume histories match.

Read-only checks in WSL:

    cd /mnt/d/ai_agent
    git status --short
    git rev-parse --show-toplevel
    git branch --show-current
    git log --oneline --decorate -5
    git remote -v

If origin is absent, and only after confirming this is the right working tree:

    git remote add origin https://github.com/taptanhcoder/agentic-ecosystem.git
    git fetch origin
    git log --graph --oneline --decorate --all -20
    git merge-base HEAD origin/main

If merge-base fails or histories are unrelated, STOP and reconcile by inspection/new clone/patch; never push --force, reset --hard or overwrite local uncommitted source. If the local tree has no commits, back up/diff it against a clean clone and port only intended changes. Do not run git init again.

## Branch model and work sequence

The owner selected `main` + `dev` on 2026-11-16. This supersedes the earlier
single-permanent-branch quickstart. See [ADR 0004](../adr/0004-development-branch-workflow.md)
and [daily workflow](../runbooks/GIT.md) for the authoritative branch routing table.

1. Fetch and update dev; create feature/fix/chore/docs/refactor branch from dev.
2. Implement one task; inspect the diff and execute relevant checks.
3. Push the task branch and open its PR into dev; self-review and inspect CI.
4. Squash task PRs. Promote tested dev milestones into main with merge commits.
5. Hotfixes start from main; merge into main, then synchronize main back to dev.
6. Delete completed task branches; retain main and dev. Release branches are optional.

## Commit and PR policy

- One responsibility per PR; include ticket ID, scope/non-goals, changed paths, test commands/results, rollback and ADR/API impact.
- Do not auto-merge coding-agent PRs merely because a generated summary says PASS.
- Use git revert or a new corrective PR for history-preserving rollback; avoid destructive rewriting of shared history.
- For schema changes follow expand → migrate → contract, with explicit backup/recovery plan.
- Use signed commits if configured; consider mandatory signed commits only after tooling and contributor support are verified.

## Never do by default

git push --force, git reset --hard, git clean -fdx, git rebase across unrelated histories, DB destructive migrations, or secret uploads.

## Daily command reference

See [solo Git quickstart](../runbooks/GIT.md) for clone-local settings, command examples,
squash merging and tag conventions. `main` and `dev` are the permanent branches.
