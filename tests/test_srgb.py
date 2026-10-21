"""Tests catch wrong branches/constants, hidden clipping and invalid propagation.

Literal vectors (PB-009 correction): each expected value is the correctly
rounded binary64 value of the cited equation evaluated with Decimal at
precision 60, using the exact binary value of the float input. They were
generated without calling the implementation, and
``test_literals_match_independent_decimal`` re-derives every literal the same
way so the provenance is checked on each run. PB-001's original literals for
decode(0.5), decode(128/255), decode(0.0404499), decode(0.0404501),
encode(0.001) and encode(0.00313081) were 1-4 ulp away from the correctly
rounded values; they were replaced, not loosened.

Tolerance: the float implementation may differ from the correctly rounded
value by a few units in the last place (ulp), mainly because the 2.4 and
1/2.4 exponents amplify the rounding of the power base. A 300 001-point
sample on Python 3.14/macOS arm64 measured at most 5 ulp (encode) and 7 ulp
(decode). Vector assertions allow ``VECTOR_ULPS = 16`` ulp of the expected
value, a margin for other libm ``pow`` implementations; zero is exact.
"""

import math
import unittest
from decimal import Decimal, localcontext

from experiments.srgb.reference import decode_srgb, encode_srgb

VECTOR_ULPS = 16

ENCODE_VECTORS = [(0.0, 0.0), (0.001, 0.012920000000000001),
                  (0.0031308, 0.040449936),
                  (0.18, 0.46135612950044164),
                  (0.5, 0.7353569830524495), (1.0, 1.0),
                  (0.00313079, 0.0404498068),
                  (0.00313081, 0.040450034513346)]

DECODE_VECTORS = [(0.0, 0.0), (0.01292, 0.001),
                  (0.04045, 0.0031308049535603713),
                  (0.5, 0.21404114048223244),
                  (128 / 255, 0.21586050011389915), (1.0, 1.0),
                  (0.0404499, 0.0031307972136222907),
                  (0.0404501, 0.0031308151551923446)]

KNEE = 0.0031308


def _decimal_encode(value):
    x = Decimal(value)
    if x <= Decimal('0.0031308'):
        return Decimal('12.92') * x
    return Decimal('1.055') * x ** (Decimal(1) / Decimal('2.4')) - Decimal('0.055')


def _decimal_decode(value):
    x = Decimal(value)
    if x <= Decimal('0.04045'):
        return x / Decimal('12.92')
    return ((x + Decimal('0.055')) / Decimal('1.055')) ** Decimal('2.4')


