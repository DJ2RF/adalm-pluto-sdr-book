"""
11.6 LoRa-Decoder – Setup Template

Kapitel nennt die Schritte (FFT -> Chirp -> Despreading -> FEC -> Payload)
und gibt das Pluto-Setup.

Dieses Skript speichert IQ für Offline-Analyse.
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(433_920_000)
    sdr.rx_sample_rate = int(250_000)
    sdr.rx_rf_bandwidth = int(250_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("lora_iq.npy", samples)
    print("Saved -> lora_iq.npy", samples.shape)


if __name__ == "__main__":
    main()
