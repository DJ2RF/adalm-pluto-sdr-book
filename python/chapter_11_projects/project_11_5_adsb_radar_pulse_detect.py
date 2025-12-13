"""
11.5 ADS-B Radarprojekt – Pulsdetektion (k=5)

Buch:
power = abs(samples)
thr = mean(power) + 5*std(power)
pulses = power > thr
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(1_090_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    power = np.abs(samples)

    thr = np.mean(power) + 5.0 * np.std(power)
    pulses = power > thr

    np.save("adsb_iq.npy", samples)
    np.save("adsb_pulses.npy", pulses.astype(np.uint8))

    print("thr:", thr)
    print("pulse ratio:", float(np.mean(pulses)))


if __name__ == "__main__":
    main()
