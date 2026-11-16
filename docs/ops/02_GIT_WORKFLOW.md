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

## Branch model

- main: protected, reviewable, releasable only when appropriate gates pass.
- docs/*, feat/*, fix/*, refactor/*, ops/*, experiment/*: short-lived feature branches.
- Avoid a permanent develop branch for one maintainer unless a concrete release-flow issue requires it.
- Separate exploratory PoCs from application changes; expired branches should be closed after decision.

## Git work sequence

1. git status --short; inspect changes and the latest origin/main.
2. Pick ticket and acceptance tests; create branch from an up-to-date local main with clean working tree.
3. Make one coherent change; add tests, docs and evidence.
4. Run relevant checks locally: make architecture; make python; make contract; make go; make rust (only when toolchains available).
5. Inspect git diff --check and git diff --cached; ensure no secrets, large binaries or unrelated modifications.
6. Commit with meaningful Conventional Commit, e.g. docs(ops): add delivery governance or feat(research): add lifecycle transitions.
7. Push only the feature branch; open PR; inspect CI; merge after review and passing gates.
8. After merge, update project ledger only with factual evidence.

## Commit and PR policy

- One responsibility per PR; include ticket ID, scope/non-goals, changed paths, test commands/results, rollback and ADR/API impact.
- Do not auto-merge coding-agent PRs merely because a generated summary says PASS.
- Use git revert or a new corrective PR for history-preserving rollback; avoid destructive rewriting of shared history.
- For schema changes follow expand → migrate → contract, with explicit backup/recovery plan.
- Use signed commits if configured; consider mandatory signed commits only after tooling and contributor support are verified.

## Never do by default

git push --force, git reset --hard, git clean -fdx, git rebase across unrelated histories, DB destructive migrations, or secret uploads.
