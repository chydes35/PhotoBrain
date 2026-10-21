# Source registry

Only sources actually consulted for this contribution are registered here. IDs in the unchanged blueprint are scoped to that document; this registry uses `SRC-PB001-*` to avoid pretending its source audit has been repeated.

| ID | Issuer/title and version | Consulted sections / claims | Accessed | Reuse and limitations |
| --- | --- | --- | --- | --- |
| SRC-PB001-01 | [ICC sRGB encoding registry](https://registry.color.org/rgb-registry/srgb), identifies IEC 61966-2-1:1999 and Amendment 1 | Encoding characteristics: normalized range and forward transfer, CLM-PB001-01 | 2026-10-21 | Public technical summary; no page reproduction or blanket code license assumed. Full IEC normative text not obtained. |
| SRC-PB001-02 | [W3C CSS Color 4](https://www.w3.org/TR/2026/CRD-css-color-4-20261020/), Candidate Recommendation Draft 2026-10-20 | §10.2 inverse sRGB component transfer; §19 comparison, CLM-PB001-02 | 2026-10-21 | Draft; pin this edition and recheck before production adoption. Describes an extended-domain method; this oracle deliberately covers [0,1] only. No source code copied. |

No camera, benchmark product, Apple API or full-blueprint source claims are marked verified by this bootstrap. Reuse permission and licensing for production adoption remain a separate gate.
