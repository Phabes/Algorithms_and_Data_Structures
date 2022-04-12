# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info[0]
    self.name = info[1]
    self.visited = False
    self.timeProcessing = None
    self.componentIndex = None


# Przeszukiwanie wzdłuż
def DFS(V, E):
  # Tworzymy tablicę naszych wierzchołków
  T = []
  for v in V:
    T.append(Node(v))
  time = 0
  # Odwiedzamy każdy wierzchołek
  for v in T:
    if not v.visited:
      time = DFSVisit(T, E, v, 0, time)
  return T


# Odwiedzamy wierzchołek v
def DFSVisit(T, E, v, componentIndex, time):
  # Oznaczamy wierzchołek oraz do jakiej silnej składowej należy
  v.visited = True
  v.componentIndex = componentIndex
  # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
  for e in E:
    if v.number == e[0] and not T[e[1]].visited:
      time = DFSVisit(T, E, T[e[1]], componentIndex, time)
  time += 1
  v.timeProcessing = time
  return time


# Znajduje index wierzchołka, który ma największy czas przetworzenia sposród wszystkich wierzchołków nieodwiedzonych po raz drugi
def findBiggest(T):
  biggest = 0
  n = len(T)
  for i in range(1, n):
    if not T[i].visited and T[biggest].timeProcessing < T[i].timeProcessing:
      biggest = i
  if biggest == 0 and T[0].visited:
    return -1
  return biggest


# Czyta krawędzie
def readEdges(V, E):
  for e in E:
    print(V[e[0]][1], V[e[1]][1])


# Odwraca krawędzie
def turnEdges(E):
  for i in range(len(E)):
    E[i] = (E[i][1], E[i][0])


def silnieSpojneSkladowe(V, E):
  T = DFS(V, E)
  turnEdges(E)
  # readEdges(V, E)
  for v in T:
    v.visited = False
  # summits.sort(key=lambda summit:summit.timePrecessing, reverse=True) # można posortować po czasie przetworzenia, ale później należałoby zmienić indexy w tablicy krawędzi (E)
  count = 1
  time = 0
  # Odwiedzamy każdy wierzchołek, zawsze wyszukując największy czas przetworzenia, który nie został jeszcze odwiedzony po raz drugi
  index = findBiggest(T)
  while index != -1:
    time = DFSVisit(T, E, T[index], count, time)
    index = findBiggest(T)
    count += 1
  # Wypisujemy do jakiej silnie składowej należy każdy z wierzchołków
  for v in T:
    print(v.name, v.componentIndex)


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i"), (9, "j"), (10, "k")]
E = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 0), (2, 7), (3, 4), (4, 5), (5, 3), (5, 6), (6, 3), (7, 9), (8, 6), (8, 7),
     (9, 10), (10, 8)]
# E = [(0, 1), (0, 4), (1, 2), (1, 3), (2, 0), (2, 7), (3, 4), (4, 5), (5, 3), (6,5), (3,6), (7, 9), (8, 6), (8, 7),
#      (9, 10), (10, 8)]
# G=[V,E]
# readEdges(V, E)
silnieSpojneSkladowe(V, E)