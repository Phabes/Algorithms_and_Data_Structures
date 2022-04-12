from queue import PriorityQueue
from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.wave = -1
    self.visited = False
    self.parent = None


# Znajduje ścieżkę powiększającą w sieci rezydualnej przy użyciu BFS'a
def findExtendingPath(Vertex, R, s, t):
  n = len(Vertex)
  # Przywracamy wszystkie właściwości wierzchołków do stanu początkowego
  for v in Vertex:
    v.wave = -1
    v.visited = False
    v.parent = None
  Vertex[s].visited = True
  Vertex[s].wave = 0
  q = PriorityQueue()
  # W kolejce są elementy w postaci krotek (fala, index wierzchołka)
  q.put((0, s))
  while not q.empty():
    wave, index = q.get()
    # Sprawdzamy, czy znaleźliśmy ścieżkę powiększającą
    if index == t:
      break
    # Wrzucamy wierzchołek do kolejki, jeśli da się puścić przepływ między wierzchołkami i jeśli wierzchołek nie był odwiedzony
    for i in range(n):
      if R[index][i] > 0 and not Vertex[i].visited:
        Vertex[i].visited = True
        Vertex[i].wave = wave + 1
        Vertex[i].parent = Vertex[index]
        q.put((Vertex[i].wave, i))
  x = Vertex[t]
  flow = inf
  # Obliczamy przepływ jaki jesteśmy wstanie puścić tą ścieżką
  while x.parent != None:
    flow = min(flow, R[x.parent.number][x.number])
    x = x.parent
  # Sprawdzamy, czy w ogóle dotarliśmy do wierzchołka docelowego
  if flow == inf:
    return 0
  x = Vertex[t]
  # Uaktualniamy naszą sieć rezydualną
  while x.parent != None:
    R[x.parent.number][x.number] -= flow
    R[x.number][x.parent.number] += flow
    x = x.parent
  return flow


# Oblicza maksymalny przepływ między źródłem, a ujściem
def max_flow_Edmonds_Karp(G, s, t):
  n = len(G)
  # Tworzymy sieć rezydualną
  R = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      R[i][j] = G[i][j]
  Vertex = [Node(i) for i in range(n)]
  flow = 0
  x = findExtendingPath(Vertex, R, s, t)
  while x != 0:
    flow += x
    x = findExtendingPath(Vertex, R, s, t)
  # Tworzymy ostateczny przepływ
  F = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if G[i][j] > 0:
        F[i][j] = G[i][j] - R[i][j]
  return flow


G = [
  [0, 1, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0]
]
s = 0
t = 7
print(max_flow_Edmonds_Karp(G, s, t))
