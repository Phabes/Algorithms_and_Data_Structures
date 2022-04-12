def checkIfNonDirectedGraph(G):
  n = len(G)
  F = [[0] * n for _ in range(n)]
  for i, v in enumerate(G):
    for j in v:
      F[i][j] = 1
  for line in F:
    print(line)
  for i in range(n):
    for j in range(i, n):
      if F[i][j] != F[j][i]:
        return False
  return True


G = [
  [4],
  [3, 4],
  [4],
  [1],
  [0, 1]
]
# G = [
#   [4],
#   [3, 4],
#   [4],
#   [1],
#   [0, 1, 2]
# ]
print(checkIfNonDirectedGraph(G))