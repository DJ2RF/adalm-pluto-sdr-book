"""
Kapitel 10.2 – APRS RX Frontend (145.825 MHz, 1200 Baud AX.25 / AFSK)

Buchwerte:
sdr.rx_lo = 145825000
sdr.rx_sample_rate = 48000
sdr.rx_rf_bandwidth = 20000

Weiterverarbeitung z. B.:
- direwolf (Audio)
- soundmodem
- eigene AFSK Demod

Dieses Skript speichert IQ (oder optional Audio nach Demod aus Kap. 8/10.1).
"""

import adi
import numpy as np

def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(145_825_000)
    sdr.rx_sample_rate = int(48_000)
    sdr.rx_rf_bandwidth = int(20_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    np.save("aprs_iq.npy", samples)
    print("Saved -> aprs_iq.npy", samples.shape)

if __name__ == "__main__":
    main()
