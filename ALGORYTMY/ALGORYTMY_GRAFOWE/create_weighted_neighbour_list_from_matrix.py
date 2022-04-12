def createList(G):
  n = len(G)
  V = [[] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if G[i][j] != 0:
        V[i].append((j, G[i][j]))
  for v in V:
    print(v)


G = [
  [0, 0, 2, 1, 0, 5, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 3, 7, 0],
  [0, 10, 0, 0, 0, 4, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 4, 4, 2, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
  [0, 11, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 99],
  [0, 0, 0, 0, 2, 0, 6, 0, 4, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
createList(G)