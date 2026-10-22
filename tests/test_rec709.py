"""PB-002: catch knee/domain mistakes, curve substitution and fake inversion.

Expected values (PB-009 convention, shared with tests/test_srgb.py): each
literal is the correctly rounded binary64 value of the cited equation
evaluated with Decimal at precision 60 from the exact binary value of the
float input. Branch thresholds compare exact binary values of the input and
of the threshold constant, as the float code does (Decimal(0.018) is slightly
below 0.018, so float 0.018 takes the upper branch). No literal comes from an
implementation under test; ``test_literals_match_independent_decimal``
re-derives every literal on each run. Under this convention two PB-002
literals were 1 ulp off and were corrected: encode(0.001) is
0.0045000000000000005 (was 0.0045) and encode(0.0180001) is
0.08124839465431213 (was 0.08124839465431212). The others were already
correctly rounded.

Tolerance: vector assertions allow the largest error the implementation
showed against the same Decimal reference over a 300 001-input sample
(Python 3.14.7, macOS arm64): ENCODE_ULPS = 3, INVERT_ULPS = 5 (inverse
measured on the 299 919 reachable inputs). Errors up to the bound are accepted
by design, so a perturbation smaller than (bound - the vector's own error) is
not caught by the vector tests; the literal re-derivation test guards the
literals themselves. Another libm may need the bound re-measured.
These bounds have zero headroom over the maxima measured on this platform's
libm, so a different libm could exceed them; re-measure before loosening.
PB-002 left sRGB unchanged; PB-009 later added input-type and negative-zero checks.
"""

import math
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction

from experiments.rec709.reference import encode_bt709_oetf, invert_bt709_oetf
from experiments.srgb.reference import encode_srgb

ENCODE_ULPS = 3
INVERT_ULPS = 5

OETF_VECTORS = [(0.0, 0.0), (0.001, 0.0045000000000000005), (0.01, 0.045),
                (0.018, 0.08124794403514048),
                (0.18, 0.40900772886415043),
                (0.5, 0.7055150899221212), (1.0, 1.0),
                (0.0179999, 0.08099955),
                (0.0180001, 0.08124839465431213)]

INVERSE_VECTORS = [(0.0, 0.0), (0.0045, 0.001), (0.045, 0.01),
                   (0.0809999, 0.017999977777777777),
                   (0.081248, 0.01800001241953032),
                   (0.5, 0.25958940050628576), (1.0, 1.0)]


def _decimal_oetf(value):
    x = Decimal(value)
    if x < Decimal(0.018):
        return Decimal('4.5') * x
    return Decimal('1.099') * x ** Decimal('0.45') - Decimal('0.099')


def _decimal_inverse(value):
    x = Decimal(value)
    if x < Decimal(0.081):
        return x / Decimal('4.5')
    return ((x + Decimal('0.099')) / Decimal('1.099')) ** (Decimal(1) / Decimal('0.45'))


