"""
Kapitel 5 – SNR Abschätzung

Vereinfachte Methode:
- Signalpeak - mittlerer Noise Floor
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(433_000_000)
sdr.rx_sample_rate = int(2_000_000)
sdr.rx_rf_bandwidth = int(500_000)
sdr.gain_control_mode = "manual"
sdr.rx_hardwaregain = 20

samples = np.asarray(sdr.rx())
samples -= np.mean(samples)

N = 4096
spec = np.fft.fftshift(np.fft.fft(samples[:N]))
power_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

signal_peak = np.max(power_db)
noise_floor = np.mean(power_db)

snr = signal_peak - noise_floor

plt.figure()
plt.plot(power_db)
plt.axhline(noise_floor, color="r", linestyle="--", label="Noise Floor")
plt.axhline(signal_peak, color="g", linestyle="--", label="Signal Peak")
plt.title(f"SNR ≈ {snr:.1f} dB")
plt.xlabel("FFT Bin")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
