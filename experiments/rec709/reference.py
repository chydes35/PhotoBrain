"""PB-002 research oracle; not a general video decoder or display EOTF.

OETF: ITU-R BT.709-6 (06/2015), section 1, item 1.2. Inversion on the
reachable range and rejection of the rounded-knee gap are PhotoBrain policy.
"""

import math


_UPPER_KNEE_SIGNAL = 1.099 * 0.018 ** 0.45 - 0.099


def _check_normalized(value: float) -> None:
    if not math.isfinite(value) or not 0.0 <= value <= 1.0:
        raise ValueError('reference input must be finite and in [0, 1]')


def encode_bt709_oetf(value: float) -> float:
    """Encode a normalized linear source value with the rounded BT.709 OETF."""
    _check_normalized(value)
    if value < 0.018:
        return 4.5 * value
    return 1.099 * value ** 0.45 - 0.099


def invert_bt709_oetf(value: float) -> float:
    """Invert reachable OETF values; reject the gap, not interpolate it.

    Quantization may put otherwise valid video signals inside this gap, so
    this deliberately partial mathematical reference is not a decoder.
    """
    _check_normalized(value)
    if value < 0.081:
        # Division may round the final lower-branch value up to .018.
        return min(value / 4.5, math.nextafter(0.018, 0.0))
    if value < _UPPER_KNEE_SIGNAL:
        raise ValueError('signal is in the rounded BT.709 OETF knee gap')
    # Inverse power may round the first upper-branch value below .018.
    return max(0.018, ((value + 0.099) / 1.099) ** (1.0 / 0.45))
