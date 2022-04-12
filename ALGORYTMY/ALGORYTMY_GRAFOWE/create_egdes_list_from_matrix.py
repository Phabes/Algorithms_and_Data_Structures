def createList(G):
  n = len(G)
  L = []
  for i in range(n):
    for j in range(i, n):
      if G[i][j] != 0:
        L.append((i, j, G[i][j]))
  return L


G = [
  [0, 4, 0, 0, 0, 3, 5, 0],
  [4, 0, 7, 0, 0, 0, 3, 0],
  [0, 7, 0, 3, 4, 0, 2, 0],
  [0, 0, 3, 0, 5, 0, 0, 0],
  [0, 0, 4, 5, 0, 0, 1, 8],
  [3, 0, 0, 0, 0, 0, 7, 2],
  [5, 3, 2, 0, 1, 7, 0, 0],
  [0, 0, 0, 0, 8, 2, 0, 0]
]
print(createList(G))