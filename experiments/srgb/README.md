# PB-001 normalized sRGB reference

This independent scalar Python oracle supports [MPKB-02-005](../../chapters/02-light-color-science/MPKB-02-005.md). It is a research reference, not Editor production code.

Run `python3 -m unittest discover -s tests -v` from the PhotoBrain root. No packages, photo files, network or app frameworks are required.

Each function accepts a `numbers.Real` other than `bool` (`int`, `float`, `fractions.Fraction`, and types registered as Real), converts it once with `float()` and computes from that binary64 value; a float subclass is evaluated at its `__float__` value. A value that is non-finite, overflows `float` or lies outside [0,1] raises `ValueError`; `bool`, `Decimal` (not registered as Real), strings, `complex` and other types raise `TypeError` (PB-009; previously some of these leaked an incidental `TypeError` or were silently accepted, and a 0d8b381 draft also rejected `Fraction`). NumPy is not a dependency, so NumPy scalars were not tested here. `-0.0` is treated as `0.0`. Values are not implicitly clipped. Both endpoints are exact: `encode_srgb(1.0)` returns `1.0` because the real equation gives `1.055 - 0.055 = 1`, while binary64 evaluation of the rounded constants gave `1 - 2**-53` (so `floor(x * 255)` was 254). Output is a floating-point component, not an 8-bit code. Quantization, alpha, color matrices, white-point adaptation and HDR are outside this slice.

The tests use literal vectors computed independently with Python Decimal at precision 60 from the cited equations, using the exact binary value of each float input (`Decimal(0.18)`, not `Decimal('0.18')`, because the code receives the float) and rounding the result once to binary64. Branch thresholds compare exact binary values of the input and the threshold constant, as the float code does. The Rec.709 tests use the same convention. `test_literals_match_independent_decimal` re-derives every literal on each run without calling the implementation. PB-009 corrected six PB-001 literals that were 1–4 ulp from the correctly rounded values (for example `decode(0.5)`: `0.21404114048223244`, not `0.21404114048223255`). Implementation outputs differ from the correctly rounded value by a few ulp: at most 5 for encode and 7 for decode over a 300 001-input sample (Python 3.14.7, macOS arm64). Vector and 1001-point grid assertions use exactly those bounds. Blind spot: an error within the bound passes, so a perturbation smaller than (bound minus a point's own error) is not caught; the literal re-derivation test guards the literals. Another libm may need the bounds re-measured. These bounds have zero headroom over the maxima measured on this platform's libm, so a different libm could exceed them; re-measure before loosening. Example derivation of `encode_srgb(0.18)`:

```python
from decimal import Decimal as D, localcontext
with localcontext() as context:
    context.prec = 60
    print(D('1.055') * D(0.18) ** (D(1) / D('2.4')) - D('0.055'))
# 0.461356129500441641900737092054743291983052624697977139620395
# float(...) == 0.46135612950044164
```

These are independently calculated expected values, not an independently measured IEC conformance dataset. Rounded piecewise constants have tiny knee discontinuities: do not replace explicit numeric tolerances with a claim of exact invertibility. With the stated constants the real-number encode curve drops by about `2.85e-8` (Decimal: `-2.8517309848e-8`) from `0.0031308` to the next input, so `encode_srgb` is monotonic except for that one step; the decode curve jumps up by about `2.33e-9` at `0.04045` and stays monotonic. The tests assert both steps directly because a `1e-4` grid never samples both sides of the knee. The IEC 61966-2-1 text itself was not obtained, so this is a property of the constants as stated by SRC-PB001-01/02.
