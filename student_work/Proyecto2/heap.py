import math
import matplotlib.pyplot as plt

class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]
        self.ultima_figura = None

    def _upheap(self, i):
        while i > 1:
            padre = i // 2
            if self.arreglo[i] < self.arreglo[padre]:
                self.arreglo[i], self.arreglo[padre] = self.arreglo[padre], self.arreglo[i]
                i = padre
            else:
                break

    def _downheap(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            hijo_izq = 2 * i
            hijo_der = 2 * i + 1
            menor = hijo_izq
            if hijo_der <= n and self.arreglo[hijo_der] < self.arreglo[hijo_izq]:
                menor = hijo_der
            if self.arreglo[menor] < self.arreglo[i]:
                self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
                i = menor
            else:
                break

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        self._upheap(len(self.arreglo) - 1)
        if imagen:
            self.mostrar_imagen()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) <= 1:
            return None
        min_val = self.arreglo[1]
        ultimo = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = ultimo
            self._downheap(1)
        if imagen:
            self.mostrar_imagen()
        return min_val

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1
        for i in range(n // 2, 0, -1):
            self._downheap(i)
        if imagen:
            self.mostrar_imagen()

    def mostrar_imagen(self):
        n = len(self.arreglo) - 1
        if n <= 0:
            print("Heap vacío, nada que mostrar.")
            return

        altura = int(math.floor(math.log2(n))) + 1
        pos = {}

        def asignar_pos(idx, x, y, dx):
            if idx > n:
                return
            pos[idx] = (x, y)
            asignar_pos(2 * idx, x - dx, y - 1, dx / 2)
            asignar_pos(2 * idx + 1, x + dx, y - 1, dx / 2)

        asignar_pos(1, 0, 0, 2 ** (altura - 1))

        fig, ax = plt.subplots(figsize=(max(8, 2 ** altura * 0.8), max(6, altura * 1.2)))
        ax.axis('off')

        for i in range(1, n + 1):
            x_p, y_p = pos[i]
            for hijo in (2 * i, 2 * i + 1):
                if hijo <= n:
                    x_c, y_c = pos[hijo]
                    ax.plot([x_p, x_c], [y_p, y_c], color='#555555', lw=2, zorder=1)
        for i in range(1, n + 1):
            x, y = pos[i]
            circle = plt.Circle((x, y), 0.35, color='#4A90E2', ec='black', lw=1.5, zorder=2)
            ax.add_patch(circle)
            ax.text(x, y, str(self.arreglo[i]), color='white', weight='bold', fontsize=11,
                    ha='center', va='center', zorder=3)

        margin = 1.0
        xs = [p[0] for p in pos.values()]
        ys = [p[1] for p in pos.values()]
        ax.set_xlim(min(xs) - margin, max(xs) + margin)
        ax.set_ylim(min(ys) - margin, max(ys) + margin)
        ax.set_aspect('equal')
        plt.tight_layout()
        self.ultima_figura = fig
        plt.show()


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7)
    print(H.arreglo)