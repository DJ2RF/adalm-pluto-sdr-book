import numpy as np


def fm_demod_phase(samples: np.ndarray) -> np.ndarray:
    """FM demod via differential phase."""
    dphi = np.angle(samples[1:] * np.conj(samples[:-1]))
    return dphi - np.mean(dphi)


def inst_freq_from_phase(samples: np.ndarray) -> np.ndarray:
    """Instantaneous frequency proxy (rad/sample)."""
    phase = np.unwrap(np.angle(samples))
    return np.diff(phase)


def am_envelope(samples: np.ndarray) -> np.ndarray:
    """AM envelope detector."""
    env = np.abs(samples)
    return env - np.mean(env)
