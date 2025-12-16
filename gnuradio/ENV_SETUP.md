# Environment Setup – GNU Radio & ADALM-Pluto

This document describes the setup required to use **GNU Radio** with the  
**ADALM-Pluto SDR** for the experiments provided in this repository.

The focus is on a **stable Linux-based setup** (Ubuntu), which is also used
throughout the book.

---

## Recommended Platform

- **Operating System:** Ubuntu 22.04 LTS or 24.04 LTS
- **Architecture:** x86_64 (64-bit)
- **GNU Radio:** ≥ 3.10.5
- **Python:** 3.10 or newer
- **Hardware:** ADALM-Pluto SDR

> ⚠️ Windows and macOS are possible, but Linux is strongly recommended
> for reproducibility and driver stability.

---

## 1. System Preparation

Update the system and install basic build tools:

sudo apt update
sudo apt upgrade
sudo apt install -y \
  git \
  cmake \
  build-essential \
  pkg-config \
  usbutils \
  net-tools

## 2. Install GNU Radio (3.10)
Install GNU Radio from the Ubuntu repositories:

sudo apt install -y gnuradio
Verify the installation:

gnuradio-companion --version
Expected output (example):

nginx
Code kopieren
GNU Radio Companion 3.10.5.1

## 3. Install libiio & Pluto Support

The ADALM-Pluto uses libiio for communication.

Install libiio and GNU Radio IIO blocks

sudo apt install -y \
  libiio-utils \
  libiio-dev \
  gr-iio
Verify IIO tools:

iio_info -s
You should see the Pluto listed, e.g.:

Available contexts:
  0: ip:pluto.local

## 4. Connect the ADALM-Pluto

USB (default)
Plug in the Pluto via USB

The device exposes:

USB serial

USB mass storage

USB Ethernet interface

Check network interface
ip a
You should see an interface similar to:

usb0
Test Pluto connectivity
ping pluto.local
or directly:
iio_info -u ip:pluto.local

## 5. GNU Radio Pluto Blocks

After installing gr-iio, GNU Radio Companion should provide blocks such as:

PlutoSDR Source
IIO Pluto Source
FMComms2 Source
In GNU Radio Companion:
Open the block tree
Search for pluto or iio
If the blocks are missing:
Restart GNU Radio Companion
Verify gr-iio is installed

## 6. Python Environment (optional but recommended)

For Python-based SDR experiments (outside GRC), use a virtual environment.

Create a virtual environment
python3 -m venv venv
source venv/bin/activate
Install pyadi-iio
pip install pyadi-iio
Verify:
python -c "import adi; print(adi.__version__)"
⚠️ Note:
On some systems, pyadi-iio requires a virtual environment because
system Python packages are restricted.

## 7. Common Pluto URI Settings

Typical Pluto URIs used in this repository:

ip:pluto.local
or with static IP:

ip:192.168.2.1
These URIs are used consistently in all .grc flowgraphs.

## 8. Performance & Stability Tips

Disable unnecessary background applications

Avoid USB hubs (connect Pluto directly)

Use sample rates ≤ 5 MS/s for stable operation

Start with manual gain before using AGC

## 9. Troubleshooting

Pluto not found
iio_info -s
Check USB cable

Check network interface (usb0)

Try replugging the device

GNU Radio error: missing IIO blocks
sudo apt install gr-iio
Permission issues
sudo usermod -a -G plugdev $USER
Log out and log in again.

## 10. Scope of This Setup

This setup supports:

Spectrum & waterfall analysis
IQ recording
FM / AM / digital demodulation
Satellite reception experiments
Basic TX experiments (with care!)
Safety Notice ⚠️
Some experiments enable RF transmission.

Always use proper attenuation or dummy loads

Follow local RF regulations

Never transmit blindly into an antenna

References
Analog Devices Pluto SDR:
https://www.analog.com/pluto

GNU Radio:
https://www.gnuradio.org

libiio:
https://github.com/analogdevicesinc/libiio

73 & happy experimenting
Friedrich Riedhammer, DJ2RF