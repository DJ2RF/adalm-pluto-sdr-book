"""
Listing 7.2 – Erste Verbindung mit Python (pyadi-iio)
Buchnah, leicht verbessert: klare Ausgabe + URI Hinweis.
"""

import adi

def main():
    sdr = adi.Pluto()  # default: ip:192.168.2.1 via USB-Ethernet
    print("Verbindung erfolgreich:", sdr)

if __name__ == "__main__":
    main()
