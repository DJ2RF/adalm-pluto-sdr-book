# SDR Utils – Python Hilfsbibliothek (Anhang A)

Dieses Verzeichnis enthält die Python-Hilfsfunktionen aus **Anhang A**
des Buches  
**„ADALM-Pluto SDR – Praxisbuch für Software Defined Radio“**.

Die Bibliothek stellt wiederverwendbare Bausteine für alle Kapitel
(Kapitel 3 bis 11) bereit und vermeidet unnötigen Copy-&-Paste-Code
in den Beispielskripten.

---

## Ziel der `utils`

- klare, kurze und gut lesbare Kapitel-Skripte
- saubere Trennung von **Didaktik** und **Implementierung**
- Wiederverwendbarkeit von DSP-, Demodulations- und Messfunktionen
- konsistentes Verhalten über alle Kapitel hinweg

---

## Verzeichnisinhalt

| Datei | Beschreibung |
|------|--------------|
| `pluto_utils.py` | Verbindung, RX/TX-Konfiguration und I/Q-Datentransfer für den ADALM-Pluto |
| `dsp_utils.py` | DSP-Grundfunktionen (DC-Entfernung, FFT, Fenster, dB-Skalierung) |
| `demod_utils.py` | AM-, FM- und frequenzbasierte Demodulationsfunktionen |
| `measurement_utils.py` | Messpraxis: Noise Floor, SNR, Peak-Frequenz, IMD-Hilfen |
| `utils_sample.py` | Lauffähiges Referenz- und Testskript für die utils |
| `__init__.py` | Export der wichtigsten Funktionen für `from utils import …` |

---

## Schnelltest (empfohlen)

Nach Installation der Abhängigkeiten kann die Bibliothek direkt getestet werden:

```bash
python python/utils/utils_sample.py

Erwartetes Ergebnis:

erfolgreiche Verbindung zum ADALM-Pluto

Empfang eines I/Q-Datenblocks

Anzeige eines Spektrums (FFT)

Dieses Skript dient gleichzeitig als Smoke-Test und
als Minimalbeispiel für die Nutzung der utils.

Verwendung in Kapitel-Skripten

Skripte außerhalb des utils-Verzeichnisses (z. B. in chapter_07_first_steps/) importieren die Bibliothek wie folgt:

from utils import (
    pluto_connect,
    pluto_rx_config,
    pluto_rx_block,
    dc_remove,
    spectrum_db,
)


Beispiel:

samples = dc_remove(pluto_rx_block(sdr))
freq, spec_db = spectrum_db(samples, n=4096, fs_hz=2_000_000)

Imports innerhalb von utils

Dateien innerhalb des utils-Ordners verwenden direkte Importe,
damit sie ohne zusätzliche Pfad-Konfiguration ausführbar sind:

from pluto_utils import pluto_connect
from dsp_utils import spectrum_db


Dies erlaubt das direkte Ausführen von utils_sample.py
ohne Anpassung von PYTHONPATH oder sys.path.

Abhängigkeiten

Die benötigten Python-Pakete sind in

python/requirements.txt


aufgeführt.

Minimal erforderlich:

numpy
matplotlib
pyadi-iio