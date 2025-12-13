"""
Kapitel 3 – Fensterfunktionen vergleichen
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1_000_000
N = 4096
t = np.arange(N) / fs

signal = np.exp(1j * 2 * np.pi * 123_456 * t)

windows = {
    "Rectangular": np.ones(N),
    "Hann": np.hanning(N),
    "Hamming": np.hamming(N)
}

plt.figure()

for name, w in windows.items():
    fft_data = np.fft.fftshift(np.fft.fft(signal * w))
    power = 20 * np.log10(np.maximum(np.abs(fft_data), 1e-12))
    plt.plot(power, label=name)

plt.title("Fenstervergleich (Spektrum)")
plt.xlabel("FFT Bin")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
