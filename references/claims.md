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
| CLM-PB002-03 | Research inverse rejects the gap/invalid input and preserves its selected branch after float evaluation | [D] | PB-002 contract and boundary regression tests | Quantization can produce gap values; cannot be a general video decoder |
| CLM-PB002-04 | Source-curve inversion and BT.1886 screen response have different roles | [V]/A for source definitions; [I] for comparison | SRC-PB002-02 Annex 1; SRC-PB002-01 footnote | No BT.1886 implementation, measured display or reference-viewing validation |
| CLM-PB002-05 | Panasonic separately defines V-Log conversion | [V]/C for manufacturer definition; S5 applicability [U] | SRC-PB002-03 §§1/3 | Manual addresses Varicam; no original S5 mode claim or V-Log implementation |
| CLM-PB002-06 | sRGB and BT.709 equations give different signals for the listed equal numeric inputs | [I]/C | Independent Decimal vectors and comparison tests | Does not establish equal physical input/image state or appearance superiority |

## PB-003 claims and decisions

| ID | Claim / decision | Class and evidence grade | Support | Limits |
| --- | --- | --- | --- | --- |
| CLM-PB003-01 | DNG is TIFF-based and may organize multiple image resources/IFDs in one container | [V]/A | SRC-PB003-01 Chapter 1 “Introduction”; Chapter 2 “DNG Format Overview,” “SubIFD Trees,” printed p. 13 | Format specification, not validation of an arbitrary file |
| CLM-PB003-02 | DNG CFA and LinearRaw are distinct photometric interpretations; LinearRaw represents non-CFA or already-demosaiced data | [V]/A | SRC-PB003-01 Chapter 3 “Restrictions and Extensions to Existing TIFF Tags,” “PhotometricInterpretation,” printed pp. 22–23; SRC-PB003-05 “Custom compatibility preferences” | Per-resource semantics; no claim that every DNG carries either particular form |
| CLM-PB003-03 | DNG resource-role tags distinguish full-resolution raw, previews/reduced images and enhanced images; enhanced data is demosaiced at minimum | [V]/A | SRC-PB003-01 Chapter 2 “DNG Format Overview,” “Enhanced Image Data,” printed p. 17; Chapter 3, “NewSubFileType,” printed p. 20 | Does not characterize every resource or every DNG producer's processing pipeline |
| CLM-PB003-04 | Apple describes ProRAW as DNG-based, linearized/demosaiced and capable of multi-frame computational processing | [V]/B | SRC-PB003-02 02:43–05:12; SRC-PB003-03; SRC-PB003-06 | Vendor/product description, not payload validation for each file or capture mode |
| CLM-PB003-05 | Apple describes ProRes RAW as retaining Bayer-pattern video samples for later demosaicing | [V]/B | SRC-PB003-04, printed pp. 4–5 | Specific to ProRes RAW; does not support claims about other codecs |
| CLM-PB003-06 | A resource-level tuple for container, role, sample layout, encoding, demosaic state, processing history, temporal composition and evidence avoids collapsing distinct questions into one label | [I]/C | Synthesis of CLM-PB003-01–05 | Proposed research taxonomy; not an industry standard |
| CLM-PB003-07 | Confidence should be assigned per field; high-confidence observed payload properties require validated resource structure, while format-level declarations without payload validation remain medium | [D] | MPKB-11-001 confidence policy | Proposed operational convention, not a probability or source-defined grade |
| CLM-PB003-08 | Specific Panasonic LUMIX mode behavior remains unknown within this research | [U] | PB-003 scope; no authorized public sample or mode-specific primary definition inspected | Unknown does not mean unsupported or absent |