class SRGBReferenceTests(unittest.TestCase):
    def assertWithinUlps(self, actual, expected, ulps=VECTOR_ULPS):
        if expected == 0.0:
            self.assertEqual(actual, 0.0)
            return
        error = abs(actual - expected) / math.ulp(expected)
        self.assertLessEqual(error, ulps,
                             '%r is %.1f ulp from %r' % (actual, error, expected))

    def test_literals_match_independent_decimal(self):
        # Re-derives the literals without calling the implementation.
        with localcontext() as context:
            context.prec = 60
            for value, expected in ENCODE_VECTORS:
                with self.subTest(function='encode', value=value):
                    self.assertEqual(float(_decimal_encode(value)), expected)
            for value, expected in DECODE_VECTORS:
                with self.subTest(function='decode', value=value):
                    self.assertEqual(float(_decimal_decode(value)), expected)

    def test_encode_known_vectors(self):
        for value, expected in ENCODE_VECTORS:
            with self.subTest(value=value):
                self.assertWithinUlps(encode_srgb(value), expected)

    def test_decode_known_vectors(self):
        for value, expected in DECODE_VECTORS:
            with self.subTest(value=value):
                self.assertWithinUlps(decode_srgb(value), expected)

    def test_endpoints_are_exact(self):
        # encode(1.0) previously returned 1 - 2**-53, so floor(x * 255) was 254.
        for function in (encode_srgb, decode_srgb):
            with self.subTest(function=function.__name__):
                self.assertEqual(function(0.0), 0.0)
                self.assertEqual(function(1.0), 1.0)
                self.assertEqual(math.floor(function(1.0) * 255), 255)

    def test_negative_zero_returns_positive_zero(self):
        for function in (encode_srgb, decode_srgb):
            with self.subTest(function=function.__name__):
                result = function(-0.0)
                self.assertEqual(result, 0.0)
                self.assertEqual(math.copysign(1.0, result), 1.0)

    def test_int_endpoints_are_accepted(self):
        for function in (encode_srgb, decode_srgb):
            with self.subTest(function=function.__name__):
                self.assertEqual(function(0), 0.0)
                self.assertEqual(function(1), 1.0)

    def test_reject_out_of_domain_instead_of_clipping(self):
        for function in (encode_srgb, decode_srgb):
            for value in (-0.001, 1.001, math.nan, math.inf, -math.inf,
                          -1, 2, 10 ** 400):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_reject_non_numeric_types(self):
        for function in (encode_srgb, decode_srgb):
            for value in (True, False, Decimal('0.5'), Decimal('2'), '0.5',
                          None, [0.5], complex(0.5, 0)):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

    def test_encode_knee_step_is_bounded_and_documented(self):
        # With the stated rounded constants the real-number encode curve is
        # discontinuous at 0.0031308: the upper branch starts about 2.85e-8
        # below the lower branch's end (Decimal: -2.8517309848e-8). The
        # 1e-4 grid below never samples both sides, so test it directly.
        below = encode_srgb(KNEE)
        above = encode_srgb(math.nextafter(KNEE, 1.0))
        step = above - below
        self.assertLess(step, 0.0)
        self.assertAlmostEqual(step, -2.8517309848e-8, delta=1e-15)
        self.assertLess(abs(step), 3e-8)

    def test_decode_knee_step_is_upward(self):
        # The inverse curve jumps up by about 2.33e-9 at 0.04045, so it stays
        # monotonic; bound the size so a constant change is caught.
        step = decode_srgb(math.nextafter(0.04045, 1.0)) - decode_srgb(0.04045)
        self.assertGreater(step, 0.0)
        self.assertAlmostEqual(step, 2.3295073109e-9, delta=1e-15)

    def test_monotonic_except_documented_encode_knee(self):
        # Dense grid plus every float within 64 steps of each knee. The only
        # permitted decrease is the encode step from KNEE to its successor.
        near_encode_knee = [KNEE]
        near_decode_knee = [0.04045]
        for _ in range(64):
            near_encode_knee.append(math.nextafter(near_encode_knee[-1], 1.0))
            near_encode_knee.insert(0, math.nextafter(near_encode_knee[0], 0.0))
            near_decode_knee.append(math.nextafter(near_decode_knee[-1], 1.0))
            near_decode_knee.insert(0, math.nextafter(near_decode_knee[0], 0.0))
        grid = [i / 10000 for i in range(10001)]
        for function, extra in ((encode_srgb, near_encode_knee),
                                (decode_srgb, near_decode_knee)):
            inputs = sorted(set(grid + extra))
            outputs = [function(x) for x in inputs]
            decreases = [(a, b) for a, b, fa, fb in
                         zip(inputs, inputs[1:], outputs, outputs[1:]) if fb < fa]
            with self.subTest(function=function.__name__):
                if function is encode_srgb:
                    self.assertEqual(decreases, [(KNEE, math.nextafter(KNEE, 1.0))])
                else:
                    self.assertEqual(decreases, [])

    def test_round_trip_linear_grid(self):
        for i in range(10001):
            value = i / 10000
            self.assertAlmostEqual(decode_srgb(encode_srgb(value)), value, delta=1e-8)

    def test_round_trip_all_8bit_codes(self):
        for i in range(256):
            value = i / 255
            self.assertAlmostEqual(encode_srgb(decode_srgb(value)), value, delta=1e-7)


if __name__ == '__main__':
    unittest.main()
