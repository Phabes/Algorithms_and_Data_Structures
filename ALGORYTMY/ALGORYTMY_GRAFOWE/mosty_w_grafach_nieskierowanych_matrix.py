# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info
    self.visited = False
    self.timeVisit = None
    self.parent = None
    self.kids = []
    self.backs = []
    self.low = None


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
            v.backs.append(i)
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
      DFSVisit(T, v)
  return T


def bridges(G):
  T = DFS(G)
  bridges = []
  # Znajdujemy wszystkie mosty
  for v in T:
    if v.timeVisit == v.low and v.parent != None:
      bridges.append((v.parent, v.number))
  return bridges


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
G = [
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
]
# G = [
#   [0, 1, 1, 0, 0, 0, 0, 0, 0],
#   [1, 0, 1, 0, 0, 0, 0, 0, 0],
#   [1, 1, 0, 1, 1, 1, 1, 0, 0],
#   [0, 0, 1, 0, 1, 0, 0, 0, 0],
#   [0, 0, 1, 1, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0, 1, 0, 0],
#   [0, 0, 1, 0, 0, 1, 0, 1, 1],
#   [0, 0, 0, 0, 0, 0, 1, 0, 1],
#   [0, 0, 0, 0, 0, 0, 1, 1, 0]
# ]
# G = [
#   [0, 1, 1, 1, 0, 0],
#   [1, 0, 1, 0, 0, 0],
#   [1, 1, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 1],
#   [0, 0, 0, 1, 0, 1],
#   [0, 0, 0, 1, 1, 0]
# ]
print(bridges(G))