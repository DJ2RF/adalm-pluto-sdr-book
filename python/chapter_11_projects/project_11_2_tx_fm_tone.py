"""
11.2 Pluto als Signalgenerator – FM-Ton (1 kHz)

Buch-Snippet:
fs = 2000000
t = arange(2048)/fs
fm_tone = exp(j*2*pi*(f_c + deviation*sin(2*pi*1000*t))*t)
sdr.tx(fm_tone)

Leicht verbessert:
- separates baseband (freq deviation als Phase-Integral)
- einfache Parameter
"""

import adi
import numpy as np
import time


def main():
    sdr = adi.Pluto()
    sdr.tx_sample_rate = int(2_000_000)
    sdr.tx_rf_bandwidth = int(2_000_000)
    sdr.tx_lo = int(1_000_000_000)
    sdr.tx_hardwaregain_chan0 = -10

    fs = float(sdr.tx_sample_rate)
    N = 2048
    tone_hz = 1000.0
    deviation_hz = 5000.0  # anpassen

    t = np.arange(N) / fs

    # FM: Phase(t) = 2π * ∫ f_inst dt, mit f_inst = deviation*sin(2π f_tone t)
    phase = 2 * np.pi * (deviation_hz / tone_hz) * (1 - np.cos(2 * np.pi * tone_hz * t))
    fm = 0.5 * np.exp(1j * phase)

    sdr.tx(fm)
    print("FM-Ton TX läuft (2s)…")
    time.sleep(2)

    try:
        sdr.tx_destroy_buffer()
    except Exception:
        pass


if __name__ == "__main__":
    main()
