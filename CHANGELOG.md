# Changelog

## 2026-10-22 — PB-010 review corrections (MPKB-11-001 0.3.1)

- Correct availability wording: IEC lists the ISO/IEC 23008-12:2025 and ISO/IEC 14496-12:2026 base publications at CHF 0; their full technical text remains unconsulted. Keep the syntax claims [U].
- Regrade ISO publisher-catalog metadata [V]/C, retain unsupported normative details as [U]/D, and record ISO/IEC 14496-12:2026 stage 90.92 and expected DIS replacement.
- Add IEC Webstore source records `SRC-PB010-06` and `SRC-PB010-07`, complete the PB-010 task-record template, and state the explicit authorization for shared-file changes. Record that the task-board row landed with the content commit; no history rewrite was made.
- Findings were checked independently. At corrected content commit `0e514b6656a63fbc191d045cd38247c7602e2e20`, all 32 tests passed, `git diff --check` was clean, and all 19 cited source IDs and 27 claim IDs resolved exactly once. The corrected contribution remains research-draft; follow-up review of the corrected head is pending.

## 2026-10-22 — PB-010 HEIF/HEIC research draft (MPKB-11-001 0.3.0)

- Add a bounded HEIF/HEIC evidence slice to MPKB-11-001 and register `SRC-PB010-01`–`05` plus `CLM-PB010-01`–`04`.
- Grade Apple API and WWDC17 statements [V]/C for their documented vendor scope. Mark HEIF/ISOBMFF normative details and the 2026 amendment's technical meaning [U]/D because their full normative text was not consulted; no HEIF box or codec syntax is asserted from memory.
- Update the topic and index from 0.2.3 to 0.3.0. The topic remains research-draft and has not been independently reviewed at a specific commit.
- Checks: `python3 -m unittest discover -s tests -v` — 32 tests, `OK`; `git diff --check` clean; every source and claim ID cited by MPKB-11-001 resolves exactly once. No code or media files added. PR #16 is open; independent review remains pending.

## 2026-10-22 — PB-007 Skeptic review fixes (MPKB-11-002 0.3.1)

- Skeptic (`ee0c3372…`) reviewed PR #10 head `c7e6878`: NEEDS FIXES, nothing blocking. All 17 findings addressed on `research/PB-007-grokbot` (some as partial fixes or recorded deviations; see `tasks/PB-007.md`). Topic stays research-draft; `MPKB-11-002` 0.2.0 → 0.3.0.
- Skeptic re-reviewed `51fd965` (round 2): NEEDS FIXES (minor), one privacy should-fix and seven nits, all addressed in 0.3.1 (`21146e8`). Privacy: per-sample green-pair means, the twelve preview correlations, neutral-block medians and WB reciprocals, step and clipping percentages, Orientation, BurstMode and black levels replaced with ranges across samples or 'within X' statements; no value is tied to an individual sample. Nits: 'of visible pixels' dropped (the denominator is unrecorded); S5 still-RAW bit depth is [U] in both the summary and `CLM-PB007-02`; LibRaw saturation at `decoders_libraw.cpp` 526–529 cited; `open.cpp` range corrected to 636–688; this entry says 'addressed'; the PB-007 owned-files bullet fixed. The proposed owner-reported-results decision was not added to `DECISIONS.md` (integrator-owned); it is written up in `tasks/PB-007.md`. `MPKB-11-002` 0.3.0 → 0.3.1.
- Skeptic re-reviewed `21146e8` (round 3): NEEDS FIXES, one line (INDEX still said 0.3.0; now 0.3.1), plus nits, all addressed with the module kept at 0.3.1. LibRaw citation widened to `decoders_libraw.cpp` 461–462 (14-bit bound and saturation value; 12-bit saturates to 4095). Privacy: every per-sample range end rounded outward to coarse values (for example clipping 8–27%, step > 1 7–12%, correlations to 0.1), so each range still brackets the earlier values and every conclusion holds. Round 2's verdict recorded.
- Registries and index, at Collin's request: add `MPKB-11-002` to INDEX and the search hint; add `SRC-PB007-01`–`11` to `references/sources.md` and `CLM-PB007-01`–`28` to `references/claims.md` (previously only proposed in `tasks/PB-007.md`). Append-only; no other task's rows changed. Every ID the chapter cites resolves.
- Labels: results measured on the 3 owner-provided S5 samples go from [V]/C to [I]/C, owner-reported (inputs not redistributable; scripts not retained), because CONTRIBUTING requires reproducible input, settings and results. Tag meanings and the step map are [I]. Panasonic manuals and pages are graded A (blueprint §1.2 normative tier) instead of B. The shot-noise [H] becomes [U]. `CLM-PB007-20` and the LibRaw support note get labels.
- Corrections: LibRaw chooses 11 or 14 samples per block from bit depth, not data size. LibRaw is pinned to tag 0.22.1 (`b860248`, the version rawpy 0.27.1 bundles) with line numbers re-checked. ExifTool 13.55 and 13.59 source compared: no change to the tags read. Citations fixed (JpgFromRaw note at `PanasonicRaw.pm` line 204; Blackmagic recorders at manual p. F-28; `CLM-PB007-10` cites the counting argument). The numpy decoder is described as a transcription check. ≡ 1 (mod 16) explained by decoder arithmetic. The upper end of the 8147-value histogram range marked [U]. Step-share rounding reconciled (a 0.1-point difference in one sample) and the start-value counting convention marked [U].
- Privacy: exact per-file preview byte lengths, Gamma and DistortionScale replaced with ranges (0.3.0); remaining per-sample values replaced with ranges (0.3.1). A private-data scan of the diff found no file names, serials, GPS, capture dates or hashes.
- Checks (0.3.0 and again for 0.3.1): 32 tests OK (Python 3.14.7); `git diff --check` clean; every ID the chapter cites resolves. No code, sample files or private data added.

