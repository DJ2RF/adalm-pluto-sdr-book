"""
11.1 Pluto als Spektrumanalysator – 433 MHz ISM Spektrum

Buch-Snippet:
sdr.rx_lo = 433920000
sdr.rx_rf_bandwidth = 2000000
sdr.rx_sample_rate = 2000000
N=4096; window=np.hanning(N)
spec = 20*log10(abs(fftshift(fft(samples[:N]*window))))

Leicht verbessert:
- DC entfernen
- log(0)-Schutz
"""

import adi
import numpy as np
import matplotlib.pyplot as plt


def main():
    sdr = adi.Pluto()
    sdr.rx_lo = int(433_920_000)
    sdr.rx_rf_bandwidth = int(2_000_000)
    sdr.rx_sample_rate = int(2_000_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    N = 4096
    window = np.hanning(N)

    samples = np.asarray(sdr.rx())
    samples = samples - np.mean(samples)

    spec = np.fft.fftshift(np.fft.fft(samples[:N] * window))
    spec_db = 20 * np.log10(np.maximum(np.abs(spec), 1e-12))

    plt.figure()
    plt.plot(spec_db)
    plt.title("433 MHz ISM Spektrum")
    plt.xlabel("FFT Bin")
    plt.ylabel("Amplitude [dB]")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
