# Chapter 9 – Satellitenempfang (NOAA, METEOR, ISS, ICARUS)

Python-Beispiele zu Kapitel 9 des Buches.

## Inhalte
- NOAA APT: Aufnahme eines kompletten Passes in eine .npy Datei
- METEOR-M2 LRPT: RX-Setup (QPSK, externer Decoder)
- ISS (ARISS Voice/APRS): RX-Setups
- ICARUS (401–403 MHz): RX-Setup + Doppler-Hinweis
- Doppler-Korrektur: (a) Liste von Frequenzen, (b) Live via Gpredict UDP

Hinweis:
Diese Skripte liefern das IQ-Frontend (Pluto). Decoding/Audio-Pipelines
erfolgen typischerweise in GNU Radio / externen Tools.
