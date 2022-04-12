# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None


def hamilton_DAG(V, E):
    def DFSVisit(summits, V, E, v):
        nonlocal time, T
        time += 1
        v.visited = True
        for e in E:
            if v.number == e[0] and not summits[e[1]].visited:
                summits[e[1]].parent = e[0]
                DFSVisit(summits, V, E, summits[e[1]])
        T = [V[v.number]] + T

    summits = []
    for v in V:
        summits.append(Summit(v))
    time = 0
    T = []
    for summit in summits:
        if not summit.visited:
            DFSVisit(summits, V, E, summit)
    print(T)
    for i in range(1,len(T)):
        print(T[i-1][0], summits[T[i][0]].parent)
        if T[i-1][0] != summits[T[i][0]].parent:
            return False
    return True


# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
# E = [(0, 1), (1, 2), (1, 4), (4, 3)]
V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
E = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(hamilton_DAG(V, E))
