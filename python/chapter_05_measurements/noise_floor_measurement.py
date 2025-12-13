"""
Kapitel 5 – Noise Floor messen

Einfaches Verfahren:
- Antenne ab / Abschlusswiderstand
- FFT im dB-Maßstab
- Mittelwert als Noise Floor
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(1_000_000_000)
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

noise_floor = np.mean(power_db)

plt.figure()
plt.plot(power_db)
plt.axhline(noise_floor, color="r", linestyle="--",
            label=f"Noise Floor ≈ {noise_floor:.1f} dB")
plt.title("Noise Floor Messung")
plt.xlabel("FFT Bin")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
