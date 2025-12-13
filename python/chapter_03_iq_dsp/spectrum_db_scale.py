"""
Kapitel 3 – Lineare vs. logarithmische Spektrumsdarstellung
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1_000_000
N = 4096
t = np.arange(N) / fs

signal = (
    np.exp(1j * 2 * np.pi * 100_000 * t)
    + 0.2 * np.exp(1j * 2 * np.pi * 150_000 * t)
)

fft_data = np.fft.fftshift(np.fft.fft(signal))

power_lin = np.abs(fft_data)
power_db = 20 * np.log10(np.maximum(power_lin, 1e-12))

plt.figure()
plt.plot(power_db)
plt.title("Spektrum in dB")
plt.xlabel("FFT Bin")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.show()
