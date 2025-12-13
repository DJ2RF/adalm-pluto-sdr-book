"""
Kapitel 9.4 – METEOR-M2 LRPT RX Setup (QPSK, 72 kbit/s)

Dieses Skript zeigt nur die Pluto-Konfiguration und das Aufnehmen von IQ.
Die eigentliche Dekodierung erfolgt typischerweise mit:
- meteor_decoder
- LRPTOfflineDecoder
- GNU Radio
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()

    # Buchwerte (Beispiel 137.9 MHz)
    sdr.rx_lo = int(137_900_000)
    sdr.rx_rf_bandwidth = int(140_000)
    sdr.rx_sample_rate = int(288_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("meteor_lrpt_block.npy", samples)
    print("Saved one block -> meteor_lrpt_block.npy", samples.shape)


if __name__ == "__main__":
    main()
