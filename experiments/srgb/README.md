# PB-001 normalized sRGB reference

This independent scalar Python oracle supports [MPKB-02-005](../../chapters/02-light-color-science/MPKB-02-005.md). It is a research reference, not Editor production code.

Run `python3 -m unittest discover -s tests -v` from the PhotoBrain root. No packages, photo files, network or app frameworks are required.

Each function accepts a finite Python `int` or `float` in [0,1]. Non-finite or out-of-range numbers raise `ValueError`; `bool`, `Decimal`, strings and other types raise `TypeError` (PB-009; previously some of these leaked an incidental `TypeError` or were silently accepted). `-0.0` is treated as `0.0`. Values are not implicitly clipped. Both endpoints are exact: `encode_srgb(1.0)` returns `1.0` because the real equation gives `1.055 - 0.055 = 1`, while binary64 evaluation of the rounded constants gave `1 - 2**-53` (so `floor(x * 255)` was 254). Output is a floating-point component, not an 8-bit code. Quantization, alpha, color matrices, white-point adaptation and HDR are outside this slice.

The tests use literal vectors computed independently with Python Decimal at precision 60 from the cited equations, using the exact binary value of each float input and rounding the result once to binary64. `test_literals_match_independent_decimal` re-derives every literal on each run without calling the implementation. PB-009 corrected six PB-001 literals that were 1–4 ulp from the correctly rounded values (for example `decode(0.5)`: `0.21404114048223244`, not `0.21404114048223255`). Implementation outputs may differ from the correctly rounded value by a few ulp (measured at most 5 for encode and 7 for decode on a 300 001-point sample); vector assertions allow 16 ulp. Example derivation of `encode_srgb(0.18)`:

```python
from decimal import Decimal as D, localcontext
with localcontext() as context:
    context.prec = 60
    print(D('1.055') * D('0.18') ** (D(1) / D('2.4')) - D('0.055'))
# 0.461356129500441649862826868134178786136892138210028214953781
```

These are independently calculated expected values, not an independently measured IEC conformance dataset. Rounded piecewise constants have tiny knee discontinuities: do not replace explicit numeric tolerances with a claim of exact invertibility. With the stated constants the real-number encode curve drops by about `2.85e-8` (Decimal: `-2.8517309848e-8`) from `0.0031308` to the next input, so `encode_srgb` is monotonic except for that one step; the decode curve jumps up by about `2.33e-9` at `0.04045` and stays monotonic. The tests assert both steps directly because a `1e-4` grid never samples both sides of the knee. The IEC 61966-2-1 text itself was not obtained, so this is a property of the constants as stated by SRC-PB001-01/02.
