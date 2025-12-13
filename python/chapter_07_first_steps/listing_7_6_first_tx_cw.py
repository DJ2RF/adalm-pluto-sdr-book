"""
Listing 7.6 – Pluto als Sender: erstes TX-Signal (CW)
Buchnah, leicht verbessert: Kommentar + Stop/Destroy Hinweis.
WICHTIG: Dummyload + 10–20 dB Dämpfung verwenden!
"""

import adi
import numpy as np
import time

def main():
    sdr = adi.Pluto()

    sdr.tx_rf_bandwidth = int(2_000_000)
    sdr.tx_lo = int(1_000_000_000)  # 1 GHz
    sdr.tx_hardwaregain_chan0 = -10

    N = 2048
    wave = 0.5 * np.exp(1j * 2 * np.pi * np.arange(N) / N)

    sdr.tx(wave)
    print("TX läuft (CW). Stoppe in 2 Sekunden...")
    time.sleep(2)

    # TX stoppen (pyadi-iio: destroy_buffer ist üblich)
    try:
        sdr.tx_destroy_buffer()
    except Exception:
        pass

if __name__ == "__main__":
    main()
