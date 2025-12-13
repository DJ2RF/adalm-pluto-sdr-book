"""
Kapitel 8 – Konstellationsdiagramm (I/Q Scatter)

Leicht verbessert:
- nur Ausschnitt plotten (Performance)
- Achsen gleich skalieren
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def main():
    sdr = adi.Pluto()
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.rx_lo = int(433_000_000)

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)

    N = min(len(samples), 20000)
    x = samples[:N]

    plt.figure()
    plt.scatter(np.real(x), np.imag(x), s=2)
    plt.title("I/Q Konstellation (Ausschnitt)")
    plt.xlabel("I")
    plt.ylabel("Q")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
