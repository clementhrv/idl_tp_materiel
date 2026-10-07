import csv
import sys
import matplotlib.pyplot as plt

CSV_FILE = sys.argv[1] if len(sys.argv) > 1 else "mountain.csv"
SIZE = 32 * 1024

strides = []
speeds = []

with open(CSV_FILE, newline="") as file:
    for row in csv.DictReader(file):
        if int(row["size_bytes"]) == SIZE:
            strides.append(int(row["stride"]))
            speeds.append(float(row["mbps"]) / 1000)

if not strides:
    raise SystemExit("Aucune mesure trouvée pour 32 Kio.")

for stride, speed in zip(strides, speeds):
    print(f"pas {stride:>2} : {speed:.1f} Go/s")

plt.plot(strides, speeds, "o-")
plt.xlabel("Pas (éléments de 8 octets)")
plt.ylabel("Débit (Go/s)")
plt.title("Effet du pas pour un tableau de 32 Kio (L1)")
plt.grid(True)
plt.savefig("mountain_stride32K.png", dpi=120)
print("Figure écrite dans mountain_stride32K.png")
