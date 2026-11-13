import matplotlib
matplotlib.use("Agg")
import os
from heap import Heap

os.makedirs("fotos", exist_ok=True)
valores = [15, 8, 20, 3, 10]
H = Heap()
for i, v in enumerate(valores, start=1):
    H.insert(v, imagen=True)
    H.ultima_figura.savefig(f"fotos/insert_{i}.png")
    print(i, H.arreglo)