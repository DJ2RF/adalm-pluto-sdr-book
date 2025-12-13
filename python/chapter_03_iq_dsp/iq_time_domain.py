"""
Kapitel 3 – I/Q-Signale im Zeitbereich
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

sdr = adi.Pluto()
sdr.rx_lo = int(1_000_000_000)
sdr.rx_sample_rate = int(1_000_000)
sdr.rx_rf_bandwidth = int(1_000_000)

samples = np.asarray(sdr.rx())
samples = samples - np.mean(samples)

N = 2000
plt.figure()
plt.plot(np.real(samples[:N]), label="I")
plt.plot(np.imag(samples[:N]), label="Q")
plt.title("I/Q-Signal im Zeitbereich")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()