## 2026-10-22 — PB-012 status-record cleanup

- Board: PB-008 merged as PR #11 (`cbbd0eb`, 6:45 AM CDT) and PB-011 merged as PR #14 (`9a916cd`, 6:39 AM CDT); add the PB-012 row.
- `tasks/PB-006.md`: merged as PR #9 (`a0034d4`, 7:12 PM CDT 2026-10-21), replacing "awaiting integrator review". `tasks/PB-008.md` and `tasks/PB-011.md`: integration commits filled in; pre-merge "pending" statements marked superseded.
- `tasks/PB-011.md`: [I] items confirmed from CI logs: PR #14's run used `ubuntu-24.04` image `20261012.334.1` with CPython 3.14.8, 3.11.17 and 3.9.25, and the bounds tests passed on the runner's glibc (version not measured). A later run on image `20261021.345.10` used 3.14.9. `main` requires `tests (3.9)`, `tests (3.11)` and `tests (3.14)`.
- Status text only; no knowledge, registry, index, code or test changes. Independently reviewed by Skeptic at `1d61c8f` (holds up); nits applied in `e2c1cc9`.

## 2026-10-22 — PB-008 merged with current `main`

- Merge `origin/main` @ `94093d9` (PR #12, PB-009, which includes PR #9, PB-006) into PR #11. PR #12 merged first, so this PR takes `MPKB-11-001` 0.2.3 (front matter and INDEX), and the `contribution:` line combines to `PB-003 + PB-005 + PB-008 + PB-009 (citation corrections)`.
- Status corrections: PB-006 merged as PR #9 and PB-009 as PR #12; the PR #11 review fixes were re-reviewed by Skeptic (holds up).

## 2026-10-21 — PB-008 H.264 V16 author review

- Added ITU's V16 summary evidence for its new SEI interfaces, and full normative evidence confirming the sample-array, bit-depth and VUI defaults stated in the chapter.
- Confirmed V15 and V16 agree on the scoped sample organization and VUI facts; kept camera-pipeline and stream-specific inferences separate.
- Integration review corrected the separation between eleven new SEI messages and separate VSEI extensions, and changed the full-text source link to the direct official PDF. A separate verification agent reproduced and checked both fixes; 19 repository reference tests and `git diff --check` passed. No code, sample files, local media or standard text were added.
- `MPKB-11-001` 0.2.1 → 0.2.2: front matter lists `SRC-PB008-01`/`SRC-PB008-02` and the PB-008 contribution; INDEX updated. PR #12 (PB-009) also sets this module to 0.2.2 from the same base, so whichever of PR #11/#12 merges second must take 0.2.3 and combine both contributions on the `contribution:` line.
- PR #11 review fixes (Grok Bot, `research/PB-008-fixes-grokbot`, at the maintainer's request; Skeptic re-reviewed them: holds up): `CLM-PB005-06` cites Annex E.2.1 only, worded as in PR #12; `CLM-PB005-08` keeps its PB-005 wording and points to `CLM-PB008-01`–`03`, with its [U] narrowed to V16 clauses outside that review; `CLM-PB008-01` regraded B → C at `d2558dd`, then re-supported from V16 Annex D.1.1 SEI payload syntax (pp. 335–337, checked against V15's D.1.1) and graded A, with its [I] limit moved to the Limits column; `CLM-PB008-02` adds §7.3.2.1.1 (p. 46); `CLM-PB008-03` and `SRC-PB008-02` extend E.2.1 to p. 438.

## 2026-10-21 — PB-008 assigned

- Assign review of current ITU-T H.264 V16 clauses against the existing H.264 V15-based representation claims in `MPKB-11-001` to `research/PB-008-codex` from base `6a7f30e`.
- Scope is standard-backed technical differences and claim updates only; no local media, decoder, dataset, or application behavior changes.

## 2026-10-22 — PB-011 GitHub Actions CI

- Add `.github/workflows/tests.yml`: on `pull_request` and `push` to `main`, run `python -m unittest discover -s tests -v` for Python 3.9, 3.11 and 3.14 (`fail-fast: false`, `permissions: contents: read`). Job names `tests (3.9)`, `tests (3.11)`, `tests (3.14)` are stable for use as required checks.
- Runner pinned to `ubuntu-24.04`: `ubuntu-latest` is migrating to Ubuntu 26.04 between 2026-10-19 and 2026-11-19 ([actions/runner-images#14748](https://github.com/actions/runner-images/issues/14748)), and Python 3.9.25 has no 26.04 build. Dropping 3.9 or moving the runner to 26.04 is a later decision.
- Actions pinned to full SHAs: `actions/checkout` `3d3c42e…` (v7.0.1) with `persist-credentials: false`; `actions/setup-python` `6d4fd22…` (v7.1.0). No Dependabot added.
- Allowlist `/.github/` in `.gitignore` as a reviewed tooling exception (CI workflows only), not a knowledge root.
- The suite uses only the standard library, no network, no model and no private paths. Skeptic measured the ulp bounds on glibc 2.41: sRGB encode 5/5, decode 7/7, Rec.709 encode 3/3, inverse 4/5 (max/bound), so three bounds have zero margin. Not yet run on GitHub's runners.
- Review: Skeptic reviewed `ddd371d` (NEEDS FIXES), then `0139af7` (HOLDS UP); nits applied. `.github/` allowlist narrowed to `.github/workflows/`. Making a check required in branch protection is Collin's setting; no GitHub settings changed.

## 2026-10-21 — PB-009 post-merge review fixes

- Act as integrator for the confirmed findings of the Skeptic review of `main` @ `6a7f30e`; retroactively record PR #8 (merge `6a7f30e`, head `418afa4`; its review was by the same agent identity as its author and `418afa4` was not re-reviewed) in `tasks/PB-009.md`. Separate-agent review of PB-009: Skeptic (`6a7f30e`, re-review `0d8b381`); final pass at `ddcf56d` held up, with its doc fixes in `b1e32a4`. Merged as [PR #12](https://github.com/chydes35/PhotoBrain/pull/12) (`94093d9`) at 6:06 AM CDT 2026-10-22.
- sRGB oracle and tests: six literals corrected to correctly rounded Decimal values (e.g. `decode(0.5)` = `0.21404114048223244`) and re-derived in a test; vector checks allow the measured per-function maximum error (sRGB 5 ulp encode / 7 ulp decode, Rec.709 3 / 5) plus a Decimal grid check; explicit test of the `-2.85e-8` encode step at `0.0031308`; `encode_srgb(1.0)` now exactly `1.0`. Both reference modules raise `TypeError` for `bool`/`Decimal`/other types and `ValueError` for bad numbers, and map `-0.0` to `0.0`. Rec.709 literals use the same exact-binary-input convention (two corrected by 1 ulp); inputs may be any `numbers.Real` except `bool`. 32 tests pass on Python 3.14.7, 3.11.16 and 3.9.6.
- Registries: `CLM-PB001-01`/`02` relabelled [I] and graded D (secondary summaries; IEC text not obtained); `CLM-PB005-02` APP0 applies to all JFIF; `CLM-PB005-06` cites Annex E.2.1 only. `MPKB-02-005` 0.2.1 and `MPKB-11-001` 0.2.2.
- Records: dated notes in PB-001 to PB-005 for published branches/PRs and unretained review output; SRC-PB003-01 access note re-tested; absolute local paths replaced with placeholders in four public files (Git history unchanged). No CI or GitHub settings changed.

## 2026-10-21 — PB-006 assigned

- Assign a reproducible keyword-versus-embedding retrieval comparison on the pinned approved Markdown corpus, with a hand-checked query set and retrieval metrics.
- Initial scope used installed local tools and tracked knowledge files only; the user later authorized the benchmark model download to the external SSD. No datasets, private data, or app behavior changes.

## 2026-10-21 — PB-006 retrieval comparison

- Record the pinned-corpus SQLite FTS5 baseline and Nomic Embed Text v1.5 cosine comparison over 52 chunks and 12 queries; keyword Recall@5/MRR@5 0.826/0.628 versus embedding 0.708/0.597. Embedding expected claim-ID presence was 16/22 versus keyword's 13/22, at higher one-run latency. The Apache-2.0 model was stored on the external SSD; no model data entered Git. No application or database adoption decision follows.
- Publish the reviewed contribution as [PR #9](https://github.com/chydes35/PhotoBrain/pull/9); merged as `a0034d4` at 7:12 PM CDT 2026-10-21.

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
