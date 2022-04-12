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
    # Usuwamy krawędź, po której przyszliśmy
    if v.parent != None:
      if v.parent < v.number:
        E.remove((v.parent, v.number))
      else:
        E.remove((v.number, v.parent))
    nonlocal time, path
    time += 1
    v.visited = True
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
    for e in E:
      if v.number == e[0]:
        T[e[1]].parent = e[0]
        DFSVisit(T, V, E, T[e[1]])
      elif v.number == e[1]:
        T[e[0]].parent = e[1]
        DFSVisit(T, V, E, T[e[0]])
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


# Czyta krawędzie
def readEdges(V, E):
  for e in E:
    print(V[e[0]][1], V[e[1]][1])


# Sprawdza czy jest to rodzaj grafu eulerowskiego
def cyklEulera(V, E):
  T = DFS(V, E)
  n = len(E)
  if n == 0:
    text = "eulerowski"
    if T[0] != T[n - 1]:
      text = "półeulerowski"
    return T, text
  return False


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f")]
# E = [(0, 1), (0, 5), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]
E = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]
# E = [(0, 1), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]
# G=[V,E]
# readEdges(V,E)
print(cyklEulera(V, E))

# Z WYKŁADU
# tablica krawedzi: [[0, 4], [4, 0], [1, 0], [0, 1], [4, 1], [1, 4], [1, 5], [5, 1], [1, 2], [2, 1], [2, 5], [5, 2], [2, 3],
#            [3, 2], [2, 4], [4, 2], [4, 5], [5, 4], [3, 5], [5, 3]]
# macierz: [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1],
#           [0, 1, 1, 1, 1, 0]]
# sasiedztwo: [[4, 1], [0, 4, 5, 2], [1, 5, 3, 4], [2, 5], [0, 1, 2, 5], [1, 2, 4, 3]]