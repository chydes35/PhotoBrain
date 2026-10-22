# Changelog

## 2026-10-21 — PB-008 H.264 V16 author review

- Added ITU's V16 summary evidence for its new SEI interfaces, and full normative evidence confirming the sample-array, bit-depth and VUI defaults stated in the chapter.
- Confirmed V15 and V16 agree on the scoped sample organization and VUI facts; kept camera-pipeline and stream-specific inferences separate.
- Integration review corrected the separation between eleven new SEI messages and separate VSEI extensions, and changed the full-text source link to the direct official PDF. A separate verification agent reproduced and checked both fixes; 19 repository reference tests and `git diff --check` passed. No code, sample files, local media or standard text were added.
- `MPKB-11-001` 0.2.1 → 0.2.2: front matter lists `SRC-PB008-01`/`SRC-PB008-02` and the PB-008 contribution; INDEX updated. PR #12 (PB-009) also sets this module to 0.2.2 from the same base, so whichever of PR #11/#12 merges second must take 0.2.3 and combine both contributions on the `contribution:` line.
- PR #11 review fixes (Grok Bot, `research/PB-008-fixes-grokbot`, at the maintainer's request; independent re-review pending): `CLM-PB005-06` cites Annex E.2.1 only, worded as in PR #12; `CLM-PB005-08` keeps its PB-005 wording and points to `CLM-PB008-01`–`03`, with its [U] narrowed to V16 clauses outside that review; `CLM-PB008-01` regraded B → C at `d2558dd`, then re-supported from V16 Annex D.1.1 SEI payload syntax (pp. 335–337, checked against V15's D.1.1) and graded A, with its [I] limit moved to the Limits column; `CLM-PB008-02` adds §7.3.2.1.1 (p. 46); `CLM-PB008-03` and `SRC-PB008-02` extend E.2.1 to p. 438.

## 2026-10-21 — PB-008 assigned

- Assign review of current ITU-T H.264 V16 clauses against the existing H.264 V15-based representation claims in `MPKB-11-001` to `research/PB-008-codex` from base `6a7f30e`.
- Scope is standard-backed technical differences and claim updates only; no local media, decoder, dataset, or application behavior changes.

## 2026-10-21 — Post-merge cleanup

- Add `MPKB-11-001` (0.2.1) to the index and search hint.
- Replace commit IDs that exist only in local history with their published equivalents.
- Mark PB-002 merged via PR #2.
- Grade `CLM-PB005-05` and `CLM-PB005-06` B, not A: the full H.264 V15 text was not retrieved.
- `MPKB-11-001`: add ProRAW companded storage, `DNGVersion`, CFA tag requirements and mask/depth `NewSubFileType` roles (`CLM-PB003-09`–`12`, DNG 1.7.1.0 re-read); split one summary label; clarify the RGB contrast for conventional video. Topic remains `research-draft`.
- Update stale integration states (`ee9b41c`): PB-001 on `main` since bootstrap `7e8f304`; PB-002 merged via PR #2 (`3be85b0`); PB-005 prerequisite records PB-003 merged via PR #6 (`da5f827`).
- Apply PR #8 review nits: restore `CLM-PB005-05` and `CLM-PB005-06` to A after consulting the full H.264 V15 (08/2024) text (Table 6-1 p. 23; §7.4.2.1.1 pp. 77–78; E.2.1 pp. 431–436); record both DNG 1.7.1.0 PDF copies and WWDC21 10160 timestamps; cite the ProRes RAW white paper (p. 4) for the per-pixel RGB meaning; note that Apple does not name the semantic-mask tag; complete PB-003/PB-004/PB-005 records.

## 2026-10-21 — PB-004 open-source ecosystem research

