"""
Kapitel 4 – Decimation-Effekt

Zeigt, wie Decimation die effektive Samplerate reduziert.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(433_000_000)
sdr.rx_sample_rate = int(2_000_000)
sdr.rx_rf_bandwidth = int(500_000)

samples = np.asarray(sdr.rx())
samples -= np.mean(samples)

# Decimation Faktor
D = 4
samples_dec = samples[::D]

def spectrum(x, fs, label):
    N = 4096
    spec = np.fft.fftshift(np.fft.fft(x[:N]))
    mag = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))
    freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/fs))
    plt.plot(freq/1e3, mag, label=label)

plt.figure()
spectrum(samples, sdr.rx_sample_rate, "Original")
spectrum(samples_dec, sdr.rx_sample_rate / D, "Decimated x4")

plt.title("Decimation – Vergleich")
plt.xlabel("Frequenz [kHz]")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
