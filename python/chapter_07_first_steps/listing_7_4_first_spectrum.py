"""
Listing 7.4 – Das erste Spektrum anzeigen (FFT)
Buchnah, leicht verbessert: Fensterung, dB-Schutz, Frequenzachse.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

def main():
    sdr = adi.Pluto()

    sdr.rx_lo = int(1_000_000_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    samples = sdr.rx()

    N = 2048
    window = np.hanning(N)
    x = np.asarray(samples[:N]) * window

    spec = np.fft.fftshift(np.fft.fft(x))
    mag = np.abs(spec)
    mag = np.maximum(mag, 1e-12)  # Schutz gegen log(0)
    power_db = 20 * np.log10(mag)

    fs = float(sdr.rx_sample_rate)
    freq = np.fft.fftshift(np.fft.fftfreq(N, d=1.0/fs))

    plt.figure()
    plt.plot(freq/1e6, power_db)
    plt.title("Spektrum am Pluto")
    plt.xlabel("Frequenz [MHz] (relativ zur LO)")
    plt.ylabel("Amplitude [dB]")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
