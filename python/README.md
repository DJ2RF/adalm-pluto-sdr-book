# ADALM-Pluto SDR – Begleitmaterial zum Praxisbuch

Dieses Repository enthält den **begleitenden Quellcode, Beispiele und Materialien**
zum Buch

**„ADALM-Pluto SDR – Praxisbuch für Software Defined Radio“**  
von Friedrich Riedhammer, DJ2RF  
(Nerd Verlag)

Der Fokus liegt auf **praxisnahen Python-Beispielen** für den
**ADALM-Pluto SDR** von Analog Devices.

## Ziel dieses Repositories

- Ergänzung zum Buch (kein Ersatz)
- lauffähige, verständliche Python-Beispiele
- reproduzierbare Experimente mit realen Funksignalen
- saubere Trennung von:
  - Kapitel-Beispielen
  - wiederverwendbaren Hilfsfunktionen (Anhang A)

## Inhalt & Struktur

.
├── python/
│ ├── utils/ # Hilfsbibliothek (Anhang A)
│ ├── chapter_03_... # Kapitelbezogene Beispiele
│ ├── chapter_04_...
│ ├── chapter_08_...
│ ├── chapter_10_...
│ ├── chapter_11_...
│ ├── ENV_SETUP.md # Ausführliche Installationsanleitung
│ └── requirements.txt
└── README.md # Diese Datei

## Voraussetzungen

- ADALM-Pluto SDR
- Linux (Ubuntu/Debian empfohlen)
- Python ≥ 3.9
- Grundkenntnisse in Python und Signalverarbeitung sind hilfreich

## Schnellstart (empfohlen)

1. Repository klonen
2. **Installationsanleitung lesen:**

👉 **[`python/ENV_SETUP.md`](python/ENV_SETUP.md)**

Dort sind alle Schritte zur Einrichtung einer funktionierenden
Python-Umgebung mit `pyadi-iio` beschrieben.

## Die utils-Bibliothek (Anhang A)

Im Verzeichnis `python/utils` befindet sich eine kleine Hilfsbibliothek,
die im Buch als **Anhang A** beschrieben ist.

Sie enthält u. a.:

- Pluto-Initialisierung & RX/TX-Konfiguration
- DSP-Grundfunktionen (FFT, dB, Fenster)
- einfache Demodulatoren (AM/FM)
- Messfunktionen (Noise Floor, SNR, IMD)

👉 Einstieg & Test:

python python/utils/utils_sample.py

