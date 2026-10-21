# Shared remote setup

## Remote and branch policy

- Repository: [private `chydes35/PhotoBrain`](https://github.com/chydes35/PhotoBrain)
- Default branch: `main`
- Local remote name: `origin`
- Initial published commit: `6e3c9e35bbe0ffdc16fc7dfef8e5d2f69f456d96`
- `main` requires a pull request, applies that rule to administrators, disallows force-pushes and branch deletion, and requires no fixed approval count. No required CI checks are configured yet. Review the science, source claims, tests and privacy before the integrator merges.

Contributors should clone the private repository using an already-authorized Git client, claim a task on [the task board](../tasks/README.md), and work on a task branch. Push that branch and open a PR to `main`; do not push directly to `main`. The branch rule ensures changes arrive through PRs, while the task board assigns ownership and prevents overlapping edits.

## Model and connector access

The repository is private. GitHub access belongs to each execution environment and must be granted through that environment's normal account or connector setup. Never place a credential in a prompt, document, commit, or command output. Do not assume that one model's connected GitHub account makes this repository available to another model.

At setup verification, the GitHub connector installation for `chydes35` did not include this new repository, so the connector could not fetch it. To use that connector, the owner must add PhotoBrain in [GitHub's installation settings](https://github.com/settings/installations/163568512). This grants that connector access to the private knowledge repository. Until the owner enables it, use a separately authorized local Git client or exchange a reviewed patch. Other model providers need their own authorized access; no provider credentials or collaborator invitations are configured by this setup.

## Scope and data boundary

Only PhotoBrain's tracked knowledge and process files were published. Local private-media directories, copied fixtures, manifests, test logs and the Perception Editor checkout remain outside this repository. Check `git status` and inspect the exact branch diff before every push. The Editor has its own repository and roadmap; link a reviewed PhotoBrain topic by immutable commit and version when considering adoption.

The existing PB-002 worktree was not included in the initial push. It remains an independent contribution and should be pushed from its assigned branch after its owner completes review and validation.
