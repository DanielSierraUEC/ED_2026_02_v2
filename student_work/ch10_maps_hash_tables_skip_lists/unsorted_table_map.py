class UnsortedTableMap:
    """Diccionario implementado desde cero con una lista no ordenada de entradas."""

    def __init__(self):
        """Crea un diccionario vacío."""
        self._table = []
    # ---------- auxiliar ----------
    def _buscar(self, k):
        """Retorna el índice de la entrada con clave k, o -1 si no existe."""
        for i in range(len(self._table)):
            if self._table[i][0] == k:
                return i
        return -1

    # ---------- núcleo: métodos especiales ----------
    def __len__(self):
        """Retorna el número de elementos en el diccionario."""
        return len(self._table)

    def __getitem__(self, k):
        """Retorna el valor asociado a la clave k (M[k])."""
        pos = self._buscar(k)
        if pos == -1:
            raise KeyError(k)
        return self._table[pos][1]

    def __setitem__(self, k, v):
        """Asigna v a la clave k (M[k] = v). Inserta o reemplaza."""
        pos = self._buscar(k)
        if pos != -1:
            self._table[pos][1] = v
        else:
            self._table.append([k, v])

    def __delitem__(self, k):
        """Elimina la entrada con clave k (del M[k])."""
        pos = self._buscar(k)
        if pos == -1:
            raise KeyError(k)
        self._table.pop(pos)

    def __contains__(self, k):
        """Retorna True si la clave k está en el diccionario (k in M)."""
        return self._buscar(k) != -1

    def __iter__(self):
        """Recorre las claves del diccionario."""
        for entrada in self._table:
            yield entrada[0]

    def __eq__(self, otro):
        """Compara si dos diccionarios tienen los mismos pares clave-valor."""
        if len(self) != len(otro):
            return False
        for k in self:
            if k not in otro or self[k] != otro[k]:
                return False
        return True

    # ---------- dado ----------
    def __repr__(self):
        return '{' + ', '.join(f'{k!r}: {v!r}' for k, v in self._table) + '}'
