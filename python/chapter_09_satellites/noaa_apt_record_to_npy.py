"""
Kapitel 9.3 / 9.10 – NOAA APT aufnehmen und als .npy speichern

Buch-Snippet:
samples = []
for _ in range(400):
    samples.extend(sdr.rx())
np.save("noaa_pass.npy", samples)

Leicht verbessert:
- numpy array direkt
- sample count/shape
- Parametrisierung der "Blöcke"
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()

    # Buchwerte für NOAA APT (137.10 MHz Beispiel)
    sdr.rx_lo = int(137_100_000)
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(240_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    blocks = 400  # Buchwert
    buf = []

    for i in range(blocks):
        buf.append(np.asarray(sdr.rx()))
        if (i + 1) % 50 == 0:
            print(f"Recorded {i+1}/{blocks} blocks...")

    samples = np.concatenate(buf)
    np.save("noaa_pass.npy", samples)
    print("Saved:", samples.shape, "-> noaa_pass.npy")


if __name__ == "__main__":
    main()
