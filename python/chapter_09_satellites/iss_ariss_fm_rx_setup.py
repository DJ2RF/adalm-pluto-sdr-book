"""
Kapitel 9.6 – ISS ARISS Voice (145.800 MHz) – einfacher FM-Empfang (Frontend)

Hinweis:
Dieses Skript ist nur das IQ-Frontend. Für Audio:
- FM Demod (z.B. GNU Radio oder Python-Demod aus Kap. 8 / Anhang A)
- Ausgabe an Sounddevice / WAV
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(145_800_000)
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("iss_ariss_iq.npy", samples)
    print("Saved -> iss_ariss_iq.npy", samples.shape)


if __name__ == "__main__":
    main()
