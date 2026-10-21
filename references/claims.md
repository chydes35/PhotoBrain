# Claim registry

The classifications are claim-specific. Review evidence is in [PB-001](../tasks/PB-001.md). A verified equation does not make the entire module engineering-ready.

| ID | Claim / decision | Class and evidence grade | Support | Limits |
| --- | --- | --- | --- | --- |
| CLM-PB001-01 | Normalized sRGB encoding uses the piecewise function in MPKB-02-005 | [V], C (official technical summary) | SRC-PB001-01, encoding characteristics | Full IEC normative document not inspected; no camera inference |
| CLM-PB001-02 | Normalized inverse component transfer uses the piecewise function in MPKB-02-005 | [V], A for the pinned W3C draft's definition | SRC-PB001-02 §10.2; restricted to nonnegative normalized inputs | Draft authority for CSS, not proof of full IEC compliance |
| CLM-PB001-03 | Rounded forward/inverse knees require nonzero round-trip tolerances | [I], C (local numeric analysis) | Decimal-derived boundary values and reference tests | Tested scalar binary64 domain only; no global GPU/quantization guarantee |
| CLM-PB001-04 | This oracle rejects nonfinite/out-of-range input | [D], not a physical/source fact | PB-ADR-004 and invalid-input tests | A caller must separately select clipping, gamut or extended-range policy |

Grade A: directly consulted normative definition or replicated measurement; B: reviewed research; C: documented implementation or single measurement; D: unconfirmed/secondary. Do not treat the W3C draft as a final IEC standard.
