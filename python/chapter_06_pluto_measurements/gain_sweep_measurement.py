"""
Kapitel 6 – Gain Sweep

Zeigt, wie sich RX-Gain direkt auf den gemessenen Pegel auswirkt.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

gains = list(range(0, 71, 5))
levels = []

for gain in gains:
    sdr = adi.Pluto()
    sdr.rx_lo = int(433_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(500_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = gain

    samples = np.asarray(sdr.rx())
    samples -= np.mean(samples)

    spec = np.fft.fftshift(np.fft.fft(samples[:4096]))
    power_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

    levels.append(np.max(power_db))

plt.figure()
plt.plot(gains, levels, marker="o")
plt.title("RX Gain Sweep – Maximalpegel")
plt.xlabel("RX Gain [dB]")
plt.ylabel("Max. Amplitude [dB]")
plt.grid(True)
plt.show()
