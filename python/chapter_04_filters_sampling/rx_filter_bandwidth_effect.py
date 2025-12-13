"""
Kapitel 4 – Einfluss der RX-Filterbandbreite
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

bandwidths = [200_000, 500_000, 1_000_000]

plt.figure()

for bw in bandwidths:
    sdr = adi.Pluto()
    sdr.rx_lo = int(433_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(bw)

    samples = np.asarray(sdr.rx())
    samples -= np.mean(samples)

    N = 4096
    spec = np.fft.fftshift(np.fft.fft(samples[:N]))
    mag = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

    plt.plot(mag, label=f"BW = {bw/1e3:.0f} kHz")

plt.title("RX-Filterbandbreite – Einfluss auf das Spektrum")
plt.xlabel("FFT Bin")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
