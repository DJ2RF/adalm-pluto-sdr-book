"""
Kapitel 6 – Pluto als einfacher Spektrumanalysator

Ersetzt keinen Labor-Spektrumanalysator,
ist aber hervorragend für Vergleichs- und Relativmessungen.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(433_000_000)
sdr.rx_sample_rate = int(2_000_000)
sdr.rx_rf_bandwidth = int(2_000_000)
sdr.gain_control_mode = "manual"
sdr.rx_hardwaregain = 20

samples = np.asarray(sdr.rx())
samples -= np.mean(samples)

N = 4096
window = np.hanning(N)
spec = np.fft.fftshift(np.fft.fft(samples[:N] * window))
power_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

fs = float(sdr.rx_sample_rate)
freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))

plt.figure()
plt.plot(freq/1e3, power_db)
plt.title("Pluto als Spektrumanalysator")
plt.xlabel("Frequenz [kHz] (relativ zur LO)")
plt.ylabel("Amplitude [dB]")
plt.grid(True)
plt.show()
