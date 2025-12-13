"""
11.2 Pluto als Signalgenerator – CW

Buch-Snippet:
N=2048
wave = 0.5*exp(j*2*pi*arange(N)/N)
sdr.tx(wave)

WICHTIG: Immer Dummyload + 10–20 dB Dämpfung!
"""

import adi
import numpy as np
import time


def main():
    sdr = adi.Pluto()
    sdr.tx_rf_bandwidth = int(2_000_000)
    sdr.tx_lo = int(1_000_000_000)
    sdr.tx_hardwaregain_chan0 = -10

    N = 2048
    wave = 0.5 * np.exp(1j * 2 * np.pi * np.arange(N) / N)

    sdr.tx(wave)
    print("CW TX läuft (2s)…")
    time.sleep(2)

    try:
        sdr.tx_destroy_buffer()
    except Exception:
        pass


if __name__ == "__main__":
    main()
