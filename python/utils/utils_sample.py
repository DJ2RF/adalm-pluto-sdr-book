"""
utils_sample.py

Referenz- und Testskript für die utils-Bibliothek (Anhang A).

Zeigt:
- Pluto-Verbindung
- RX-Konfiguration
- DC-Entfernung
- FFT + dB-Spektrum

Gedacht als:
- Smoke-Test
- Minimalbeispiel
- Einstieg für neue Leser
"""

import matplotlib.pyplot as plt

# relative Imports aus utils
from pluto_utils import pluto_connect, pluto_rx_config, pluto_rx_block, RxConfig
from dsp_utils import dc_remove, spectrum_db


def main():
    print("Connecting to Pluto...")
    sdr = pluto_connect()

    print("Configuring RX...")
    rx_cfg = RxConfig(
        lo_hz=433_920_000,
        sample_rate_hz=2_000_000,
        rf_bw_hz=2_000_000,
        gain_db=20,
    )
    pluto_rx_config(sdr, rx_cfg)

    print("Receiving samples...")
    samples = pluto_rx_block(sdr)

    print("Processing...")
    samples = dc_remove(samples)

    freq, spec_db = spectrum_db(
        samples,
        n=4096,
        fs_hz=rx_cfg.sample_rate_hz,
        window="hann",
    )

    print("Plotting spectrum...")
    plt.figure()
    plt.plot(freq / 1e3, spec_db)
    plt.title("utils sample – Pluto spectrum")
    plt.xlabel("Frequency [kHz] (relative to LO)")
    plt.ylabel("Amplitude [dB]")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
