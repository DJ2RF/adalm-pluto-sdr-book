"""
Listing 7.3 – Erste Samples empfangen (RX)
Buchnah, leicht verbessert: typisierte ints + kompakte Ausgabe.
"""

import adi
import numpy as np

def main():
    sdr = adi.Pluto()

    sdr.rx_lo = int(1_000_000_000)          # 1 GHz
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = sdr.rx()
    print("Samples (erste 10):", np.asarray(samples[:10]))

if __name__ == "__main__":
    main()
