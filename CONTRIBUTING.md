# Contributing with multiple AI models

## Assign work before editing

The task board allocates a stable task/module ID, owner/model, base commit, branch, owned files, prerequisites and reviewer. Assignment is a coordination record, not a filesystem lock. One integrator serializes assignments; contributors must not both claim the same files. If a topic overlaps, split the question or queue the work.

Use a separate clone/worktree and a branch such as `research/<task-id>-<model>`. Only one worker edits any checkout. The canonical remote is the GitHub repository (public as checked 2026-10-21) [`chydes35/PhotoBrain`](https://github.com/chydes35/PhotoBrain); `main` accepts changes through pull requests. Push only the assigned task branch, then open a PR to `main` with the task ID, base commit, scope, evidence and checks. Never push directly to `main`. The integrator reviews and merges accepted work, integrating shared registries and indexes serially.

Each model's execution environment needs its own authorized GitHub access for writing to this repository. Do not copy passwords, access tokens or private media into prompts or contribution files. If a model's GitHub connector cannot see PhotoBrain, have the repository owner grant that connector access to this repository in GitHub's installation settings; use an already-authorized local Git client or a reviewed patch until then. For a model without Git access, supply the topic template, pinned prerequisites and sources, and collect its patch or draft as a distinct contribution for an integrator to import. Do not give multiple models a single mutable canonical document/database.

Native worktree creation must use the PhotoBrain repository, never the Editor repo, and honor the external-SSD placement rule. A configured URL does not establish that any particular model environment has working credentials. PB-002 research was initially integrated locally; the user subsequently authorized GitHub publication.

## Author a contribution

Use [the topic template](templates/topic.md) and [the task/review template](templates/contribution.md). One question or algorithm per topic; chapter pages are indexes. Keep equations beside their units, assumptions and failure cases. Record model identifier if exposed by the host; use `not exposed` rather than guessing. Record author, base commit, source revisions/access dates, evidence scope and executable checks.

Preserve the blueprint and existing IDs. New source/claim IDs must be unique: use task-prefixed IDs such as `SRC-PB002-01` during independent work. Propose additions to shared registries in the contribution record; the integrator owns final registry/index edits. Do not auto-renumber another branch's references.

Use [V]/[I]/[H]/[U]/[D]. Source claims require a source-to-claim map; experiments require reproducible input/settings and results. Rejecting an experiment is a useful result. Keep scientific facts separate from app implementation choices. No arbitrary performance promises or unmeasured camera properties.

## Review and integrate

1. Author records changed files and checks at a specific commit, then hands the contribution to a different reviewer/agent.
2. Reviewer checks math, cited evidence, units, boundary cases, source/license status, tests, private-data exclusions and ownership. Each reported finding is independently confirmed; rejected findings are retained one per line.
3. Author addresses confirmed findings and reruns affected checks. A second checker verifies bug fixes using verification-runner. Two consecutive no-progress rounds stop for user input.
4. Integrator checks the current branch, base drift and changes from other contributors. Resolve substantive disagreements in a decision/review record; do not silently overwrite. Incorporate from the reviewed commit with a local merge/cherry-pick or reviewed patch. Merge shared indexes/registries serially, rerun all reference tests, and inspect staged files before commit.
5. Record integrated commit, review evidence, source/claim additions, limitations and changelog. An assigned task authorizes publishing its task branch and opening a PR; the integrator owns merge decisions. Do not publish data or merge unrelated work.

`research-draft` means unresolved coverage or gates. `fact-checked` requires independent claim/math review for the declared scope. `engineering-ready` additionally needs every blueprint §1.4 gate: executable reference/oracle, vectors/tolerances, domain/precision audit, data/license review, resource analysis and traced interface/dependencies. Code tests alone cannot promote a topic. Use `superseded` with a successor link for replaced topics.

## Publication and data

No blanket reuse license is granted by this repository yet. Cite sources instead of copying substantial third-party content. Public references can carry their own terms. Preserve private subjects and media; never commit local logs, populated manifests, media hashes or Editor project files. The source blueprint's checksum is a document-integrity checksum, not a private-media checksum.

An optional search/embedding database must be reproducible from an approved knowledge commit, record that commit, and be replaced atomically by one integrator. Drafts must remain distinguishable in search results. Multiwriter database design is deferred until there is an actual requirement.
