# Claim registry

The classifications are claim-specific. Review evidence is in [PB-001](../tasks/PB-001.md). A verified equation does not make the entire module engineering-ready.

| ID | Claim / decision | Class and evidence grade | Support | Limits |
| --- | --- | --- | --- | --- |
| CLM-PB001-01 | Normalized sRGB encoding uses the piecewise function in MPKB-02-005 | [V], C (official technical summary) | SRC-PB001-01, encoding characteristics | Full IEC normative document not inspected; no camera inference |
| CLM-PB001-02 | Normalized inverse component transfer uses the piecewise function in MPKB-02-005 | [V], A for the pinned W3C draft's definition | SRC-PB001-02 §10.2; restricted to nonnegative normalized inputs | Draft authority for CSS, not proof of full IEC compliance |
| CLM-PB001-03 | Rounded forward/inverse knees require nonzero round-trip tolerances | [I], C (local numeric analysis) | Decimal-derived boundary values and reference tests | Tested scalar binary64 domain only; no global GPU/quantization guarantee |
| CLM-PB001-04 | This oracle rejects nonfinite/out-of-range input | [D], not a physical/source fact | PB-ADR-004 and invalid-input tests | A caller must separately select clipping, gamut or extended-range policy |

Grade A: directly consulted normative definition or replicated measurement; B: reviewed research; C: documented implementation or single measurement; D: unconfirmed/secondary. Do not treat the W3C draft as a final IEC standard.

## PB-002 claims and decisions

| ID | Claim / decision | Class and evidence grade | Support | Limits |
| --- | --- | --- | --- | --- |
| CLM-PB002-01 | Rounded BT.709 source OETF uses lower branch below 0.018 and upper branch at/above it | [V]/A | SRC-PB002-01 §1 item 1.2; §3 item 3.1 | Nominal normalized reference; no actual camera source behavior determined |
| CLM-PB002-02 | Rounded equations leave a gap from 0.081 to the upper-knee output; an algebraic inverse exists on the reachable range | [I]/C | Local derivation and independent Decimal/source review | Real-number range analysis with floating-point tolerances; not a decoder requirement |
| CLM-PB002-03 | Research inverse rejects that gap and invalid numeric inputs | [D] | PB-002 contract and tests | Quantization can produce gap values; cannot be a general video decoder |
| CLM-PB002-04 | Source-curve inversion and BT.1886 screen response have different roles | [V]/A for source definitions; [I] for comparison | SRC-PB002-02 Annex 1; SRC-PB002-01 footnote | No BT.1886 implementation, measured display or reference-viewing validation |
| CLM-PB002-05 | Panasonic separately defines V-Log conversion | [V]/C for manufacturer definition; S5 applicability [U] | SRC-PB002-03 §§1/3 | Manual addresses Varicam; no original S5 mode claim or V-Log implementation |
| CLM-PB002-06 | sRGB and BT.709 equations give different signals for the listed equal numeric inputs | [I]/C | Independent Decimal vectors and comparison tests | Does not establish equal physical input/image state or appearance superiority |
