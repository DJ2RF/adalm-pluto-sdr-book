import numpy as np
import matplotlib.pyplot as plt

# erwartet: 'samples' ist ein komplexes numpy-array
N = 4096
window = np.hanning(N)

fft_data = np.fft.fftshift(np.fft.fft(samples[:N] * window))
power = 20 * np.log10(np.maximum(np.abs(fft_data), 1e-12))

plt.plot(power)
plt.title("Spektrum")
plt.show()
