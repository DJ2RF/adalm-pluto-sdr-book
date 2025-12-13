"""
Listing 7.7 – Live Spektrum
Buchnah, leicht verbessert: Ctrl+C sauber, log(0)-Schutz.
"""

import adi
import numpy as np
import matplotlib.pyplot as plt

def main():
    sdr = adi.Pluto()
    sdr.rx_sample_rate = int(2_000_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.rx_lo = int(433_000_000)

    plt.ion()
    fig, ax = plt.subplots()

    try:
        while True:
            samples = np.asarray(sdr.rx())
            spec = np.fft.fftshift(np.fft.fft(samples))
            mag = np.abs(spec)
            mag = np.maximum(mag, 1e-12)

            ax.clear()
            ax.plot(20 * np.log10(mag))
            ax.set_ylim(-120, 0)
            ax.set_title("Live Spektrum")
            ax.set_xlabel("FFT Bin")
            ax.set_ylabel("Amplitude [dB]")
            plt.pause(0.01)
    except KeyboardInterrupt:
        print("Beendet (Ctrl+C).")

if __name__ == "__main__":
    main()
