from queue import PriorityQueue
from math import inf


# Reprezentacja wierzchołka
class Node():
    def __init__(self, number):
        self.number = number
        self.weight = inf
        self.visited = False
        self.parent = None


# Algorytm Prima
def MST_Prime(G, W):
    n = len(G)
    # Tworzymy tablicę reprezentującą nasze wierzchołki
    T = [Node(i) for i in range(n)]
    # Zmieniamy wagę naszego pierwszego wierzchołka na 0 i wrzucamy go do kolejki
    T[0].weight = 0
    # W kolejce będą krotki postaci (waga, index)
    q = PriorityQueue()
    q.put((T[0].weight, T[0].number))
    # Dopóki kolejka priorytetowa nie jest pusta, to ściagamy wierzchołek o najmniejszej wadze
    while not q.empty():
        x = q.get()
        print(x)
        xIndex = x[1]
        # Oznaczamy wierzchołek jako odwiedzony już, żeby nie brać go już później pod uwagę w minimalnym drzewie rozpinającym
        T[xIndex].visited = True
        # Sprawdzamy wszystkie wychodzące krawędzie z naszego wierzchołka
        for i in range(len(G[xIndex])):
            uIndex = G[xIndex][i]
            # Sprawdzamy, czy wierzchołek, z którym łączy się nasz pobrany wierzchołek nie był już odwiedzony
            if not T[uIndex].visited:
                weight = W[xIndex][uIndex]
                # Sprawdzamy, czy waga tej krawędzi jest mniejsza od aktualnie najniższej wagi wierzchołka
                if weight < T[uIndex].weight:
                    T[uIndex].weight = weight
                    T[uIndex].parent = T[xIndex]
                    # T[uIndex].parent = xIndex # Wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
                    q.put((weight, uIndex))
    A = []
    # Tworzymy tablicę naszych krawędzi minimalnego drzewa rozpinającego
    for i in range(n):
        if T[i].parent != None:
            x = [T[i].parent.number, i]
            # x = [T[i].parent, i] # Gdy jest wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
            x.sort()
            A.append((x[0], x[1], W[i][T[i].parent.number]))
            # A.append((x[0], x[1], W[i][T[i].parent])) # Gdy jest wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
    return A


G = [
    [1, 5],
    [0, 2, 5],
    [1, 3, 4, 5],
    [2, 4],
    [2, 3, 5],
    [0, 1, 2, 4]
]
# W = [(0, 1, 1), (0, 5, 12), (1, 2, 5), (1, 5, 7), (2, 3, 3000), (2, 4, 4), (2, 5, 6), (3, 4, 9), (4, 5, 8)]
W = [
    [0, 1, 0, 0, 0, 12],
    [1, 0, 5, 0, 0, 7],
    [0, 5, 0, 3000, 4, 6],
    [0, 0, 3000, 0, 9, 0],
    [0, 0, 4, 9, 0, 8],
    [12, 7, 6, 0, 8, 0],
]
# G = [
#     [1, 5],
#     [0, 2, 3],
#     [1, 3, 5],
#     [1, 2, 4, 5],
#     [3, 5],
#     [0, 2, 3, 4]
# ]
# W = [
#     [0, 5, 0, 0, 0, 2],
#     [5, 0, 6, 4, 0, 0],
#     [0, 6, 0, 9, 0, 3],
#     [0, 4, 9, 0, 1, 8],
#     [0, 0, 0, 1, 0, 7],
#     [2, 0, 3, 8, 7, 0]
# ]

print(MST_Prime(G, W))