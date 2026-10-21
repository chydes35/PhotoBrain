"""Tests catch wrong branches/constants, hidden clipping and invalid propagation.

Literal vectors were calculated independently with Decimal at precision 60
from the cited equations, then rounded to binary64-comparable decimals.
No expected value calls the implementation under test.
"""

import math
import unittest

from experiments.srgb.reference import decode_srgb, encode_srgb


class SRGBReferenceTests(unittest.TestCase):
    def test_encode_known_vectors(self):
        for value, expected in [(0.0, 0.0), (0.001, 0.01292),
                                (0.0031308, 0.040449936),
                                (0.18, 0.46135612950044165),
                                (0.5, 0.7353569830524495), (1.0, 1.0)]:
            with self.subTest(value=value):
                self.assertAlmostEqual(encode_srgb(value), expected, delta=1e-14)

    def test_decode_known_vectors(self):
        for value, expected in [(0.0, 0.0), (0.01292, 0.001),
                                (0.04045, 0.0031308049535603713),
                                (0.5, 0.21404114048223255),
                                (128 / 255, 0.21586050011389923), (1.0, 1.0)]:
            with self.subTest(value=value):
                self.assertAlmostEqual(decode_srgb(value), expected, delta=1e-14)

    def test_encode_breakpoint_neighbors(self):
        # Values straddling the rounded breakpoint expose wrong branch choice.
        self.assertAlmostEqual(encode_srgb(0.00313079), 0.0404498068, delta=1e-14)
        self.assertAlmostEqual(encode_srgb(0.00313081), 0.04045003451334598, delta=1e-14)

    def test_decode_breakpoint_neighbors(self):
        self.assertAlmostEqual(decode_srgb(0.0404499), 0.003130797213622291, delta=1e-14)
        self.assertAlmostEqual(decode_srgb(0.0404501), 0.003130815155192346, delta=1e-14)

    def test_reject_out_of_domain_instead_of_clipping(self):
        for function in (encode_srgb, decode_srgb):
            for value in (-0.001, 1.001, math.nan, math.inf, -math.inf):
                with self.subTest(function=function.__name__, value=value):
                    with self.assertRaises(ValueError):
                        function(value)

    def test_round_trip_linear_grid(self):
        for i in range(10001):
            value = i / 10000
            self.assertAlmostEqual(decode_srgb(encode_srgb(value)), value, delta=1e-8)

    def test_round_trip_all_8bit_codes(self):
        for i in range(256):
            value = i / 255
            self.assertAlmostEqual(encode_srgb(decode_srgb(value)), value, delta=1e-7)

    def test_monotonic_grid(self):
        # Rounded constants have a tiny encode discontinuity at the knee;
        # this is a grid check, not a claim of strict global monotonicity.
        for function in (encode_srgb, decode_srgb):
            values = [function(i / 10000) for i in range(10001)]
            self.assertTrue(all(a <= b for a, b in zip(values, values[1:])))


if __name__ == '__main__':
    unittest.main()
