"""
Kapitel 9.2 / Anhang A.6.2 – Doppler-Korrektur per Liste

Buchidee:
for f in doppler_list:
    sdr.rx_lo = int(f)
    block = sdr.rx()

Leicht verbessert:
- speichert pro Schritt kleine Blöcke
- zeigt Fortschritt
"""

import adi
import numpy as np


def main():
    sdr = adi.Pluto()
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    # Beispiel-Liste (ersetzen durch echte Doppler-Frequenzen)
    doppler_list = [
        145_801_500, 145_801_000, 145_800_500, 145_800_000, 145_799_500
    ]

    blocks = []
    for i, f in enumerate(doppler_list, start=1):
        sdr.rx_lo = int(f)
        block = np.asarray(sdr.rx())
        blocks.append(block)
        print(f"{i}/{len(doppler_list)}  LO={f} Hz  block={block.shape}")

    out = np.concatenate(blocks)
    np.save("doppler_blocks.npy", out)
    print("Saved -> doppler_blocks.npy", out.shape)


if __name__ == "__main__":
    main()
