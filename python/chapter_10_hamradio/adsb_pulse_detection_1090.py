"""
Kapitel 10.3 – ADS-B (1090 MHz) – Pulsdetektion (Rohdaten-Analyse)

Buch:
power = np.abs(samples)
threshold = mean(power) + 4*std(power)
pulses = power > threshold

Leicht verbessert:
- robustere Schwelle (k=4 default)
- kleine Statistik-Ausgabe
"""

import adi
import numpy as np

def main(k: float = 4.0):
    sdr = adi.Pluto()
    sdr.rx_lo = int(1_090_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())

    power = np.abs(samples)
    thr = np.mean(power) + k * np.std(power)
    pulses = power > thr

    print("ADS-B pulse detection")
    print("samples:", len(samples))
    print("threshold:", thr)
    print("pulse ratio:", np.mean(pulses))

    # Optional speichern, um offline weiter zu machen:
    np.save("adsb_iq.npy", samples)
    np.save("adsb_pulses.npy", pulses.astype(np.uint8))

if __name__ == "__main__":
    main()
