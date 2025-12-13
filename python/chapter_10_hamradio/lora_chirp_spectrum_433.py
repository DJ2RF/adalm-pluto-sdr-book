"""
Kapitel 10.4 – LoRa Experimente (433 MHz) – Chirps im Spektrum sichtbar machen

Buch:
sdr.rx_lo = 433920000
sdr.rx_rf_bandwidth = 250000
sdr.rx_sample_rate = 250000
spec = abs(fftshift(fft(samples)))
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(433_920_000)
    sdr.rx_rf_bandwidth = int(250_000)
    sdr.rx_sample_rate = int(250_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)

    spec = np.abs(np.fft.fftshift(np.fft.fft(samples)))
    spec_db = 20 * np.log10(np.maximum(spec, 1e-12))

    plt.figure()
    plt.plot(spec_db)
    plt.title("LoRa Chirps – Spektrum (Ausschnitt)")
    plt.xlabel("FFT Bin")
    plt.ylabel("Amplitude [dB]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
