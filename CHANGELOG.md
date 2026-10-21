# Changelog

## 2026-10-21 — PB-005 assigned

- Assign JPEG, PNG and AVC/H.264 representation research to `research/PB-005-codex` from base `acbdf2c`.
- Scope to official format evidence and distinguish coded representation from container, metadata and capture history; no private samples, decoder, or app behavior changes.

## 2026-10-21 — PB-003 research draft

- Added `MPKB-11-001`, a bounded, evidence-backed taxonomy for classifying image resources and video tracks without relying on filename extensions alone.
- Registered six official Adobe/Apple sources and eight task-prefixed claims. The draft leaves Panasonic LUMIX mode behavior and broader codec coverage explicitly unknown; it includes no app recommendation, code, samples, or copied source text.
- Validation: Adobe DNG facts and Apple ProRAW/ProRes RAW claims independently checked against official sources. Review corrected DNG headings/page citations and clarified the confidence threshold for validated payload properties. `git diff --check` passed after those corrections. Status remains `research-draft` because format coverage, samples and implementation gates are open.
- Integrated locally from author commit `1e0a622` as `cf45cbd`; no push or publication.

## 2026-10-21 — PB-003 assigned

- Claim MPKB-11-001 input representation research on `research/PB-003-codex` from base `7098ed3`.
- Scope the contribution to source-backed representation classes and metadata evidence; no local media, Editor code, or application behavior changes.

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
