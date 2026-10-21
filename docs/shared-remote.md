# Shared remote setup

## Remote and branch policy

- Repository: [`chydes35/PhotoBrain`](https://github.com/chydes35/PhotoBrain)
- Visibility: public, independently checked through GitHub on 2026-10-21 before PB-002 publication. This task did not change visibility.
- Default branch: `main`
- Local remote name: `origin`
- Initial published commit: `6e3c9e35bbe0ffdc16fc7dfef8e5d2f69f456d96`
- `main` requires a pull request, applies that rule to administrators, disallows force-pushes and branch deletion, and requires no fixed approval count. No required CI checks are configured yet. Review the science, source claims, tests and privacy before the integrator merges.

Contributors should clone the repository using a suitable Git client, claim a task on [the task board](../tasks/README.md), and work on a task branch. Push that branch and open a PR to `main`; do not push directly to `main`. The branch rule ensures changes arrive through PRs, while the task board assigns ownership and prevents overlapping edits.

## Model and connector access

The repository is currently public. Reading public content does not grant write access. Writing through GitHub belongs to each execution environment and must be authorized through that environment's normal account or connector setup. Never place a credential in a prompt, document, commit, or command output. Do not assume that one model's connected GitHub account makes this repository available to another model.

At the original private-repository setup verification, the GitHub connector installation for `chydes35` did not include this new repository, so the connector could not fetch it. At that time, adding PhotoBrain in [GitHub's installation settings](https://github.com/settings/installations/163568512) was the proposed remedy. That result is historical: a connector read succeeded during PB-002 publication checking. Recheck each environment's current read and write capabilities separately; public read access does not establish push/PR permissions. Use a separately authorized local Git client or a reviewed patch where needed. Other model providers need their own authorized write access; no provider credentials or collaborator invitations are configured by this setup.

## Scope and data boundary

Only PhotoBrain's tracked knowledge and process files were published. Local private-media directories, copied fixtures, manifests, test logs and the Perception Editor checkout remain outside this repository. Check `git status` and inspect the exact branch diff before every push. The Editor has its own repository and roadmap; link a reviewed PhotoBrain topic by immutable commit and version when considering adoption.

The existing PB-002 worktree was not included in the initial push. It was completed as an independently reviewed contribution; subsequent publication uses its assigned branch and a pull request, as authorized by the user.
