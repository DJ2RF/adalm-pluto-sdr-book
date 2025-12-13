"""
Kapitel 6 – Relative Pegelmessung

Vergleicht zwei Messungen mit unterschiedlicher Gain-Einstellung.
Absolutwerte sind unwichtig – Relationen sind entscheidend.
"""

import adi
import numpy as np

def measure_level(gain):
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
    return np.max(power_db)

level_low = measure_level(10)
level_high = measure_level(30)

print(f"Gain 10 dB: {level_low:.1f} dB")
print(f"Gain 30 dB: {level_high:.1f} dB")
print(f"Delta: {level_high - level_low:.1f} dB")
