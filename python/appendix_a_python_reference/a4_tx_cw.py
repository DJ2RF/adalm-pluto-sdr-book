import numpy as np

N = 2048
wave = 0.5 * np.exp(1j * 2 * np.pi * np.arange(N) / N)
# sdr.tx(wave)