- Add a source-linked inventory of knowledge retrieval, image/video research tools, neural imaging projects, and photography datasets.
- Record project-specific license boundaries, model/data caveats, and evidence limitations; generated retrieval remains subordinate to reviewed Markdown and claim/source records.
- Recommend a measured keyword-versus-embedding retrieval trial before adopting a database; graph retrieval and large dataset downloads remain deferred pending demonstrated need.
- No dependencies, code, datasets, application behavior, or private workspace data added.
- Content commit `9f6728a`; published via PR #5, merged as `1ff8f50`.

## 2026-10-21 — PB-005 research draft

- Extended `MPKB-11-001` with source-backed JFIF, PNG and H.264 coding examples; kept file/container layers, source-image fidelity and camera processing history distinct.
- Registered four sources and eight claims. Two independent reviewers checked cited clauses and corrections. `git diff --check` passed; no code, samples, dependencies or app changes were added.
- H.264 technical claims are pinned to V15 (08/2024); ITU lists V16 (06/2026) as current, but that edition's technical text was not reviewed. The full V15 PDF exceeded the browser retrieval limit, so cited clauses were checked using official indexed excerpts. Topic remains `research-draft`.
- Content commit `b4ebce6`; published via PR #6, merged as `da5f827`.

## 2026-10-21 — PB-005 assigned

- Assign JPEG, PNG and AVC/H.264 representation research to `research/PB-005-codex` from base `fb7e8fd`.
- Scope to official format evidence and distinguish coded representation from container, metadata and capture history; no private samples, decoder, or app behavior changes.

## 2026-10-21 — PB-003 research draft

- Added `MPKB-11-001`, a bounded, evidence-backed taxonomy for classifying image resources and video tracks without relying on filename extensions alone.
- Registered six official Adobe/Apple sources and eight task-prefixed claims. The draft leaves Panasonic LUMIX mode behavior and broader codec coverage explicitly unknown; it includes no app recommendation, code, samples, or copied source text.
- Validation: Adobe DNG facts and Apple ProRAW/ProRes RAW claims independently checked against official sources. Review corrected DNG headings/page citations and clarified the confidence threshold for validated payload properties. `git diff --check` passed after those corrections. Status remains `research-draft` because format coverage, samples and implementation gates are open.
- Content commit `67b50e5`; published via PR #6, merged as `da5f827`.

## 2026-10-21 — PB-003 assigned

- Claim MPKB-11-001 input representation research on `research/PB-003-codex` from base `f6217b1` (assignment `bdd444b`).
- Scope the contribution to source-backed representation classes and metadata evidence; no local media, Editor code, or application behavior changes.

## 2026-10-21 — Blueprint authorship (PB-ADR-005)

- Record owner authorship (with AI assistance) of the V2 blueprint and V1.0 source, and authorization to publish it in this repository. No license granted; blueprint and provenance hash unchanged.

## 2026-10-21 — PB-002 Rec.709 research

- Extend MPKB-02-005 to 0.2.0 with primary-source Rec.709 encoding, inverse-domain analysis and sRGB numeric comparisons; parent remains research-draft.
- Distinguish source encoding/inversion, BT.1886 display response and camera log; preserve original sRGB oracle/tests unchanged.
- Add a scalar Rec.709 OETF and explicitly partial inverse, independent Decimal vectors and 11 tests. Gap rejection is a research policy, not an ITU decoder mandate.
- Boundary review reproduced inverse rounding across both sides of the discontinuity; preserve the selected inverse branch and add signal-domain regression checks.
- Register task-specific source/claim IDs and review evidence. No app behavior, saved schema, private data or performance assumptions changed.

## 2026-10-21 — Local knowledge bootstrap

- Preserve MPKB-BLUEPRINT-2.0 unchanged and record provenance; V1 remains unavailable.
- Establish separate knowledge ownership, contribution/review templates, IDs and source/claim registries.
- Establish a pinned Editor integration index and workspace migration record.
- Add first MPKB-02-005 research slice and executable sRGB reference/tests; broader transfer coverage remains draft.
- No application behavior, schema, performance budget, release or runtime dependency changes.
