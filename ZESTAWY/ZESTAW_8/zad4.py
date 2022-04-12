from math import inf

# Reprezentacja wiezrchołka
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.parent = None


# Czyta krawędzie
def readEdges(E):
    n = len(E)
    for i in range(n):
        for j in range(i + 1, n):
            if E[i][j] == 1:
                print(i, j)

# Odwiedzamy wierzchołek
def DFSVisit(top, E, W, currentV, endV, lastEdge):
    # Sprawdzamy, czy dotarliśmy do szukanego wierzchołka
    if currentV == endV:
        return True
    n = len(top)
    for i in range(n):
        currWeight = W[currentV.number][top[i].number]
        # Sprawdzamy, czy istnieje krawędź i czy waga krawędzi, po której chcemy iść dalej ma mniejszą wagę niż ta, po której przyszliśmy do tego wierzchołka
        if E[currentV.number][i] == 1 and lastEdge > currWeight:
            top[i].parent=currentV.number
            if DFSVisit(top, E, W, top[i], endV, currWeight):
                print(currentV.number, i, currentV.name, top[i].name)
                return True
    # Usuwamy krawędź, po której przyszliśmy
    E[currentV.number][currentV.parent]=0
    E[currentV.parent][currentV.number]=0
    return False

# Sprawdza, czy można przejść z punktu startowego (start) do punktu końcowego (end), po malejących wagach krawędzi
def decreasingEdges(V, E, W, start, end):
    top = []
    for v in V:
        top.append(Summit(v))
    # Zaczynamy z punktu początkowego (start)
    return DFSVisit(top, E, W, top[start], top[end], inf)


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i"), (9, "j"), (10, "k")]
E = [
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
]
W = [
    [0, 15, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [15, 0, 14, 0, 0, 0, 10, 3, 0, 0, 0],
    [0, 14, 0, 13, 12, 5, 0, 0, 0, 0, 0],
    [0, 0, 13, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 12, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7],
    [0, 10, 0, 0, 0, 6, 0, 11, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 11, 0, 9, 2, 0],
    [8, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 1, 0]
]
start = 0
end = 10
print(decreasingEdges(V, E, W, start, end))
