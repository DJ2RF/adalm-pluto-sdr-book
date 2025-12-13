"""
Kapitel 5 – Zweiton-IMD Messung (IMD3)

Erzeugt zwei nahe Träger und zeigt IMD-Produkte
(f1, f2, 2f1-f2, 2f2-f1).
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1_000_000
N = 4096
t = np.arange(N) / fs

f1 = 100_000
f2 = 120_000

# Zweiton-Signal
signal = (
    0.8 * np.exp(1j * 2 * np.pi * f1 * t) +
    0.8 * np.exp(1j * 2 * np.pi * f2 * t)
)

spec = np.fft.fftshift(np.fft.fft(signal))
power_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

plt.figure()
plt.plot(freq/1e3, power_db)
plt.title("Zweiton-IMD (IMD3)")
plt.xlabel("Frequenz [kHz]")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.show()
