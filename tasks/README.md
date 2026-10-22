# Task board

The integrator serializes this file; contributors request assignment before changing another owner's files. Assignment is not an automatic lock.

| ID | Owner/model | Module and scope | State | Record |
| --- | --- | --- | --- | --- |
| PB-001 | Codex / model version not exposed | Bootstrap + MPKB-02-005 normalized sRGB slice | on `main` since bootstrap commit `7e8f304`; topic remains research-draft | [Contribution](PB-001.md) |
| PB-002 | Codex / model version not exposed | Extend MPKB-02-005 with independently sourced Rec.709 comparison | merged; topic remains research-draft | [Contribution/review](PB-002.md); [PR #2](https://github.com/chydes35/PhotoBrain/pull/2); merge `3be85b0` |
| PB-003 | Codex / model version not exposed | MPKB-11-001: classify image input representations from payload and metadata | merged; topic remains research-draft | [Contribution](PB-003.md); [PR #6](https://github.com/chydes35/PhotoBrain/pull/6); merge `da5f827` |
| PB-004 | Codex / model version not exposed | Open-source ecosystem and retrieval research inventory | merged; inventory remains research-draft | [Contribution](PB-004.md); [PR #5](https://github.com/chydes35/PhotoBrain/pull/5); merge `1ff8f50` |
| PB-005 | Codex / model version not exposed | Extend MPKB-11-001 with source-backed JPEG, PNG and AVC/H.264 rendered-representation evidence | merged; topic remains research-draft | [Contribution](PB-005.md); [PR #6](https://github.com/chydes35/PhotoBrain/pull/6); merge `da5f827` |
| PB-006 | Codex / model version not exposed | Benchmark local keyword retrieval against one embedding retriever on approved Markdown corpus | comparison complete on task branch; awaiting integrator review | [Contribution](PB-006.md) |
| PB-008 | Codex / model version not exposed | Review current ITU-T H.264 V16 technical text against PB-005's V15-based claims; update the bounded H.264 section | author, independent clause and integration reviews complete on `research/PB-008-codex` from `6a7f30e`; PR #11 review fixes on `research/PB-008-fixes-grokbot` reviewed by Skeptic (holds up); awaiting Collin's approval to fold into PR #11 | [Contribution](PB-008.md) |
| PB-009 | PhotoBrain (Grok Bot) / model version not exposed | Post-merge review fixes (Skeptic review of `main` @ `6a7f30e`); acts as integrator for shared registries/index; owned files listed in the record | Skeptic re-review fixes complete; final Skeptic re-review pending; local commits on `research/PB-009-grokbot` from `6a7f30e`; not pushed | [Contribution](PB-009.md) |

PB-002/PB-003/PB-005 may research independently; shared files are integrated serially. Representation topics must inspect actual format definitions before recommending app changes. Other chapter/module IDs remain proposed by the blueprint.
