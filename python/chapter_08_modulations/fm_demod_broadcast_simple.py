"""
Kapitel 8.2 FM – einfache FM-Demodulation (Differentialwinkel)

fm = angle( x[n] * conj(x[n-1]) )

Leicht verbessert:
- DC-Entfernung (IQ-Mittelwert)
- Normalisierung der Demod-Ausgabe
- optionaler Plot
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def fm_demod(samples: np.ndarray) -> np.ndarray:
    # Differential-Phasenwinkel (FM)
    dphi = np.angle(samples[1:] * np.conj(samples[:-1]))
    # Grobe Normalisierung für Anzeige
    dphi = dphi - np.mean(dphi)
    dphi = dphi / (np.max(np.abs(dphi)) + 1e-12)
    return dphi


def main():
    sdr = adi.Pluto()

    # UKW-FM Beispiel-Setup
    sdr.rx_lo = int(100_000_000)       # 100 MHz
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)  # DC entfernen (leicht verbessert)

    fm = fm_demod(samples)

    plt.figure()
    plt.plot(fm[:5000])
    plt.title("FM Demod (Differentialwinkel) – Zeitbereich (Ausschnitt)")
    plt.xlabel("Sample")
    plt.ylabel("norm. Demod-Wert")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
