# 1. Stellen Sie sicher, dass das venv-Modul installiert ist (falls noch nicht geschehen)
sudo apt update
sudo apt install python3-full

# 2. Erstellen Sie eine virtuelle Umgebung im aktuellen Verzeichnis (z.B. mit dem Namen "venv")
python3 -m venv venv

# 3. Aktivieren Sie die virtuelle Umgebung
source venv/bin/activate

# 4. Installieren Sie das Paket mit pip3 (jetzt innerhalb der venv)
pip3 install pyadi-iio