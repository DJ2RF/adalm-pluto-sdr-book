"""
Kapitel 10.1 – SSB-Empfang über FFT-Shift + Bandpass (Prinzipdemo)

Buch: baseband = samples * exp(-j*2*pi*freq_shift*t)

Dieses Skript zeigt nur den Frequency-Shift im Basisband.
Bandpass/Audio-Pipeline wird typischerweise in GNU Radio gemacht.
"""

import numpy as np

def shift_frequency(samples: np.ndarray, fs: float, freq_shift_hz: float) -> np.ndarray:
    n = np.arange(len(samples))
    t = n / fs
    return samples * np.exp(-1j * 2 * np.pi * freq_shift_hz * t)

# Beispiel-Aufruf (samples müssen vorhanden sein):
# shifted = shift_frequency(samples, fs=200000, freq_shift_hz=1500)
