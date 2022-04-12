from math import inf


# Znajduję domknięcie przechodnie grafu G
def transitiveClosure(G):
  n = len(G)
  # Uruchamiamy lekko zmodyfikowany algorytm Floyda-Warshalla
  D = [[inf] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if G[i][j] != 0:
        D[i][j] = G[i][j]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        D[j][k] = min(D[j][k], D[j][i] + D[i][k])
  for line in D:
    print(line)
  print()
  # Nasze domknięci przechodnie ma krawędź, gdy algorytm Floyda-Warshalla pokazał, że istnieje ścieżka z "i" do "j"
  for i in range(n):
    for j in range(n):
      if D[i][j] == inf:
        D[i][j] = 0
      else:
        D[i][j] = 1
  for line in D:
    print(line)


G = [
  [0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 1, 0]
]
transitiveClosure(G)