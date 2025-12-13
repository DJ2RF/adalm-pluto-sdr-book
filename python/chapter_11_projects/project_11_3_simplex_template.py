"""
11.3 Pluto als Simplex-Transceiver (Template)

Kapitel-Idee:
"Sende ein Signal -> empfange Antwort -> analysiere IQ"

Hinweis:
Kein Full-Duplex. Typisch: TX-Burst, dann RX-Fenster.
"""

import adi
import numpy as np
import time


def main():
    sdr = adi.Pluto()

    # Gemeinsame Parameter (anpassen)
    lo = int(433_920_000)
    fs = int(1_000_000)
    bw = int(1_000_000)

    # RX
    sdr.rx_lo = lo
    sdr.rx_sample_rate = fs
    sdr.rx_rf_bandwidth = bw
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    # TX
    sdr.tx_lo = lo
    sdr.tx_sample_rate = fs
    sdr.tx_rf_bandwidth = bw
    sdr.tx_hardwaregain_chan0 = -10

    # kurzer TX-Burst
    N = 2048
    wave = 0.5 * np.exp(1j * 2 * np.pi * np.arange(N) / N)
    sdr.tx(wave)
    time.sleep(0.2)
    try:
        sdr.tx_destroy_buffer()
    except Exception:
        pass

    # RX-Fenster
    rx = np.asarray(sdr.rx())
    np.save("simplex_rx.npy", rx)
    print("Saved RX -> simplex_rx.npy", rx.shape)


if __name__ == "__main__":
    main()
