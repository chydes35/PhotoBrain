# Perception Editor integration index

This is PhotoBrain's Chapter 17 integration summary, not an authoritative app roadmap. Repository-specific implementation tickets, ADRs, test gates and release decisions stay in Perception Editor. Research can advance without modifying or rebuilding the app.

## Application references

- Application repository: [chydes35/perception-media-editor](https://github.com/chydes35/perception-media-editor).
- M0 checkout: `<m0-editor-checkout>/` (a standalone clone beside PhotoBrain on the external SSD).
- M0 branch: `codex/mpkb-v2-m0-baseline`.
- Pinned M0 commit: `593549a4e0461ad548b7f0588c068fb509fda6d4`.
- Baseline source investigated by M0: `0d3283aa9063bb081ac39554a66221c5e87db53f`.
- Existing separate stabilization checkout: `<editor-stabilization-checkout>/`; preserved untouched by this setup. Its working state can evolve independently.
- Placeholders in angle brackets stand for machine-local absolute paths, removed from this public record by PB-009 (2026-10-21); the owner's machine holds the real locations.
- M0's own status is in its `docs/CURRENT_STATUS.md`, `docs/research/mpkb-v2/` and `plans/active/mpkb-v2-m0-baseline.md` at the pinned app commit. Historical claims apply only to their recorded revision/data; PhotoBrain setup does not complete M0.

## Adoption contract

| PhotoBrain record | Knowledge version | Editor adoption | Gate |
| --- | --- | --- | --- |
| MPKB-02-005 | 0.2.1, research-draft | Not implemented or assessed in this task | Independent review of full intended scope plus app-specific audit/ticket before adoption; partial Rec.709 inverse is not a video decoder |

For each future adoption record, capture PhotoBrain commit + topic IDs/versions, Editor base/implementation commits, app ticket/ADR link, compatibility implications, tests, rollback and explicit accepted/unverified results. Use the actual immutable commits, not merely “latest PhotoBrain.”

Generic mathematical contracts can live in PhotoBrain. Concrete Swift/Metal interfaces and named app files must be derived from an app audit and maintained in the app repo. The blueprint's ENG-* list is a proposed research backlog, not proof those components exist.

No app runtime code reads this repository. No automatic sync, Git submodule, remote dependency or embedded search service was introduced. [Workspace migration](../docs/workspace-migration.md) documents local path compatibility.
