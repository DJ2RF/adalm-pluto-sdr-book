import numpy as np
from .dsp_utils import windowed_fft, db20


def noise_floor_db(spec_db: np.ndarray) -> float:
    """Mean noise floor estimate."""
    return float(np.mean(spec_db))


def snr_estimate_db(spec_db: np.ndarray) -> float:
    """SNR ≈ peak - noise floor."""
    return float(np.max(spec_db) - np.mean(spec_db))


def peak_freq_hz(samples: np.ndarray, fs_hz: float, n: int = 4096) -> float:
    """Peak frequency (relative to LO)."""
    X = windowed_fft(samples, n=n, window="hann")
    mag = np.abs(X)
    freq = np.fft.fftshift(np.fft.fftfreq(n, d=1.0 / fs_hz))
    return float(freq[np.argmax(mag)])


def imd3_estimate_bins(spec_db: np.ndarray, f1_bin: int, f2_bin: int):
    """Estimate IMD3 levels in FFT-bin domain."""
    imd_low = 2 * f1_bin - f2_bin
    imd_high = 2 * f2_bin - f1_bin
    return spec_db[imd_low], spec_db[imd_high]
