"""
Kapitel 9.7 – ICARUS Downlink (401–403 MHz)

Buchwerte:
sdr.rx_lo = 402000000
sdr.rx_rf_bandwidth = 200000
sdr.rx_sample_rate = 200000

Hinweis:
Sehr schneller Doppler (±12 kHz), Signal oft schwach -> LNA/Yagi empfohlen.
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(402_000_000)
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("icarus_iq.npy", samples)
    print("Saved -> icarus_iq.npy", samples.shape)


if __name__ == "__main__":
    main()
