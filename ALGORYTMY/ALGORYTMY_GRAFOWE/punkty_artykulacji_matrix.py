from math import inf


# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info
    self.visited = False
    self.timeVisit = inf  # None
    self.parent = None
    self.kids = []
    self.backs = []
    self.low = None
    self.startingPoint = False


# Przeszukiwanie wzdłuż
def DFS(G):
  n = len(G)

  # Odwiedzamy wierzchołek v
  def DFSVisit(T, v):
    nonlocal time
    time += 1
    v.visited = True
    v.timeVisit = time
    v.low = time
    for i in range(n):
      if G[v.number][i] == 1:
        if not T[i].visited:
          T[i].parent = v.number
          v.kids.append(i)
          DFSVisit(T, T[i])
        else:
          if i != v.parent and v.timeVisit > T[i].timeVisit:
            # v.low = min(v.low, T[i].timeVisit) # można tu tutaj obliczyć low, z krawędzi wstecznych
            v.backs.append(i)
    # Obliczamy parametr low
    for back in v.backs:
      v.low = min(v.low, T[back].timeVisit)
    for kid in v.kids:
      v.low = min(v.low, T[kid].low)

  # Tworzymy tablicę naszych wierzchołków
  T = [Node(i) for i in range(n)]
  time = 0
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      v.startingPoint = True
      DFSVisit(T, v)
  return T


def articulationPoints(G):
  T = DFS(G)
  points = []
  # Znajdujemy wszystkie punkty artykulacji
  for v in T:
    print(v.number, v.timeVisit, v.low, v.kids, v.backs)
    if v.startingPoint:
      if len(v.kids) > 1:
        points.append(v.number)
    else:
      for kid in v.kids:
        if T[kid].low >= v.timeVisit:
          points.append(v.number)
          break
  return points


# G = [
#   [0, 1, 0, 0, 1, 0, 0, 0],
#   [1, 0, 1, 0, 0, 0, 0, 0],
#   [0, 1, 0, 1, 1, 0, 0, 0],
#   [0, 0, 1, 0, 0, 1, 1, 0],
#   [1, 0, 1, 0, 0, 0, 0, 1],
#   [0, 0, 0, 1, 0, 0, 1, 0],
#   [0, 0, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0, 0]
# ]
# G = [
#   [0, 1, 1, 1, 1],
#   [1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0],
# ]
# G = [
#   [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#   [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
# ]
G = [
  [0, 1, 1, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 1, 1, 1, 1, 0, 0],
  [0, 0, 1, 0, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 1, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 1, 1, 0]
]
# G = [
#   [0, 1, 1, 1, 0, 0],
#   [1, 0, 1, 0, 0, 0],
#   [1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1],
#   [0, 0, 0, 1, 0, 1],
#   [0, 0, 0, 1, 1, 0]
# ]
print(articulationPoints(G))