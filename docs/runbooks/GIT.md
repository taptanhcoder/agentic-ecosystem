# Git workflow for a solo project

## Branches

`main` is the only permanent branch. Keep it usable and check CI after pushing.
Use one short-lived branch and a pull request per task, including small changes.
This follows [repository policy](../ops/02_GIT_WORKFLOW.md).
No `develop`, staging branch, or release branch is needed at this stage.
Use `feat/research-api`, `fix/document-parser`, or `chore/tooling`; Codex-created
branches use `codex/<task>`. Delete the task branch after merging.

## Daily commands

```sh
git switch main
git pull --ff-only
git switch -c feat/research-api
# Implement, test, inspect the diff, then stage specific files.
git add <specific-files>
git commit -m "feat(research): add research API"
git push -u origin HEAD
```

Open a PR targeting `main`, review your own diff, and wait for relevant CI checks.
Use **Squash and merge** with a descriptive PR title. No second reviewer is needed
for solo work. Delete the remote branch using the PR page after merging, then:

```sh
git switch main
git pull --ff-only
git fetch --prune
```

Squash merging does not mark the local feature commits as merged. Delete the
local task branch only after confirming its changes are on `main`; Git may require
`git branch -D <task-branch>` for a squash-merged branch.

## Commits and releases

Use `type(scope): short description`; scope is optional. Common types:
`feat`, `fix`, `docs`, `refactor`, `test`, `ci`, `chore`, `perf`.
Each commit should represent one coherent change. This is a convention, not a
mandatory hook or extra Node dependency. Commit messages may use English or Vietnamese.

Create an annotated version tag only for a tested milestone; do not tag every commit:

```sh
git tag -a v0.1.0 -m "First usable research milestone"
git push origin v0.1.0
```

The version above is an example, not a release already created. Tag only a commit
whose `main` CI passed. Use patch versions for fixes, minor for additions, and major
for breaking public API changes after 1.0.

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

## Checks and GitHub settings

CI runs on pushes to `main`, PRs targeting `main`, and manual dispatch. New runs
cancel superseded runs for the same PR/branch. Language checks are selected by
changed paths; manual dispatch runs all language/contract checks.
See [local checks](LOCAL.md). Inspect CI and review the diff before merging.

This setup does not enforce server-side branch protection or merge settings.
If you enable protection later, block force pushes/deletion of `main`, require PRs,
and avoid requiring another reviewer for a solo project.

Keep `.env`, credentials, environments, build artifacts, and dependencies out of
Git. `.env.example` contains only sample values. Review `git diff --cached` before
committing. Lockfiles are intentionally versioned.

Reference: https://git-scm.com/docs/git-config
