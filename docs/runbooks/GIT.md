# Development and release workflow

Two permanent branches: `main` for approved stable milestones, `dev` for integration.
Branch names describe work, not its author. Create task branches only when needed;
there is no permanent branch named `feature`, `fix`, or `release`.
This implements [ADR 0004](../adr/0004-development-branch-workflow.md).

## Branch routing

| Branch | Start from | PR target | Merge method |
| --- | --- | --- | --- |
| `feature/<task>` | `dev` | `dev` | Squash |
| `fix/<task>` | `dev` | `dev` | Squash |
| `chore/<task>`, `docs/<task>`, `refactor/<task>` | `dev` | `dev` | Squash |
| `experiment/<topic>` | `dev` | `dev`, only if accepted | Squash |
| `dev` (ready milestone) | existing branch | `main` | Merge commit |
| `release/<version>` (optional stabilization) | `dev` | `main` | Merge commit |
| `hotfix/<task>` | `main` | `main` | Merge commit |
| `main` (after release/hotfix) | existing branch | `dev` | Merge commit |

Use lowercase kebab-case, for example `feature/research-api`, `fix/parser-timeout`,
`hotfix/auth-check`, `release/0.1.0`. Keep branch work bounded to one task.
Use `feat(research): ...` for commit messages even though the branch prefix is `feature/`.

## Daily development

```sh
git switch dev
git pull --ff-only
git switch -c feature/research-api
# Implement and run relevant checks from LOCAL.md.
git status --short
git diff
git add <specific-files>
git diff --cached
git commit -m "feat(research): add research API"
git push -u origin HEAD
```

Open a PR **into dev**. Review the diff and actual CI results yourself; an independent
reviewer is not required for solo work. Squash merge task PRs and delete their branches.
After a squash, local branch deletion may need `git branch -D <task>`; first confirm
its changes are present in dev. Never delete `dev` or `main`.

If dev moves while a task is in progress, fetch and merge `origin/dev` into the task
branch, resolve conflicts and rerun checks. Do not force-push shared history.

## Promotion and release

For a tested milestone, open `dev → main` and choose **Create a merge commit**.
Keep dev. Do not squash/rebase promotions between permanent branches: this preserves
ancestry for subsequent releases. After promotion, open `main → dev` and merge with
a merge commit if there is a difference, keeping both histories synchronized.

When development must continue during stabilization, create `release/0.1.0` from
an explicitly selected, tested dev commit. Restrict it to release fixes/versioning;
merge it into main using a merge commit, then sync main back to dev before deleting
the release branch. A release branch is optional, not created for every task.

After main CI passes and the release decision is recorded, tag the exact main commit:

```sh
git switch main
git pull --ff-only
git tag -a v0.1.0 -m "First usable research milestone"
git push origin v0.1.0
```

This is an example, not an existing release. Git branches/tags do not deploy services.
Production still requires the gates in [release policy](../ops/06_RELEASE_ROLLBACK.md).

## Hotfix

Create `hotfix/<task>` from up-to-date main. Open its PR into main, run checks and
merge using a merge commit. Then open `main → dev` so the fix reaches future releases.
If a release branch is active, merge main into it through a PR too and rerun its checks.
Tag a patch release only after validation. Do not fix production only on dev.

## Commits and AI engineering evidence

Use `type(scope): description`, for example `feat(research): add retrieval filters`.
Types: feat, fix, docs, refactor, test, ci, chore, perf. Each commit has one purpose.
For model/prompt/retrieval changes, record model/config and dataset versions,
evaluation command, baseline versus new results, cost/latency and known regressions
when applicable. Link evidence in the PR; do not commit credentials, private datasets,
or sensitive prompts. CI currently checks the scaffold, not model quality.

## Local Git configuration

These settings apply only to this clone, not other projects. Repeat after cloning:

```sh
git config --local pull.ff only
git config --local fetch.prune true
git config --local push.default simple
git config --local core.autocrlf false
```

`pull.ff=only` stops when local and remote histories diverge. Inspect with
`git log --oneline --graph --all` before deciding how to integrate; do not force-push
`main`. To undo a published change, use `git revert <commit>` and push the new commit.
Repository `.gitattributes` controls line endings; `.editorconfig` helps editors
keep consistent formatting. Keep the configured GitHub noreply author email for privacy.

In this WSL clone, Git uses the installed Windows Git Credential Manager.
Credentials remain in the credential manager, never in repository files.
Other machines should use their own credential manager or SSH setup.

## CI and repository settings

Foundation and operations checks run for PRs into main/dev/release branches and
pushes to those branches. Feature PRs use changed-path checks; main-targeted PRs,
main pushes and manual Foundation runs execute all language/contract checks.
Read [local validation](LOCAL.md) before opening a PR.

Remote protection is not configured by these files. Target settings for main/dev:
require PRs, block force pushes/deletion, zero mandatory external approvals for solo
work. Allow merge commits and squash; do not require linear history. Do not enable
automatic branch deletion that could remove dev after a promotion. Delete only task
branches manually. Keep main as default; select dev explicitly for normal PRs.

Keep .env, secrets, local environments and generated output out of Git; lockfiles
remain versioned. To undo published work, open a revert PR against the affected
branch and propagate release fixes back to dev.

Reference: https://docs.github.com/en/pull-requests/reference/pull-request-merges
