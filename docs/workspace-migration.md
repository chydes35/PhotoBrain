# Workspace separation — 2026-10-21

## Canonical locations

| Project/data | Canonical location |
| --- | --- |
| PhotoBrain knowledge repository | `/Volumes/ExSSD1/Developer/PhotoBrain` |
| Existing M0 Editor clone | `/Volumes/ExSSD1/Developer/perception-media-editor-m0` |
| Existing separate Editor stabilization checkout | `/Volumes/ExSSD1/Developer/perception-media-editor` |
| M0 audit kit, original sample folder, copied fixtures and evidence | `/Volumes/ExSSD1/Developer/PerceptionEditor-M0-Workspace` |

The M0 sidecar workspace contains `Perception_Editor_Milestone_0/`, `PhotoTestFilesLumix/`, `m0-private/` and `m0-evidence/`. It is outside both repositories. Its new parent uses mode 700. Existing directory/file permissions are preserved. No private contents were opened for this migration.

## Compatibility and preserved work

The original five names under PhotoBrain are compatibility symlinks to the canonical locations. Absolute paths recorded by M0 and the old PhotoBrain alias layout remain resolvable. New Editor work should use its canonical checkout path. Historical descriptions that evidence was “beside the clone” refer to the original alias layout; use the explicit sidecar workspace for new commands, rather than assuming `../m0-evidence` from the relocated canonical checkout.

The M0 chat was idle with its last turn completed before relocation. Its branch was clean and matched its upstream. Same-volume directory renames preserved the checkout (including ignored build products), audit kit, original media directory, copied fixtures and evidence without copying or rewriting file contents. Existing links were not removed. Original media filenames/bytes and private manifests/logs were not opened or edited.

[Before snapshot](workspace-before.json) and [migration verification](workspace-migration.json) record the Editor HEAD/branch/status, tracked-file aggregate fingerprint and Git-config hash. All matched after relocation through both canonical and compatibility paths. These are public code/document fingerprints; private media hashes were not collected.

The ignored `.build` cache is preserved, but no build was run after relocation. Build tools may invalidate cached absolute paths and need a fresh build later. This task makes no post-move app-build or runtime claim. The separate stabilization checkout was not modified.

Root Git allowlisting excludes all five compatibility entries, private datasets, app source, `.build`, logs and nested Git metadata. Do not force-add them. A symlink is path compatibility, not a security boundary: agents must still obey `AGENTS.md` and avoid entering excluded datasets without authorization.

## Continuing existing chats

The old paths remain valid, so existing M0 references do not require a forced chat move. Use canonical app paths for future Editor commands. This setup did not change app project settings, message other chats, publish repositories, update the M0 PR or select a shared hosting service.
