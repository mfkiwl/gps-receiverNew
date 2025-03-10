"""This module contains commonly used values whose definitions shouldn't change,
either because they're defined in the GPS spec (e.g. ``BITS_PER_SUBFRAME``) or
because they're derived from other values (e.g. ``SAMPLES_PER_SECOND``)."""

import numpy as np

from .config import SAMPLES_PER_MILLISECOND

# Sampling

L1_FREQUENCY = 1575.42e6

SAMPLES_PER_SECOND = SAMPLES_PER_MILLISECOND * 1000

# The time of each sample within a 1 ms sampling period (in seconds).
SAMPLE_TIMES = np.arange(SAMPLES_PER_MILLISECOND) / SAMPLES_PER_SECOND

SECONDS_PER_SAMPLE = 1 / SAMPLES_PER_SECOND

# Navigation data demodulation

# The number of bits contained within a subframe of the navigation message.
# Defined in section 20.3.2 of IS-GPS-200.
BITS_PER_SUBFRAME = 300
