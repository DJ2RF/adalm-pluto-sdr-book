"""
Kapitel 4 – Abtastrate vs. Bandbreite

Zeigt, dass die Samplerate die darstellbare Frequenzspanne bestimmt,
während die Filterbandbreite das nutzbare Signal begrenzt.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()

sdr.rx_lo = int(433_000_000)
sdr.rx_sample_rate = int(2_000_000)     # 2 MS/s
sdr.rx_rf_bandwidth = int(500_000)      # 500 kHz Filter

samples = np.asarray(sdr.rx())
samples -= np.mean(samples)

N = 4096
spec = np.fft.fftshift(np.fft.fft(samples[:N]))
mag = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

fs = float(sdr.rx_sample_rate)
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

plt.figure()
plt.plot(freq/1e3, mag)
plt.title("Abtastrate vs. Filterbandbreite")
plt.xlabel("Frequenz [kHz]")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.show()
