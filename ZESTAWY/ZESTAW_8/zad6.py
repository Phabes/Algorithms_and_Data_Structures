from math import inf


# Reprezentacja wiezrchołka
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.window = [-inf, inf]
        self.parent = None
        self.visited = False


# Czyta krawędzie
def readEdges(E):
    n = len(E)
    for i in range(n):
        for j in range(i + 1, n):
            if E[i][j] == 1:
                print(i, j)

# Tworzy część wspólną przedziałów, jeżeli to możliwe
def changeWindow(win1, win2):
    newWin = [max(win1[0], win2[0]), min(win1[1], win2[1])]
    if newWin[0] > newWin[1]:
        return None
    return newWin

# Odwiedzamy wierzchołek
def DFSVisit(top, E, W, currentV, endV, t):
    print(currentV.parent,currentV.number,currentV.window)
    # Sprawdzamy, czy dotarliśmy do celu
    if currentV==endV:
        return True
    currentV.visited = True
    n = len(top)
    for i in range(n):
        if E[currentV.number][i] == 1 and not top[i].visited:
            currOpt=W[currentV.number][top[i].number]
            x = changeWindow(currentV.window, [currOpt - t, currOpt + t])
            # Sprawdza, czy przedział istnieje
            if x != None:
                top[i].window = x
                top[i].parent = currentV.number
                if DFSVisit(top, E, W, top[i], endV, t):
                    return True
    # Gdy wracamy, musimy oznaczyć wierzchołek, jako nieodwiedzony, aby, można było się do niego dostać ponownie
    currentV.window = [-inf, inf]
    currentV.parent = None
    currentV.visited = False
    return False

# Sprawdza, czy można przelecieć z punktu startowego (start) do końcowego (end)
def safeFlight(V, E, W, start, end, t):
    top = []
    for v in V:
        top.append(Summit(v))
    # Zaczynamy nasz lot z punktu startowego (start)
    return DFSVisit(top, E, W, top[start], top[end], t)


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f")]
E = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]
# W = [
#     [0, 10, 16, 0, 0, 0],
#     [10, 0, 25, 11, 0, 0],
#     [16, 25, 0, 30, 0, 0],
#     [0, 11, 30, 0, 30, 11],
#     [0, 0, 0, 30, 0, 17],
#     [0, 0, 0, 11, 17, 0],
# ]
W = [
    [0, 10, 16, 0, 0, 0],
    [10, 0, 12, 11, 0, 0],
    [16, 12, 0, 17, 0, 0],
    [0, 11, 17, 0, 30, 11],
    [0, 0, 0, 30, 0, 6],
    [0, 0, 0, 11, 6, 0],
]
# W = [
#     [0, 14, 16, 0, 0, 0],
#     [14, 0, 13, 11, 0, 0],
#     [16, 13, 0, 17, 0, 0],
#     [0, 11, 17, 0, 30, 17],
#     [0, 0, 0, 30, 0, 6],
#     [0, 0, 0, 17, 6, 0],
# ]
start = 0
end = 4
t = 5
print(safeFlight(V, E, W, start, end, t))
