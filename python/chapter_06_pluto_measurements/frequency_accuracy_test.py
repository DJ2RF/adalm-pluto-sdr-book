"""
Kapitel 6 – Frequenzgenauigkeit & Drift

Misst die Abweichung eines bekannten Signals relativ zur LO.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(433_920_000)
sdr.rx_sample_rate = int(2_000_000)
sdr.rx_rf_bandwidth = int(500_000)
sdr.gain_control_mode = "manual"
sdr.rx_hardwaregain = 20

samples = np.asarray(sdr.rx())
samples -= np.mean(samples)

N = 4096
spec = np.fft.fftshift(np.fft.fft(samples[:N]))
mag = np.abs(spec)

freq = np.fft.fftshift(np.fft.fftfreq(N, d=1/sdr.rx_sample_rate))
peak_freq = freq[np.argmax(mag)]

plt.figure()
plt.plot(freq/1e3, 20*np.log10(np.maximum(mag, 1e-12)))
plt.axvline(peak_freq/1e3, color="r",
            label=f"Peak ≈ {peak_freq:.1f} Hz")
plt.title("Frequenzabweichung / Drift")
plt.xlabel("Frequenz [kHz] (relativ)")
plt.ylabel("Amplitude [dB]")
plt.legend()
plt.grid(True)
plt.show()
