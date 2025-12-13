"""
11.4 Eigenes digitales Protokoll – QPSK Symbolmapping

Buch-Snippet:
symbols = np.array([1+1j, 1-1j, -1+1j, -1-1j])
bits = np.random.randint(0, 4, 1024)
wave = symbols[bits]
sdr.tx(wave)

Leicht verbessert:
- Normierung auf 1/sqrt(2)
- optionales Speichern
"""

import numpy as np

def main():
    symbols = np.array([1+1j, 1-1j, -1+1j, -1-1j]) / np.sqrt(2)
    bits = np.random.randint(0, 4, 1024)
    wave = symbols[bits]

    np.save("qpsk_wave.npy", wave)
    print("Saved -> qpsk_wave.npy", wave.shape)

    # sdr.tx(wave)  # bewusst auskommentiert (TX-Sicherheit)

if __name__ == "__main__":
    main()
