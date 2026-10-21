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

## PB-003 additions

All accessed 2026-10-21. Public manufacturer/specification sources only; links are references, not blanket rights to reproduce or decode.

| ID | Issuer/title and exact edition | Consulted sections / claims | Reuse and limitations |
| --- | --- | --- | --- |
| SRC-PB003-01 | Adobe, [Digital Negative (DNG) Specification](https://helpx.adobe.com/content/dam/help/en/camera-raw/digital-negative/jcr_content/root/content/flex/items/position/position-par/download_section_733958301/download-1/DNG_Spec_1_7_1_0.pdf), version 1.7.1.0, September 2023 | Chapter 1 “Introduction”; Chapter 2 “DNG Format Overview,” printed pp. 13, 17; Chapter 3 “Restrictions and Extensions to Existing TIFF Tags,” printed pp. 20, 22–23: TIFF 6.0 basis, IFD/resource roles, NewSubFileType, PhotometricInterpretation, CFA and LinearRaw; CLM-PB003-01–03 | Official specification PDF linked, not vendored. Tag semantics describe format-conforming resources; no arbitrary payload was inspected. |
| SRC-PB003-02 | Apple, [Capture and process ProRAW images](https://developer.apple.com/videos/play/wwdc2021/10160/), WWDC21 session 10160 | 02:43–05:12: ProRAW DNG, linearized/demosaiced data and possible multi-frame fusion; CLM-PB003-04 | Vendor session, not a conformance test of individual files or every device/mode. |
| SRC-PB003-03 | Apple Support, [About Apple ProRAW](https://support.apple.com/en-us/119916), current page as accessed | “About Apple ProRAW” and file-format discussion: DNG and computational processing; CLM-PB003-04 | Support article can change; cited for broad product description, with session above for technical detail. |
| SRC-PB003-04 | Apple, [Apple ProRes RAW white paper](https://www.apple.com/final-cut-pro/docs/Apple_ProRes_RAW.pdf), May 2023 | Printed pp. 4–5: conventional demosaic path and Bayer-pattern ProRes RAW representation; CLM-PB003-05 | Manufacturer white paper describes ProRes RAW only; no generalization to unrelated codecs. |
| SRC-PB003-05 | Adobe, [Adobe DNG Converter](https://helpx.adobe.com/camera-raw/desktop/dng-and-file-formats/adobe-dng-converter.html), “Custom compatibility preferences” | “Linear (demosaiced)” option and mosaic/linear conversion discussion; corroborates CLM-PB003-02 | Current web documentation; settings behavior is not evidence about a specific camera file. |
| SRC-PB003-06 | Apple Developer Documentation, [Capturing photos in RAW and Apple ProRAW formats](https://developer.apple.com/documentation/avfoundation/capturing-photos-in-raw-and-apple-proraw-formats), current page as accessed | RAW and ProRAW capture/representation distinction; supports scope and terminology for CLM-PB003-04 | API documentation, not a general file-format standard or proof of output contents for every capture configuration. |
