from __future__ import annotations
import numpy as np


def dc_remove(x: np.ndarray) -> np.ndarray:
    """Remove DC offset."""
    return x - np.mean(x)


def normalize(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """Normalize signal magnitude."""
    return x / (np.max(np.abs(x)) + eps)


def db20(x: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    """20*log10(|x|) with protection."""
    return 20.0 * np.log10(np.maximum(np.abs(x), eps))


def windowed_fft(x: np.ndarray, n: int, window: str = "hann") -> np.ndarray:
    """FFT with window and fftshift."""
    x = x[:n]

    if window == "hann":
        w = np.hanning(n)
    elif window == "hamming":
        w = np.hamming(n)
    elif window == "rect":
        w = np.ones(n)
    else:
        raise ValueError("window must be hann|hamming|rect")

    return np.fft.fftshift(np.fft.fft(x * w))


def fft_freq_axis(n: int, fs_hz: float) -> np.ndarray:
    """Frequency axis for fftshifted FFT."""
    return np.fft.fftshift(np.fft.fftfreq(n, d=1.0 / fs_hz))


def spectrum_db(x: np.ndarray, n: int, fs_hz: float, window: str = "hann"):
    """Return (freq_axis_hz, spectrum_db)."""
    X = windowed_fft(x, n=n, window=window)
    f = fft_freq_axis(n, fs_hz)
    return f, db20(X)
