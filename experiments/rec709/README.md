# PB-002: normalized Rec.709 reference experiment

Purpose: support [MPKB-02-005](../../chapters/02-light-color-science/MPKB-02-005.md) with the rounded BT.709-6 source OETF, its partial algebraic inverse and same-number comparisons against the unchanged sRGB oracle. This is not a video decoder, display pipeline or camera characterization.

## Contract

- `encode_bt709_oetf(value)`: finite normalized linear source scalar in [0,1] to normalized signal.
- `invert_bt709_oetf(value)`: finite normalized signal in the rounded OETF's reachable range to a linear scalar; rejects its knee gap.
- Both return floating point without quantization. Inputs follow the same boundary as the sRGB oracle (PB-009): any `numbers.Real` except `bool`, converted once with `float()` (float subclasses at their `__float__` value); non-finite, overflowing, out-of-range or gap inputs raise `ValueError`; `bool`, `Decimal`, strings, `complex` and other types raise `TypeError`. `-0.0` is treated as `0.0`.
- Rounded constants and strict source knee are preserved. Floating-point comparisons use the computed upper-knee value (about 0.08124794403514046); equality/round trips are tolerance-based, not bitwise claims.
- After selecting a valid signal branch, the inverse result is bounded to that branch's linear domain: below 0.018 for the lower branch and at least 0.018 for the upper. This prevents floating rounding from crossing the discontinuity during re-encoding; it does not clip inputs or fill the signal gap.

The mathematical signal gap is `[0.081, 1.099*0.018^0.45-0.099)`. Gap rejection is **PhotoBrain policy**, not an ITU decoder rule. A legal 10-bit code can normalize into this interval: `(135-64)/876 ≈ 0.0810502283`. A general decoder therefore needs an explicit interpolation/approximation/other inverse policy after range handling; this partial inverse must not be substituted for it.

## Reproduce

Run from PhotoBrain's repository/worktree root:

```sh
python3 -m unittest discover -s tests -v
```

No dependencies, private fixtures, images, network or app imports are needed. The full suite includes the unchanged PB-001 tests.

## Independent vector provenance

Literal expected values were evaluated with Decimal precision 60, separately from the float implementation:

```python
from decimal import Decimal as D, localcontext
with localcontext() as context:
    context.prec = 60
    print(D('1.099') * D(0.18) ** D('0.45') - D('0.099'))
    print(((D(0.5) + D('0.099')) / D('1.099')) ** (D(1) / D('0.45')))
# 0.409007728864150435219157766569414727841193937546237742953658
# 0.259589400506285739878006128805123982781373384468868543934369
```

The neighboring vectors at linear 0.0179999 / 0.018 / 0.0180001 are 0.08099955 / 0.08124794403514047768… / 0.08124839465431212050…. Decimal inverse at encoded 0.081248 is 0.01800001241953031771…. A transcription of that last expected value was corrected against the independent calculation before implementation; no implementation result was used to set it.

PB-009 note (2026-10-21): the PB-002 values above used exact decimal inputs such as `D('0.18')`. The tests now use the exact binary value of each float input (`D(0.18)`), with branch thresholds compared as binary values (`Decimal(0.018)` is slightly below 0.018, so float 0.018 stays on the upper branch as in the code), and shared with the sRGB tests. Under that convention the knee neighbors are `0.08099955` / `0.08124794403514048` / `0.08124839465431213` and the inverse at 0.081248 is `0.01800001241953032` (binary64). Two PB-002 literals were 1 ulp off and were corrected: encode(0.001) = `0.0045000000000000005` (was `0.0045`) and encode(0.0180001) = `0.08124839465431213` (was `...212`); the other 14 were already correctly rounded. Vector and grid assertions now allow the measured maximum implementation error (3 ulp encode, 5 ulp inverse over a 300 001-input sample, Python 3.14.7 macOS arm64) instead of absolute `1e-14`; `test_literals_match_independent_decimal` re-derives every literal.

Tests catch: wrong curve or constants; inclusive lower knee; silently filled inverse gap; missing finite/range validation; wrong inverse exponent; and substitution of sRGB for Rec.709. Round trips cover generated reachable outputs only. They do not demonstrate behavior over every quantized video level or a full source-to-display chain.

## Observations and limits

Baseline: 8 PB-001 tests passed. First PB-002 run: new test import failed because `experiments.rec709` did not exist; original 8 still passed. Initial implementation passed 17 tests. Further boundary review found that inverse rounding could cross the join: the first upper signal inverted just below 0.018, and the final lower signal inverted to 0.018. Re-encoding then differed by approximately 0.000247944. Two regression tests reproduced this before the domain-preserving inverse correction. The corrected full suite executes 19 tests, 0 skipped. See [contribution/review](../../tasks/PB-002.md) for independent causal verification and review.

No speed, image quality, GPU error, file-tag correctness, original S5 mode behavior or production IEC/ITU implementation conformance was measured. This experiment supplies mathematical research evidence, not a shipping recommendation.
