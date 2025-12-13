"""
Kapitel 8.4.2 FSK – FSK sichtbar machen über Instantanfrequenz/Phasendifferenz

Buchidee:
- entweder f = angle(x[n] * conj(x[n-1])) plotten
- oder inst_phase unwrap + diff -> inst_freq

Leicht verbessert:
- unwrap+diff für stabileres Ergebnis
- optionales Glätten (moving average)
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def moving_average(x: np.ndarray, n: int = 8) -> np.ndarray:
    if n <= 1:
        return x
    kernel = np.ones(n) / n
    return np.convolve(x, kernel, mode="same")


def main():
    sdr = adi.Pluto()

    # Beispielwerte: ISM/FSK-lastige Bereiche (anpassen!)
    sdr.rx_lo = int(433_920_000)
    sdr.rx_rf_bandwidth = int(250_000)
    sdr.rx_sample_rate = int(250_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)

    inst_phase = np.unwrap(np.angle(samples))
    inst_freq = np.diff(inst_phase)          # ~ Instantanfrequenz (relativ)
    inst_freq = moving_average(inst_freq, 8)

    plt.figure()
    plt.plot(inst_freq[:8000])
    plt.title("FSK / Instantanfrequenz (relativ) – Zeitbereich (Ausschnitt)")
    plt.xlabel("Sample")
    plt.ylabel("ΔPhase [rad] (geglättet)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
