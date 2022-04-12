from queue import PriorityQueue

inf = float('inf')


class Node:
    def __init__(self, name):
        self.name = name
        self.d = inf
        self.parent = None
        self.last = inf


def Dijkstra(G, f, l):

    n = len(G)
    T = [Node(i) for i in range(n)]
    T[f].d = 0
    Q = PriorityQueue()
    Q.put((T[f].d, T[f].name))
    while not Q.empty():
        v = Q.get()
        check = True
        for i in range(n):
            if G[v[1]][i] > 0 and i != T[v[1]].parent:
                if relax(T[v[1]], T[i], G[v[1]][i]):
                    Q.put((G[v[1]][i]+v[0], i))
                    check = False
        if check and v[1] != l:
            T[v[1]].d = inf
    if T[l].parent == None:
        print("NIE MA")
    else:
        print(f, end=" ")
        getPath(T, f, l)
        print("dist:", T[l].d)


def relax(u, v, w):
    if v.d > u.d + w and u.last > w:
        v.d = u.d+w
        v.parent = u.name
        v.last = w
        return True
    return False


def getPath(T, f, cur):
    if cur != f:
        getPath(T, f, T[cur].parent)
        print(T[cur].name, end=" ")


#  0 4 6 dist: 18 0-6
G = [
    [0, 5, 0, 0, 11, 2, 0, 0, 0],
    [5, 0, 6, 4, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [11, 0, 0, 0, 0, 0, 7, 1, 2],
    [2, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 7, 3, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
]

# 0 8 7 2 3 4 dist: 24  0-4
# G = [[0, 4, 0, 0, 0, 0, 0, 0, 8],
#      [4, 0, 8, 0, 0, 0, 0, 0, 11],
#      [0, 8, 0, 3, 0, 5, 0, 4, 0],
#      [0, 0, 3, 0, 2, 14, 0, 0, 0],
#      [0, 0, 0, 2, 0, 1, 0, 0, 0],
#      [0, 0, 5, 14, 1, 0, 3, 0, 0],
#      [0, 0, 0, 0, 0, 3, 0, 6, 1],
#      [0, 0, 4, 0, 0, 0, 6, 0, 7],
#      [8, 11, 0, 0, 0, 0, 1, 7, 0]]

# # 0 8 7 6 5 4 dist: 25  0-4
# G = [[0, 4, 0, 0, 0, 0, 0, 0, 8],
#      [4, 0, 8, 0, 0, 0, 0, 0, 11],
#      [0, 8, 0, 3, 0, 5, 0, 4, 0],
#      [0, 0, 3, 0, 4, 14, 0, 0, 0],
#      [0, 0, 0, 2, 0, 1, 0, 0, 0],
#      [0, 0, 5, 14, 1, 0, 3, 0, 0],
#      [0, 0, 0, 0, 0, 3, 0, 6, 1],
#      [0, 0, 4, 0, 0, 0, 6, 0, 7],
#      [8, 11, 0, 0, 0, 0, 1, 7, 0]]

# # ([0, 2, 4, 3], 12)  0-3
# G = [[0, 10, 5, 0, 0, 0],
#      [10, 0, 1, 3, 2, 0],
#      [5, 1, 0, 6, 4, 0],
#      [0, 3, 6, 0, 3, 2],
#      [0, 2, 4, 3, 0, 1],
#      [0, 0, 0, 2, 1, 0]]

# # ([0, 3, 2], 7) 0-2
# G = [[0, 10, 0, 4],
#      [10, 0, 10, 0],
#      [0, 10, 0, 3],
#      [4, 0, 3, 0]]


# # ([0, 1, 6, 5, 4, 3, 2], 39) 0-2
# G = [[0, 9, 0, 0, 0, 0, 0],
#      [9, 0, 10, 0, 0, 0, 8],
#      [0, 10, 0, 4, 0, 0, 8],
#      [0, 0, 4, 0, 5, 0, 0],
#      [0, 0, 0, 5, 0, 6, 0],
#      [0, 0, 0, 0, 6, 0, 7],
#      [0, 8, 8, 0, 0, 7, 0]]


# # ([0, 2, 3, 4, 5], 10) 0-5
# G = [[0, 2, 4, 0, 0, 0],
#      [2, 0, 10, 0, 12, 100],
#      [4, 10, 0, 3, 0, 0],
#      [0, 0, 3, 0, 2, 0],
#      [0, 12, 0, 2, 0, 1],
#      [0, 100, 0, 0, 1, 0]]


Dijkstra(G, 0, 6)
