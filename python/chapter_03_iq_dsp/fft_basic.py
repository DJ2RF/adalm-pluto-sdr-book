"""
Kapitel 3 – FFT-Grundlagen
"""

import numpy as np
import matplotlib.pyplot as plt

fs = 1_000_000
N = 4096
t = np.arange(N) / fs

# Testsignal
signal = np.exp(1j * 2 * np.pi * 100_000 * t)

fft_data = np.fft.fftshift(np.fft.fft(signal))
power = np.abs(fft_data)

freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

plt.figure()
plt.plot(freq/1e3, power)
plt.title("FFT eines komplexen Sinussignals")
plt.xlabel("Frequenz [kHz]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
