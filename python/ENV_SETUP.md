# Python Environment Setup – ADALM-Pluto SDR (pyadi-iio)

Dieses Dokument beschreibt die Installation und Einrichtung der Python-Umgebung
für die Beispiele in diesem Repository (ADALM-Pluto SDR Buch).

Ziel: Eine stabile, reproduzierbare Umgebung für `pyadi-iio` und den ADALM-Pluto.

---

## 1) Wichtige Grundregel: nicht global installieren

Installiere Python-Pakete **nicht global** mit `pip` (System-Python).
Nutze stattdessen immer eine virtuelle Umgebung (`venv`).

Viele Linux-Systeme blockieren heute globale pip-Installationen
(`externally-managed-environment`) – `venv` ist der saubere Weg.

---

## 2) Unterstützte Plattformen

- **Linux (Ubuntu/Debian):** empfohlen, vollständig unterstützt
- **Windows:** empfohlen über **WSL2 (Ubuntu)**
- **macOS:** möglich, aber nicht in allen Setups getestet

---

# Linux / Ubuntu / Debian (empfohlen)

## Schritt 1: Systempakete installieren

```bash
sudo apt update
sudo apt install python3-full python3-venv python3-pip libiio0 libiio-dev

Warum?

python3-venv: virtuelle Umgebung

python3-full: vollständige Python-Installation (weniger „fehlende Module“)

libiio: Kommunikation mit IIO/Pluto (je nach Setup hilfreich)

## Schritt 2: In das Repository wechseln
cd <dein-repo>
cd python

## Schritt 3: Virtuelle Umgebung erstellen
python3 -m venv venv

Dadurch entsteht python/venv/.

## Schritt 4: Virtuelle Umgebung aktivieren
source venv/bin/activate

Danach siehst du typischerweise (venv) in der Shell.

## Schritt 5: pip aktualisieren
pip install --upgrade pip

## Schritt 6: Python-Abhängigkeiten installieren

Empfohlen (alle Beispiele):

pip install -r requirements.txt

Minimal (nur Pluto testen):

pip install pyadi-iio

## Schritt 7: Verbindung zum Pluto testen
python -c "import adi; sdr = adi.Pluto(); print(sdr)"

Falls nötig (explizit):

import adi
sdr = adi.Pluto("ip:192.168.2.1")
print(sdr)

Schritt 8: utils-Smoke-Test
python python/utils/utils_sample.py

Erwartung:

Verbindung zum Pluto

Empfang eines IQ-Blocks

Anzeige eines Spektrums (FFT)

Windows (WSL2 empfohlen)

Für Windows wird WSL2 + Ubuntu empfohlen.
Dann gelten die Linux-Schritte identisch.

Typische Probleme & Lösungen
Problem: externally-managed-environment

Ursache: globale Installation mit pip.
Lösung: venv aktivieren:

source venv/bin/activate

Problem: Pluto nicht erreichbar

Pluto per USB angeschlossen?

ping 192.168.2.1 möglich?

ggf. explizit verbinden:

adi.Pluto("ip:192.168.2.1")

Problem: libiio / iio fehlt

Installiere:

sudo apt install libiio0 libiio-dev

Dann venv neu aktivieren und Test wiederholen.

Virtuelle Umgebung beenden
deactivate

# 1. Stellen Sie sicher, dass das venv-Modul installiert ist (falls noch nicht geschehen)
sudo apt update
sudo apt install python3-full

# 2. Erstellen Sie eine virtuelle Umgebung im aktuellen Verzeichnis (z.B. mit dem Namen "venv")
python3 -m venv venv

# 3. Aktivieren Sie die virtuelle Umgebung
source venv/bin/activate

# 4. Installieren Sie das Paket mit pip3 (jetzt innerhalb der venv)
pip3 install pyadi-iio

Virtuelle Umgebung beenden
deactivate