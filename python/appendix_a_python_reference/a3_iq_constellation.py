import numpy as np
import matplotlib.pyplot as plt

plt.scatter(np.real(samples), np.imag(samples), s=2)
plt.xlabel("I")
plt.ylabel("Q")
plt.grid(True)
plt.title("I/Q-Konstellation")
plt.show()
