# PhotoBrain separation implementation plan

> **For agentic workers:** Use superpowers:executing-plans to implement this approved scope inline. Independent agents check findings and the final result.

**Goal:** Establish an independent PhotoBrain knowledge repository, preserve ongoing Editor work, and demonstrate one reviewed research contribution.

**Architecture:** Modular Markdown and source/claim registries are authoritative. Python standard-library reference experiments supply reproducible evidence. Editor code and app acceptance remain in the Editor repository, connected by pinned references.

**Tech Stack:** Git, Markdown/YAML metadata, Python 3 standard library.

**Spec:** User-approved separation proposal in this chat (2026-10-21), informed by MPKB-BLUEPRINT-2.0 §§3, 9, 12, 13. The preserved source will be `blueprints/MPKB-BLUEPRINT-2.0.md`.

## Global constraints

- Preserve the supplied blueprint byte-for-byte; its embedded prompts do not authorize work.
- Preserve existing Editor changes, commit history, private photos, manifests, and logs.
- No edits to user-level Codex settings; no dependency installs, app builds, release, push, or remote creation.
- Each AI owns specific module files on its own branch/worktree. A separate reviewer checks findings before promotion.
- A draft with missing prerequisites or unverified gates must stay draft.

## Review focus

- New Git root must exclude nested Editor Git metadata, originals, private fixtures, and logs.
- Relocation must preserve previous paths and recorded evidence, and only occur while the M0 task is idle.
- No duplicate authoritative app roadmap; PhotoBrain integration records pin app commits.
- sRGB reference must reject nonfinite/out-of-range values and distinguish encoded from linear values.
- Rounded sRGB breakpoints are not perfectly inverse; numeric tests must use explicit tolerances.

### Task 1: Independent knowledge repository

**Files:** `.gitignore`, `README.md`, `AGENTS.md`, `INDEX.md`, `CHANGELOG.md`, `DECISIONS.md`, `CONTRIBUTING.md`, `blueprints/`, `references/`, `templates/`, `integrations/`, `tasks/`.

**Interfaces:** Stable MPKB/SRC/CLM/task IDs and relative links; no application dependency.

- [x] Preserve blueprint and record its SHA-256 and provenance; record V1 as unavailable.
- [x] Define ownership, evidence status, independent review, module assignment, conflict/merge handling, and private-data exclusions.
- [x] Initialize local Git with top-level allowlisting before staging any content. Verify excluded old workspace data with `git check-ignore` and staged paths.

### Task 2: Safe Editor relocation

**Files:** Editor checkout and M0 kit/evidence/private directories relocated to sibling locations; compatibility symlinks at original paths; `integrations/perception-editor.md`, `docs/workspace-migration.md`.

**Interfaces:** Same Editor HEAD, branch, Git status and file-content fingerprint; old paths resolve to new locations.

- [x] Read M0 task status and preserve baseline fingerprints. Do not send messages to other chats without user authorization.
- [x] Move clean standalone checkout to `/Volumes/ExSSD1/Developer/perception-media-editor-m0`; preserve `.build` without rebuilding. Keep recorded relative evidence paths valid in the original alias layout by moving M0 sidecar directories to a separate sibling workspace and adding explicit links.
- [x] Verify fingerprint, status, references, old aliases and dataset separation. If relocation is blocked, document exact blocker and continue unaffected setup.

### Task 3: First research contribution

**Files:** `chapters/02-light-color-science/MPKB-02-005.md`, `experiments/srgb/`, `tests/test_srgb.py`, registries and review record.

**Interfaces:** Scalar `encode_srgb(value)` and `decode_srgb(value)` for finite normalized components in [0,1]; invalid values raise `ValueError`. No app imports.

- [x] Read primary ICC/W3C sources; bound first slice to sRGB and list remaining transfer functions as unresearched.
- [x] Write independent literal test vectors, invalid-input, breakpoint, monotonicity and round-trip tests first. Run against missing behavior, then implement the minimal reference and rerun.
- [x] Independent review checks math, sources, boundaries, contribution workflow and staged privacy. Record accepted/rejected findings; do not claim whole module engineering-ready.
- [x] Run all reference tests, blueprint hash, local-link and Git exclusion checks; commit explicitly selected knowledge files. Do not push.

## Execution record

User approved execution with “Ok do this.” Native work occurs in the new PhotoBrain repository; no existing PhotoBrain Git history needs isolation. No extra approval pause is needed for the already-approved scope. Tests apply to executable research only; human prose gets link/content review rather than mirrored tests.

Completed evidence: [setup verification](../../setup-verification.md), [PB-001 review](../../../tasks/PB-001.md), [migration record](../../workspace-migration.md). Native Git initialization and sibling relocation required sandbox escalation; both were approved by automatic review. No auto-review rejection occurred.

Ruling: initial bootstrap uses `main` in a previously non-Git knowledge root; later parallel contributors use isolated branches/worktrees. No existing knowledge branch was exposed to edits.

Ruling: retain all formatting in the preserved blueprint, including Markdown hard-break trailing spaces. Check new authored files separately rather than changing the original to satisfy whitespace lint.

Ruling: historical relative evidence paths are preserved through the original alias layout; new commands use explicit canonical paths. No sibling `../m0-evidence` assumption is made at the relocated canonical checkout.