class BT709ReferenceTests(unittest.TestCase):
    def assertWithinUlps(self, actual, expected, ulps):
        if expected == 0.0:
            self.assertEqual(actual, 0.0)
            return
        error = abs(actual - expected) / math.ulp(expected)
        self.assertLessEqual(error, ulps,
                             '%r is %.1f ulp from %r' % (actual, error, expected))

    def test_literals_match_independent_decimal(self):
        with localcontext() as context:
            context.prec = 60
            for value, expected in OETF_VECTORS:
                with self.subTest(function='oetf', value=value):
                    self.assertEqual(float(_decimal_oetf(value)), expected)
            for value, expected in INVERSE_VECTORS:
                with self.subTest(function='inverse', value=value):
                    self.assertEqual(float(_decimal_inverse(value)), expected)

    def test_oetf_literal_vectors(self):
        for value, expected in OETF_VECTORS:
            with self.subTest(value=value):
                self.assertWithinUlps(encode_bt709_oetf(value), expected, ENCODE_ULPS)

    def test_oetf_uses_upper_branch_at_knee(self):
        self.assertLess(encode_bt709_oetf(0.0179999), 0.081)
        self.assertGreater(encode_bt709_oetf(0.018), 0.0812)
        self.assertGreater(encode_bt709_oetf(0.0180001), encode_bt709_oetf(0.018))

    def test_partial_inverse_literal_vectors(self):
        for value, expected in INVERSE_VECTORS:
            with self.subTest(value=value):
                self.assertWithinUlps(invert_bt709_oetf(value), expected, INVERT_ULPS)

    def test_implementation_within_measured_ulps_on_grid(self):
        with localcontext() as context:
            context.prec = 60
            for i in range(1001):
                value = i / 1000
                with self.subTest(function='oetf', value=value):
                    self.assertWithinUlps(encode_bt709_oetf(value),
                                          float(_decimal_oetf(value)), ENCODE_ULPS)
                try:
                    actual = invert_bt709_oetf(value)
                except ValueError:
                    continue  # knee gap, covered by the rejection tests
                with self.subTest(function='inverse', value=value):
                    self.assertWithinUlps(actual, float(_decimal_inverse(value)),
                                          INVERT_ULPS)

    def test_partial_inverse_rejects_unreachable_gap(self):
        for value in (0.081, 0.0811, 0.0812479):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    invert_bt709_oetf(value)

    def test_quantized_signal_requires_a_decoder_policy(self):
        # Legal 10-bit code 135 normalizes inside the rounded equation's gap.
        # This rejection is why this function cannot be a general decoder.
        with self.assertRaises(ValueError):
            invert_bt709_oetf((135 - 64) / 876)

    def test_rejects_nonfinite_and_out_of_range_numbers(self):
        for function in (encode_bt709_oetf, invert_bt709_oetf):
            for value in (-0.001, 1.001, math.nan, math.inf, -math.inf):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_rejects_non_numeric_types(self):
        # PB-009: bool, Decimal and other non-int/float types raise TypeError.
        for function in (encode_bt709_oetf, invert_bt709_oetf):
            for value in (True, False, Decimal('0.5'), Decimal('2'), '0.5',
                          None, [0.5], complex(0.5, 0)):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(TypeError):
                        function(value)

    def test_accepts_other_real_numbers_via_float(self):
        class Shifted(float):
            def __float__(self):
                return 0.5

        for function in (encode_bt709_oetf, invert_bt709_oetf):
            with self.subTest(function=function.__name__):
                self.assertEqual(function(Fraction(1, 2)), function(0.5))
                self.assertEqual(function(Fraction(1, 3)), function(1 / 3))
                # A float subclass is evaluated at its __float__ value.
                self.assertEqual(function(Shifted(0.25)), function(0.5))

    def test_rejects_out_of_range_ints(self):
        for function in (encode_bt709_oetf, invert_bt709_oetf):
            for value in (-1, 2, 10 ** 400, Fraction(3, 2), Fraction(10 ** 400, 3)):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_negative_zero_and_int_endpoints(self):
        for function in (encode_bt709_oetf, invert_bt709_oetf):
            with self.subTest(function=function.__name__):
                result = function(-0.0)
                self.assertEqual(result, 0.0)
                self.assertEqual(math.copysign(1.0, result), 1.0)
                self.assertEqual(function(0), 0.0)
                self.assertEqual(function(1), 1.0)
                self.assertEqual(function(1.0), 1.0)

    def test_round_trip_on_reachable_outputs(self):
        for value in [i / 10000 for i in range(10001)] + [0.018, 0.0179999, 0.0180001]:
            self.assertAlmostEqual(invert_bt709_oetf(encode_bt709_oetf(value)), value, delta=1e-14)

    def test_inverse_preserves_upper_branch_at_the_signal_knee(self):
        # Floating inverse can undershoot .018 by one ulp, causing re-encoding
        # to cross the forward discontinuity. Preserve the selected domain.
        signals = [encode_bt709_oetf(0.018),
                   encode_bt709_oetf(math.nextafter(0.018, 1.0)),
                   0.081248, 0.5, 1.0]
        for signal in signals:
            with self.subTest(signal=signal):
                linear = invert_bt709_oetf(signal)
                self.assertGreaterEqual(linear, 0.018)
                self.assertAlmostEqual(encode_bt709_oetf(linear), signal, delta=1e-14)

    def test_inverse_preserves_lower_branch_below_the_signal_gap(self):
        signal = math.nextafter(0.081, 0.0)
        linear = invert_bt709_oetf(signal)
        self.assertLess(linear, 0.018)
        self.assertAlmostEqual(encode_bt709_oetf(linear), signal, delta=1e-14)

    def test_oetf_monotonic_grid_and_jump(self):
        values = [encode_bt709_oetf(i / 10000) for i in range(10001)]
        self.assertTrue(all(a <= b for a, b in zip(values, values[1:])))
        # A lower-branch-at-knee implementation loses the documented jump.
        self.assertGreater(encode_bt709_oetf(0.018), 0.0812)

    def test_equal_numeric_inputs_are_not_equal_encodings(self):
        for value, expected_srgb, expected_bt in [
                (0.01, 0.09985282273412834, 0.045),
                (0.18, 0.46135612950044164, 0.40900772886415043),
                (0.5, 0.7353569830524495, 0.7055150899221212)]:
            with self.subTest(value=value):
                self.assertAlmostEqual(encode_srgb(value), expected_srgb, delta=1e-14)
                self.assertAlmostEqual(encode_bt709_oetf(value), expected_bt, delta=1e-14)
                self.assertGreater(encode_srgb(value), encode_bt709_oetf(value))


if __name__ == '__main__':
    unittest.main()
