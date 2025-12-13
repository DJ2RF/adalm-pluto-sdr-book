"""
Kapitel 9.8 – Live Doppler-Tuning mit Gpredict (UDP)

Gpredict kann Doppler-Frequenzen per UDP schicken.
Dieses Skript lauscht auf einem UDP-Port und setzt sdr.rx_lo.

Hinweis:
Das genaue UDP-Format kann je nach Gpredict-Setup variieren.
Dieses Skript akzeptiert:
- reine Zahl (Hz)
- oder eine Zeile mit der Zahl als erstem Token
"""

import socket
import adi


def parse_freq(msg: str) -> int | None:
    msg = msg.strip()
    if not msg:
        return None
    # erster Token als Frequenz interpretieren
    token = msg.split()[0]
    try:
        return int(float(token))
    except ValueError:
        return None


def main(host="0.0.0.0", port=4532):
    sdr = adi.Pluto()
    sdr.rx_rf_bandwidth = int(200_000)
    sdr.rx_sample_rate = int(200_000)
    sdr.gain_control_mode = "manual"
    sdr.rx_hardwaregain = 20

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"Listening for Gpredict UDP on {host}:{port} ...")

    while True:
        data, addr = sock.recvfrom(4096)
        msg = data.decode(errors="ignore")
        freq = parse_freq(msg)
        if freq is None:
            print("Unparsed packet from", addr, ":", msg[:80])
            continue
        sdr.rx_lo = int(freq)
        print("Set LO to", freq, "Hz")


if __name__ == "__main__":
    main()
