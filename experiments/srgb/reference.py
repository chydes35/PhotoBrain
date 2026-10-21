"""PB-001 scalar oracle; finite normalized components only, no app dependency.

Equations: SRC-PB001-01 (ICC sRGB registry), SRC-PB001-02 (W3C CSS
Color 4, 2026-10-20, section 10.2). Independently written, not copied code.
"""

import math


def _check_component(value: float) -> None:
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError('component must be finite and in [0, 1]')


def encode_srgb(value: float) -> float:
    """Convert one normalized linear-light sRGB component to encoded sRGB."""
    _check_component(value)
    if value <= 0.0031308:
        return 12.92 * value
    return 1.055 * value ** (1.0 / 2.4) - 0.055


def decode_srgb(value: float) -> float:
    """Convert one normalized encoded sRGB component to linear-light sRGB."""
    _check_component(value)
    if value <= 0.04045:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4
