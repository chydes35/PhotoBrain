# Source registry

Only sources actually consulted for this contribution are registered here. IDs in the unchanged blueprint are scoped to that document; this registry uses `SRC-PB001-*` to avoid pretending its source audit has been repeated.

| ID | Issuer/title and version | Consulted sections / claims | Accessed | Reuse and limitations |
| --- | --- | --- | --- | --- |
| SRC-PB001-01 | [ICC sRGB encoding registry](https://registry.color.org/rgb-registry/srgb), identifies IEC 61966-2-1:1999 and Amendment 1 | Encoding characteristics: normalized range and forward transfer, CLM-PB001-01 | 2026-10-21 | Public technical summary; no page reproduction or blanket code license assumed. Full IEC normative text not obtained. |
| SRC-PB001-02 | [W3C CSS Color 4](https://www.w3.org/TR/2026/CRD-css-color-4-20261020/), Candidate Recommendation Draft 2026-10-20 | §10.2 inverse sRGB component transfer; §19 comparison, CLM-PB001-02 | 2026-10-21 | Draft; pin this edition and recheck before production adoption. Describes an extended-domain method; this oracle deliberately covers [0,1] only. No source code copied. |

No camera, benchmark product, Apple API or full-blueprint source claims are marked verified by this bootstrap. Reuse permission and licensing for production adoption remain a separate gate.

## PB-002 additions

All accessed 2026-10-21. These definitions were directly consulted; their listing does not certify a production pipeline.

| ID | Issuer/title and exact edition | Consulted sections / claims | Reuse and limitations |
| --- | --- | --- | --- |
| SRC-PB002-01 | [ITU-R BT.709-6, June 2015](https://www.itu.int/rec/R-REC-BT.709-6-201506-I/en), official [English document](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.709-6-201506-I!!PDF-E.pdf) | §1 item 1.2 and footnote (printed p3); §3 item 3.1 (p4): source OETF and primary-signal use, CLM-PB002-01 | Official normative source; edition listed in force when accessed. ITU copyright/all rights reserved; full document not vendored. Mathematical reference does not establish a camera's encoding. |
| SRC-PB002-02 | [ITU-R BT.1886, March 2011](https://www.itu.int/rec/R-REC-BT.1886-0-201103-I/en), official [English document](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1886-0-201103-I!!PDF-E.pdf) | Annex 1 (printed p2): display EOTF, screen-luminance parameters and nominal 10-bit normalization, CLM-PB002-04 | Official normative source; separate display role. Copyright/all rights reserved; no display oracle or conformance test implemented here. |
| SRC-PB002-03 | Panasonic, [V-Log/V-Gamut Reference Manual](https://pro-av.panasonic.net/en/cinema_camera_varicam_eva/support/pdf/VARICAM_V-Log_V-Gamut.pdf), Rev1.0, November 28, 2014 | §§1 and 3 (printed pp2–3): distinct camera-log definition, CLM-PB002-05 | Manufacturer source addresses Varicam; original S5 applicability remains unknown. Linked, not redistributed; no V-Log code copied or implemented. |
