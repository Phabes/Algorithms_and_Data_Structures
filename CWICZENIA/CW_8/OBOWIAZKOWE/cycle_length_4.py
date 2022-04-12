def DFS(G, marked, n, v, start):
    V=len(G)
    marked[v] = True
    if n == 0:
        marked[v] = False
        if G[v][start] == 1:
            return True
        return False
    for i in range(V):
        if not marked[i] and G[v][i] == 1:
            if DFS(G, marked, n - 1, i, start):
                return True
    marked[v] = False
    return False


def countCycles(G, n):
    V=len(G)
    marked = [False] * V
    for i in range(V - (n - 1)):
        if DFS(G, marked, n - 1, i, i):
            return True
        marked[i] = True


G = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]

n = 4
print(countCycles(G, n))