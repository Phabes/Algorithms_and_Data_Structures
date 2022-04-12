def createList(G):
  n = len(G)
  V = [[] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if G[i][j] == 1:
        V[i].append(j)
  for v in V:
    print(v)


G = [
  [0, 0, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0],
  [1, 1, 0, 0, 0]
]
createList(G)