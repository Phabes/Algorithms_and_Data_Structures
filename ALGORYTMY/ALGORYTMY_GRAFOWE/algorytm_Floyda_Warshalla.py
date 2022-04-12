from math import inf


def algorithm_Floyd_Warshall(G):
  n = len(G)
  # Tablica reprezentująca najkrótsze ścieżki między wierzchołkami
  D = [[inf] * n for _ in range(n)]
  # Tablica pomagająca odczytać rozwiązanie (tablica nextów)
  P = [[inf] * n for _ in range(n)]
  # Każdy wierzchołek nie ma odległości od siebie
  for i in range(n):
    D[i][i] = 0
  # Jeśli jest krawędź z "i" do "j" to nadajemy naszej ścieżce między nimi wartość tej krawędzi
  for i in range(n):
    for j in range(n):
      if G[i][j] != inf:
        D[i][j] = G[i][j]
        P[i][j] = j
      else:
        P[i][j] = -1
  for line in D:
    print(line)
  print()
  for line in P:
    print(line)
  print()
  # Dla każdego wierzchołka "i" grafu G i każdej pary wierzchołków "j", "k"  badamy, czy koszt dojścia D[j][k] jest większy od sumy kosztów dojść D[j][i] + D[i][k]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        # D[j][k] = min(D[j][k], D[j][i] + D[i][k])
        if D[j][k] > D[j][i] + D[i][k]:
          D[j][k] = D[j][i] + D[i][k]
          P[j][k] = P[j][i]
  for line in D:
    print(line)
  print()
  for line in P:
    print(line)
  print()
  print(readPath(1, 4, P), D[1][4])


# Odczytuje ścieżkę między dwoma wierzchołkami
def readPath(u, v, P):
  if P[u][v] == -1:
    return []
  path = [u]
  while u != v:
    u = P[u][v]
    path.append(u)
  return path


G = [
  [inf, 5, 4, 8, inf],
  [-4, inf, -2, inf, 5],
  [inf, inf, inf, 5, 2],
  [-1, 2, inf, inf, -1],
  [inf, inf, 4, 2, inf]
]
algorithm_Floyd_Warshall(G)