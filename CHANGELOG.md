# Changelog

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
