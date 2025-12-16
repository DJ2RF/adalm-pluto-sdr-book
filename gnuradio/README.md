
# GNU Radio Experiments – ADALM-Pluto

This directory contains GNU Radio Companion (GRC) flowgraphs and related material
used in the book **“ADALM-Pluto SDR – Praxisbuch für Software Defined Radio”**.

The focus is on **practical, reproducible SDR experiments** using the  
**ADALM-Pluto (AD936x)** with GNU Radio 3.10 and Qt GUI sinks.

---

## Requirements

- **GNU Radio:** ≥ 3.10.5  
- **Python:** 3.10 / 3.11 (Linux recommended)
- **Hardware:** ADALM-Pluto SDR
- **Connection:** USB or Ethernet (`ip:pluto.local`)
- **OS:** Linux (Ubuntu 22.04 / 24.04 tested)

> ⚠️ Note: Pluto support requires `libiio` and the GNU Radio IIO blocks.

## Available Experiments

| ID | Flowgraph | Description |
|----|----------|-------------|
| 00 | Spectrum Viewer | Basic real-time spectrum display using Pluto |
| 01 | Waterfall Viewer | Spectrum + waterfall visualization |
| 02 | IQ Recorder | Record raw complex IQ samples to file |
| 03 | WBFM Receiver | Broadcast FM demodulation |
| 04 | AM Receiver | Simple AM envelope demodulation |
| 05 | FSK / Digital Demo | Basic digital modulation analysis |
| 06 | NOAA APT RX | Weather satellite reception (advanced) |

> The numbering follows the learning path used in the book.

## How to Use

### Open a Flowgraph
gnuradio-companion grc/00_spectrum_viewer.grc
Run from GRC
Press Run (▶)

Make sure the Pluto is reachable (ip:pluto.local)

Adjust frequency, gain, and sample rate as needed

Export to Python
In GNU Radio Companion:

File → Generate → Python Flowgraph
Pluto URI Examples
USB / Ethernet (default):

ip:pluto.local
Static IP:

ip:192.168.2.1
Safety Notice ⚠️
Some flowgraphs may enable transmission (TX).

Always use dummy loads or proper attenuation

Respect local regulations

Never transmit into an antenna without knowing the output power and frequency

Relation to the Book
Each GNU Radio experiment corresponds to one or more chapters in the book.
The goal is hands-on understanding, not black-box SDR usage.

If you are reading the book:
➡️ Start with 00_spectrum_viewer.grc

License
GNU Radio flowgraphs and example code in this directory are provided for
educational use.
See the repository root for full license information.

73 & happy experimenting
Friedrich Riedhammer, DJ2RF