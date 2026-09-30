from collections import deque
from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    queue = deque([T.root()])
    visto_none = False

    while queue:
        p = queue.popleft()
        izq = T.left(p)
        if izq is not None:
            if visto_none:
                return False
            queue.append(izq)
        else:
            visto_none = True
        der = T.right(p)
        if der is not None:
            if visto_none:
                return False
            queue.append(der)
        else:
            visto_none = True

    return True


def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    camino_p = []
    actual = p
    while actual is not None:
        camino_p.append(actual)
        actual = T.parent(actual)

    camino_q = []
    actual = q
    while actual is not None:
        camino_q.append(actual)
        actual = T.parent(actual)

    lca = None
    while len(camino_p) > 0 and len(camino_q) > 0 and camino_p[-1] == camino_q[-1]:
        lca = camino_p.pop()
        camino_q.pop()

    camino_q.reverse()

    ruta_nodos = camino_p + [lca] + camino_q

    resultado = ""
    for i in range(len(ruta_nodos)):
        if i > 0:
            resultado += " -> "
        resultado += str(ruta_nodos[i].element())

    return resultado


if __name__ == "__main__":
    pass
