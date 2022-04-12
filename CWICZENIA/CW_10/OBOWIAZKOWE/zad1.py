from math import inf


# Reprezentacja wierzchołka grafu
class Vertex():
    def __init__(self, index):
        self.number = index
        self.length = 0
        self.visited = False
        self.parent = None
        self.smallest = inf
        self.path = []


# Odwiedzamy wierzchołek v
def DFSVisit(vertexes, G, last, v, t):
    # Sprawdzamy, czy dotarliśmy do naszego wierzchołka
    if v == t:
        # Sprawdzamy, czy znaleźliśmy krótszą trasę
        if v.length < v.smallest:
            v.smallest = v.length
            v.path = getSolution(v)
        return
    v.visited = True
    for e in G[v.number]:
        # Sprawdzamy, czy krawędź po której pójdziemy ma mniejszą wagę niż poprzednia i czy wierzchołek docelowy nie był już odwiedzony
        if e[1] < last and not vertexes[e[0]].visited:
            if v.length + e[1] < t.smallest:
                vertexes[e[0]].parent = v
                vertexes[e[0]].length = v.length + e[1]
                DFSVisit(vertexes, G, e[1], vertexes[e[0]], t)
    v.visited = False


# Wyznacza ścieżkę, po której przyszliśmy
def getSolution(v):
    A = []
    while v != None:
        A.append(v.number)
        v = v.parent
    A.reverse()
    return A


# Przeszukiwanie wzdłuż
def DFS(G, s, t):
    n = len(G)
    # Tworzymy tablicę naszych wierzchołków
    vertexes = []
    for i in range(n):
        vertexes.append(Vertex(i))
    # Uruchamiamy DFS'a dla wierzchołka startowego
    DFSVisit(vertexes, G, inf, vertexes[s], vertexes[t])
    return vertexes[t].path, vertexes[t].smallest


G = [
    [(1, 4), (8, 8)],
    [(0, 4), (2, 8), (8, 11)],
    [(1, 8), (3, 3), (5, 5), (7, 4)],
    [(2, 3), (4, 2), (5, 14)],
    [(3, 2), (5, 0)],
    [(2, 5), (3, 14), (4, 0), (6, 2)],
    [(5, 2), (7, 6), (8, 1)],
    [(2, 4), (6, 6), (8, 7)],
    [(0, 8), (1, 11), (6, 1), (7, 7)]
]
s = 0
t = 4

print(DFS(G, s, t))
