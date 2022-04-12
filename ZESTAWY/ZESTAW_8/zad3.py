from queue import PriorityQueue


# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None
        self.wave = -1

# Wrzucamy kamień do wierzchołka (start)
def BFS(top, E, start, end):
    top[start].visited = True
    top[start].wave = 0
    q = PriorityQueue()
    q.put(start)
    n = len(top)
    while not q.empty():
        # Poberamy element z kolejki
        index = q.get()
        for i in range(n):
            # Sprawdzamy, czy istanieje krawędź i czy wierzchołek nie został już odwiedzony
            if E[index][i] == 1 and not top[i].visited:
                top[i].visited = True
                top[i].parent = index
                top[i].wave = top[index].wave + 1
                q.put(i)
    # for v in top:
    #     print(v.name, v.wave, v.parent)
    T=findIndexes(top, end, [])
    readSolution(top,T)
    return T


# Znajduje indexy wierzchołków wchodzących w skład najkrótszej ścieżki
def findIndexes(top, index, T):
    v = top[index]
    if v.parent != None:
        findIndexes(top, v.parent,T)
    T.append(v.number)
    return T

# Odczytuje rozwiązanie
def readSolution(top,T):
    n=len(T)
    for i in range(n):
        print(top[T[i]].name, end="")
        if i!=n-1:
            print(" --> ", end="")
        else:
            print()


# Wyznacza najkrótszą ścieżkę od punktu początkowego (start), do punktu koncowego (end)
def shortestPath(V, E, start, end):
    top = []
    for v in V:
        top.append(Summit(v))
    return BFS(top, E, start, end)


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
start = 0
end = 10
print(shortestPath(V, E, start, end))
