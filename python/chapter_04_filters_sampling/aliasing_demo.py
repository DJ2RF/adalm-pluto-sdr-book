"""
Kapitel 4 – Aliasing-Demonstration

Zeigt, wie Frequenzen oberhalb der Nyquist-Grenze gespiegelt erscheinen.
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1_000_000
N = 4096
t = np.arange(N) / fs

# Signal oberhalb Nyquist
signal = np.exp(1j * 2 * np.pi * 700_000 * t)

fft_data = np.fft.fftshift(np.fft.fft(signal))
mag = 20 * np.log10(np.maximum(np.abs(fft_data), 1e-12))
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

plt.figure()
plt.plot(freq/1e3, mag)
plt.title("Aliasing bei Überschreitung der Nyquist-Frequenz")
plt.xlabel("Frequenz [kHz]")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.show()
