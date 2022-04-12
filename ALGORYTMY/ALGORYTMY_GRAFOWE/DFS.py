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
  def DFSVisit(T, E, v):
    nonlocal time
    time += 1
    v.visited = True
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
    for e in E:
      if v.number == e[0] and not T[e[1]].visited:
        T[e[1]].parent = e[0]
        DFSVisit(T, E, T[e[1]])
      elif v.number == e[1] and not T[e[0]].visited:
        T[e[0]].parent = e[1]
        DFSVisit(T, E, T[e[0]])

  # Tworzymy tablicę naszych wierzchołków
  T = []
  for v in V:
    T.append(Node(v))
  time = 0
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      DFSVisit(T, E, v)
  print(time)
  # Wypisujemy skąd trafiliśmy do danego wierzchołka
  for v in T:
    if v.parent == None:
      print(v.name, v.parent)
    else:
      print(v.name, v.parent, T[v.parent].name)


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h")]
E = [(0, 1), (0, 2), (2, 3), (1, 4), (3, 4), (2, 5), (4, 5), (5, 6), (6, 7)]
# G=[V,E]
DFS(V, E)