# Project decisions

## PB-ADR-001 — Independent knowledge and application repositories

Date: 2026-10-21. Status: adopted for this setup, authorized in chat.

PhotoBrain owns reusable research and reference experiments. Perception Editor owns app code, repository-specific specs, ADRs, implementation tickets and acceptance. A pinned integration index connects them. The blueprint's sample combined tree is refined: Chapter 17 links to app truth rather than copying a live roadmap. Alternative: keep both in the app repo; rejected because research growth and release timing would be coupled. No submodule or runtime dependency is introduced.

## PB-ADR-002 — Reviewed records are canonical

Markdown with metadata and source/claim registries is the source of truth. Search indexes are optional derived artifacts. Alternative: have every model write to one shared live database; deferred because the current need is auditable knowledge contributions, not a database service.

## PB-ADR-003 — Isolated contributions and serialized integration

Contributors own modules in separate branches/worktrees. One integrator handles shared registries, disputes and merge checks. This is a documented coordination process, not automatic locking or a hosted collaboration service. Remote access and repository licensing remain owner decisions.

## PB-ADR-004 — Bounded initial research slice

MPKB-02-005 starts with normalized sRGB components and a scalar Python oracle. Reject nonfinite/out-of-range input instead of silently clipping or inventing HDR behavior. Rec.709, PQ, HLG, log encodings and negative/extended domains remain explicit follow-ups. The parent topic stays research-draft. No claim is made about the Editor's current transfer implementation or camera output.

## PB-ADR-005 — Blueprint authorship and publication

Date: 2026-10-21. Status: [D] owner decision, stated in chat by the repository owner.

Collin (GitHub `chydes35`) authored MPKB-BLUEPRINT-2.0 and its V1.0 source (`Master_Photography_Knowledge_Base.md`) with AI assistance and authorizes public publication of the blueprint in this repository. This replaces the earlier "authorship not established / no public redistribution" status. It grants no reuse or redistribution license to third parties and does not select a project-wide license; that remains an owner decision. The preserved blueprint and its provenance hash are unchanged.
