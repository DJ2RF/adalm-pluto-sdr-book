"""
Kapitel 10.6 – QO-100 Downlink RX Setup (via LNB)

Buchhinweis:
sdr.rx_lo = 739000000  # je nach LNB LO (IF-Frequenz)

Wichtig:
Die tatsächliche IF hängt vom LNB-LO und deiner Umsetzung ab.
Dieses Skript ist ein Frontend-Template.
"""

import adi
import numpy as np

def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(739_000_000)        # Beispiel-IF
    sdr.rx_sample_rate = int(1_000_000)
    sdr.rx_rf_bandwidth = int(1_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("qo100_iq.npy", samples)
    print("Saved -> qo100_iq.npy", samples.shape)

if __name__ == "__main__":
    main()
