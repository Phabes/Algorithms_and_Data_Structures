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
    n = len(G[v.number])
    v.visited = True
    for i in range(n):
      vIndex = G[v.number][i]
      if not T[vIndex].visited:
        T[vIndex].parent = v
        DFSVisit(G, T, T[vIndex])

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


G = [
  [2],
  [2],
  [0, 1, 3],
  [2, 4],
  [3, 5, 6],
  [4],
  [4]
]
DFS(G)