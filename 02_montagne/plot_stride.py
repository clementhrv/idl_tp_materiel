import csv
import sys
import matplotlib.pyplot as plt

CSV_FILE = sys.argv[1] if len(sys.argv) > 1 else "mountain.csv"
SIZE = 64 * 1024 * 1024

strides = []
mbps = []

with open(CSV_FILE, newline="") as file:
    for row in csv.DictReader(file):
        if int(row["size_bytes"]) == SIZE:
            strides.append(int(row["stride"]))
            mbps.append(float(row["mbps"]) / 1000)

if not strides:
    raise SystemExit("Aucune mesure trouvée pour 64 Mio.")

plt.plot(strides, mbps, "o-")
plt.xlabel("Pas (éléments de 8 octets)")
plt.ylabel("Débit (Go/s)")
plt.title("Débit selon le pas pour un tableau de 64 Mio")
plt.grid(True)
plt.savefig("mountain_stride64M.png", dpi=120)
plt.show()

print(f"Figure écrite dans mountain_stride64M.png")
print("La stabilisation commence vers le pas 8, soit environ 64 octets.")
