# Knowledge index

Status records describe work actually present, not chapter completion. The [blueprint](blueprints/MPKB-BLUEPRINT-2.0.md) remains the complete proposed chapter map.

| Topic ID | Question | Status | Record |
| --- | --- | --- | --- |
| MPKB-02-005 | How do normalized sRGB and Rec.709 source transfers differ? | 0.2.1 research-draft; two bounded slices | [Transfer functions](chapters/02-light-color-science/MPKB-02-005.md) |
| MPKB-11-001 | What can file structure and metadata establish about an image input's representation? | 0.3.0 research-draft; four bounded slices | [Input representations](chapters/11-file-formats/MPKB-11-001.md) |
| MPKB-11-002 | What does a Panasonic RW2 file contain, and what do original DC-S5 files record? | 0.3.1 research-draft; sample results owner-reported (3 private files) | [Panasonic RW2](chapters/11-file-formats/MPKB-11-002.md) |

## Planned coverage

01 history; 02 light/color; 03 sensors; 04 capture pipelines; 05 optics; 06 computational photography; 07 editing algorithms; 08 LUMIX; 09 end-to-end systems; 10 glossary/references; 11 formats/metadata; 12 color management/display; 13 image-engine architecture; 14 ML/authenticity; 15 validation; 16 capture interfaces. No unlisted module is claimed complete.

Chapter 17 is represented by the [Perception Editor integration index](integrations/perception-editor.md); implementation plans remain authoritative in the app repository.

## Retrieval

1. Find the exact topic ID and read its summary, scope, status and prerequisites.
2. Follow source-to-claim records, including uncertainty and date/version limits.
3. Inspect reference code/test vectors when using an algorithm.
4. For app changes, follow the integration index to a pinned Editor revision and its own instructions.
5. Missing topics are research assignments, not permission to invent facts.

Search with `rg 'MPKB-02-005|MPKB-11-001|MPKB-11-002|sRGB|DNG|RW2' chapters references tasks`; do not crawl private compatibility paths.
