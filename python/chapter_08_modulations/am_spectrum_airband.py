"""
Kapitel 8.1 AM – Airband-Setup (Beispiel) + Spektrumsanzeige

Buchnahes Setup (LO/Bandbreite/Samplerate) und FFT-Darstellung.
Leicht verbessert: Fensterung, dB-Schutz, Frequenzachse relativ zur LO.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def main():
    sdr = adi.Pluto()

    # AM Airband Beispiel-Setup
    sdr.rx_lo = int(125_000_000)        # Beispiel: 125 MHz (Airband)
    sdr.rx_rf_bandwidth = int(100_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())

    N = 4096
    x = samples[:N]
    x = x - np.mean(x)                 # DC-Entfernung (leicht verbessert)
    window = np.hanning(len(x))
    spec = np.fft.fftshift(np.fft.fft(x * window))

    mag = np.maximum(np.abs(spec), 1e-12)
    power_db = 20 * np.log10(mag)

    fs = float(sdr.rx_sample_rate)
    freq = np.fft.fftshift(np.fft.fftfreq(len(x), d=1.0 / fs))

    plt.figure()
    plt.plot(freq / 1e3, power_db)
    plt.title("AM Spektrum (relativ zur LO)")
    plt.xlabel("Frequenz [kHz]")
    plt.ylabel("Amplitude [dB]")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
