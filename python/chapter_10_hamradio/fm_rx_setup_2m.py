"""
Kapitel 10.1 – FM Empfang (2m) – Pluto Setup + einfache FM-Demod

Buch:
sdr.rx_lo = 145500000
sdr.rx_sample_rate = 200000
sdr.rx_rf_bandwidth = 200000
fm = np.angle(samples[1:] * np.conj(samples[:-1]))

Leicht verbessert:
- DC-Entfernung
- Normalisierung für Plot
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def fm_demod(samples: np.ndarray) -> np.ndarray:
    dphi = np.angle(samples[1:] * np.conj(samples[:-1]))
    dphi = dphi - np.mean(dphi)
    dphi = dphi / (np.max(np.abs(dphi)) + 1e-12)
    return dphi


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(145_500_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)

    fm = fm_demod(samples)

    plt.figure()
    plt.plot(fm[:8000])
    plt.title("FM Demod (2m) – Zeitbereich (Ausschnitt)")
    plt.xlabel("Sample")
    plt.ylabel("norm. Demod-Wert")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
