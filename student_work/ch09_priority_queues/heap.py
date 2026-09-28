class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo= len(self.arreglo)-1
        hijo = self.arreglo[indice_hijo]
        indice_padre = indice_hijo//2
        padre = self.arreglo[indice_padre]

        while hijo < padre:
            self.arreglo[indice_hijo], self.arreglo[indice_padre] = self.arreglo[indice_padre], self.arreglo[indice_hijo]
            indice_hijo = indice_padre // 2
            hijo = self.arreglo[indice_hijo]
            padre = self.arreglo[indice_padre]

    def _hundir(self, i):
        n = len(self.arreglo)
        while 2 * i < n:
            hijo_izq = 2 * i
            hijo_der = 2 * i + 1
            hijo_menor = hijo_izq

            if hijo_der < n and self.arreglo[hijo_der] < self.arreglo[hijo_izq]:
                hijo_menor = hijo_der

            if self.arreglo[i] > self.arreglo[hijo_menor]:
                self.arreglo[i], self.arreglo[hijo_menor] = self.arreglo[hijo_menor], self.arreglo[i]
                i = hijo_menor
            else:
                break

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        if len(self.arreglo) == 2:
            return self.arreglo.pop()

        minimo = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()

        self._hundir(1)

        return minimo



    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range((len(self.arreglo) - 1) // 2, 0, -1):
            self._hundir(i)
