"""PB-001 scalar oracle; finite normalized components only, no app dependency.

Equations: SRC-PB001-01 (ICC sRGB registry), SRC-PB001-02 (W3C CSS
Color 4, 2026-10-20, section 10.2). Independently written, not copied code.

Input contract (PB-009): a component must be a ``numbers.Real`` other than
``bool`` (``int``, ``float``, ``fractions.Fraction``, and types registered as
Real; NumPy registers its floating scalars, not tested here). It is converted once with ``float()``,
so the result is computed from that binary64 value; a float subclass or other
Real type is evaluated at its ``__float__`` value. ``bool``, ``Decimal`` (not
registered as Real), ``str``, ``complex`` and other types raise ``TypeError``.
A value that is not finite after conversion, overflows float, or lies outside
[0, 1] raises ``ValueError``. ``-0.0`` is treated as ``0.0``, so no function
returns negative zero. Values are never clipped.
"""

import math
import numbers


def _check_component(value) -> float:
    """Return ``value`` as a nonnegative-zero float, or raise."""
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise TypeError('component must be a real number, not '
                        + type(value).__name__)
    try:
        value = float(value)
    except OverflowError:
        raise ValueError('component must be finite and in [0, 1]') from None
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError('component must be finite and in [0, 1]')
    return value + 0.0  # maps -0.0 to 0.0; other values unchanged


def encode_srgb(value: float) -> float:
    """Convert one normalized linear-light sRGB component to encoded sRGB.

    The upper branch evaluates to 1 - 2**-53 at 1.0 in binary64 because
    1.055 and 0.055 are not exactly representable. The real-number equation
    gives exactly 1.055 - 0.055 = 1, so the endpoint returns 1.0.
    """
    value = _check_component(value)
    if value <= 0.0031308:
        return 12.92 * value
    if value == 1.0:
        return 1.0
    return 1.055 * value ** (1.0 / 2.4) - 0.055


def decode_srgb(value: float) -> float:
    """Convert one normalized encoded sRGB component to linear-light sRGB."""
    value = _check_component(value)
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4
