"""
Kapitel 5 – Noise Floor vs. RX-Bandbreite

Zeigt: kleinere Bandbreite → niedrigerer Noise Floor
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

bandwidths = [200_000, 500_000, 1_000_000, 2_000_000]
noise_levels = []

for bw in bandwidths:
    sdr = adi.Pluto()
    sdr.rx_lo = int(1_000_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(bw)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    samples -= np.mean(samples)

    N = 4096
    spec = np.fft.fftshift(np.fft.fft(samples[:N]))
    power_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

    noise_levels.append(np.mean(power_db))

plt.figure()
plt.plot([bw/1e3 for bw in bandwidths], noise_levels, marker="o")
plt.title("Noise Floor vs. RX-Bandbreite")
plt.xlabel("RX-Bandbreite [kHz]")
plt.ylabel("Noise Floor [dB]")
plt.grid(True)
plt.show()
