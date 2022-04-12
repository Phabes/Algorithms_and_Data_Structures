# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, number):
    self.number = number
    self.visited = False
    self.parent = None


# Przeszukiwanie wzdłuż
def DFS(G):
  # Odwiedzamy wierzchołek v
  def DFSVisit(T, G, v):
    nonlocal time, path
    time += 1
    v.visited = True
    for i in range(n):
      if G[v.number][i] == 1 and not T[i].visited:
        DFSVisit(T, G, T[i])
    path = [v.number] + path

  n = len(G)
  # Tworzymy tablicę naszych wierzchołków
  T = [Node(i) for i in range(n)]
  time = 0
  # Tworzymy tablicę posortowanych wierzchołków
  path = []
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      DFSVisit(T, G, v)
  # Zwracamy tablicę posortowaną topoligicznie
  return path


def sortowanieTopologiczne(G):
  path = DFS(G)
  return path


G = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 1, 0, 0],
]
print(sortowanieTopologiczne(G))