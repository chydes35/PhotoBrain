# PB-001 normalized sRGB reference

This independent scalar Python oracle supports [MPKB-02-005](../../chapters/02-light-color-science/MPKB-02-005.md). It is a research reference, not Editor production code.

Run `python3 -m unittest discover -s tests -v` from the PhotoBrain root. No packages, photo files, network or app frameworks are required.

Each function accepts a finite numeric scalar in [0,1]. Invalid numeric values raise `ValueError`; nonnumeric objects are outside the interface. Values are not implicitly clipped. Output is a floating-point component, not an 8-bit code. Quantization, alpha, color matrices, white-point adaptation and HDR are outside this slice.

The tests use literal vectors computed independently with Python Decimal at precision 60 from the cited equations. Example derivation of `encode_srgb(0.18)`:

```python
from decimal import Decimal as D, localcontext
with localcontext() as context:
    context.prec = 60
    print(D('1.055') * D('0.18') ** (D(1) / D('2.4')) - D('0.055'))
# 0.461356129500441649862826868134178786136892138210028214953781
```

These are independently calculated expected values, not an independently measured IEC conformance dataset. Rounded piecewise constants have tiny knee discontinuities: do not replace explicit numeric tolerances with a claim of exact invertibility.
