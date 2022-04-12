# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info[0]
    self.name = info[1]
    self.visited = False
    self.parent = None


# Przeszukiwanie wzdłuż
def DFS(V, E):
  # Odwiedzamy wierzchołek v
  def DFSVisit(T, V, E, v):
    nonlocal time, path
    time += 1
    v.visited = True
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
    for e in E:
      if v.number == e[0] and not T[e[1]].visited:
        T[e[1]].parent = e[0]
        DFSVisit(T, V, E, T[e[1]])
    path = [V[v.number]] + path

  # Tworzymy tablicę naszych wierzchołków
  T = []
  for v in V:
    T.append(Node(v))
  time = 0
  # Tworzymy tablicę posortowanych wierzchołków
  path = []
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      DFSVisit(T, V, E, v)
  # Zwracamy tablicę posortowaną topoligicznie
  return path


def sortowanieTopologiczne(V, E):
  path = DFS(V, E)
  return path


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i")]
E = [(0, 1), (0, 2), (1, 2), (1, 4), (4, 3), (4, 6), (4, 5), (8, 7), (7, 4)]
# G=[V,E]
print(sortowanieTopologiczne(V, E))