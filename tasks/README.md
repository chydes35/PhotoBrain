# Task board

The integrator serializes this file; contributors request assignment before changing another owner's files. Assignment is not an automatic lock.

| ID | Owner/model | Module and scope | State | Record |
| --- | --- | --- | --- | --- |
| PB-001 | Codex / model version not exposed | Bootstrap + MPKB-02-005 normalized sRGB slice | integrated locally; topic remains draft | [Contribution](PB-001.md) |
| PB-002 | Codex / model version not exposed | Extend MPKB-02-005 with independently sourced Rec.709 comparison | integrated locally; topic remains draft | [Contribution/review](PB-002.md); content commit `465e7e7` |
| PB-003 | Codex / model version not exposed | MPKB-11-001: classify image input representations from payload and metadata | assigned; research in progress | [Contribution](PB-003.md); branch `research/PB-003-codex`; base `7098ed3` |
| PB-005 | Codex / model version not exposed | Extend MPKB-11-001 with source-backed JPEG, PNG and AVC/H.264 rendered-representation evidence | assigned; research in progress | [Contribution](PB-005.md); branch `research/PB-005-codex`; base `acbdf2c` |

PB-002/PB-003/PB-005 may research independently; shared files are integrated serially. Representation topics must inspect actual format definitions before recommending app changes. Other chapter/module IDs remain proposed by the blueprint.
