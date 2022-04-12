# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info
    self.visited = False
    self.parent = None


def DFS(G):
  def DFSVisit(G, T, v):
    nonlocal time
    time += 1
    n = len(T)
    v.visited = True
    for i in range(n):
      if G[v.number][i] > 0 and not T[i].visited:
        T[i].parent = v
        DFSVisit(G, T, T[i])

  n = len(G)
  # Tworzymy tablicę naszych wierzchołków
  T = []
  for i in range(n):
    T.append(Node(i))
  time = 0
  for v in T:
    if not v.visited:
      DFSVisit(G, T, v)
  for v in T:
    if v.parent != None:
      print(v.number, v.parent.number)
    else:
      print(v.number)


# G = [
#   [0, 4, 0, 0, 0, 0, 0, 6],
#   [4, 0, 5, 0, 0, 0, 0, 0],
#   [0, 5, 0, 3, 0, 0, 0, 0],
#   [0, 0, 3, 0, 3, 0, 0, 0],
#   [0, 0, 0, 3, 0, 3, 0, 0],
#   [0, 0, 0, 0, 3, 0, 1, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1],
#   [6, 0, 0, 0, 0, 0, 1, 0]
# ]
G = [
  [0, 4, 0, 0, 0, 0, 0, 0, 1],
  [4, 0, 5, 0, 0, 0, 0, 0, 0],
  [0, 5, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 3, 0, 3, 0, 0, 0, 0],
  [0, 0, 0, 3, 0, 3, 0, 0, 0],
  [0, 0, 0, 0, 3, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 6],
  [1, 0, 0, 0, 0, 0, 0, 6, 0]
]
DFS(G)