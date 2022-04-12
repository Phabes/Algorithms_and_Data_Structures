# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info[0]
    self.name = info[1]
    self.visited = False
    self.timeVisit = None
    self.parent = None
    self.kids = []
    self.backs = []
    self.low = None


# Przeszukiwanie wzdłuż
def DFS(V, E):
  # Odwiedzamy wierzchołek v
  def DFSVisit(T, E, v):
    nonlocal time
    time += 1
    v.visited = True
    v.timeVisit = time
    v.low = time
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
    for e in E:
      if v.number == e[0]:
        if not T[e[1]].visited:
          T[e[1]].parent = e[0]
          v.kids.append(e[1])
          DFSVisit(T, E, T[e[1]])
        else:
          if e[1] != v.parent and v.timeVisit > T[e[1]].timeVisit:
            v.backs.append(e[1])
      elif v.number == e[1]:
        if not T[e[0]].visited:
          T[e[0]].parent = e[1]
          v.kids.append(e[0])
          DFSVisit(T, E, T[e[0]])
        else:
          if e[0] != v.parent and v.timeVisit > T[e[0]].timeVisit:
            v.backs.append(e[0])
    for back in v.backs:
      v.low = min(v.low, T[back].timeVisit)
    for kid in v.kids:
      v.low = min(v.low, T[kid].low)

  # Tworzymy tablicę naszych wierzchołków
  T = [Node(v) for v in V]
  time = 0
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      DFSVisit(T, E, v)
  return T


# Czyta krawędzie
def readEdges(V, E):
  for e in E:
    print(V[e[0]][1], V[e[1]][1])


def bridges(V, E):
  T = DFS(V, E)
  bridges = []
  # Znajdujemy wszystkie mosty
  for v in T:
    if v.timeVisit == v.low and v.parent != None:
      bridges.append((v.parent, v.number))
  return bridges


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h")]
E = [(0, 1), (0, 4), (1, 2), (2, 3), (2, 4), (3, 6), (3, 5), (4, 7), (5, 6)]
# G=[V,E]
# readEdges(V,E)
# DFS(V, E)
print(bridges(V, E))