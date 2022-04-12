from math import inf, ceil


class Node():  # makeSet
  def __init__(self, val):
    self.val = val  # zastępuje self.number = number
    self.rank = 0
    self.parent = self
    self.distance = inf
    self.throughput = -inf
    self.visited = False


def find(x):  # find
  if x != x.parent:
    x.parent = find(x.parent)
  return x.parent


def union(x, y):  # union
  x = find(x)
  y = find(y)
  if x == y:
    return
  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1


# Algorytm Kruskala, który znajduje MAKSYMALNE drzewo rozpinające
def MST_Kruskal(G, n):
  print(G)
  # Sortujemy krawędzie po wagach
  G.sort(key=lambda x: x[2], reverse=True)
  print(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  A = []
  for edge in G:
    x = find(T[edge[0]])
    y = find(T[edge[1]])
    # print(x.val, y.val, edge)
    # Sprawdzamy, czy Au{edge} nie zawiera cyklu
    if x.val != y.val:
      # Łączymy nasze wierzchołki w unię i możemy naszą krawędź dodać do naszego minimalnego drzewa rozpinającego
      union(x, y)
      A.append(edge)
  return A


def tourGuide(G, n, s, t, k):
  vertexes = [Node(i) for i in range(n)]
  E = MST_Kruskal(G, n)
  for v in vertexes:
    v.parent = None
  # Tworzymy tablicę naszych wierzchołków
  vertexes[s].distance = 0
  vertexes[s].throughput = inf
  DFSVisit(vertexes, E, vertexes[s])
  return ceil(k / vertexes[t].throughput), getPath(vertexes[t]), vertexes[t].distance


def DFSVisit(vertexes, E, v):
  v.visited = True
  # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i je odwiedzamy
  for e in E:
    if v.val == e[0] and not vertexes[e[1]].visited:
      vertexes[e[1]].parent = vertexes[e[0]]
      vertexes[e[1]].distance = v.distance + e[2]
      vertexes[e[1]].throughput = min(v.throughput, e[2])
      DFSVisit(vertexes, E, vertexes[e[1]])
    elif v.val == e[1] and not vertexes[e[0]].visited:
      vertexes[e[0]].parent = vertexes[e[1]]
      vertexes[e[0]].distance = v.distance + e[2]
      vertexes[e[0]].throughput = min(v.throughput, e[2])
      DFSVisit(vertexes, E, vertexes[e[0]])


def getPath(v):
  path = []
  while v != None:
    path.append(v.val)
    v = v.parent
  path.reverse()
  return path


G = [(0, 1, 1), (0, 5, 3), (0, 6, 5), (1, 2, 7), (1, 6, 3), (2, 3, 3), (2, 4, 4), (2, 6, 2), (3, 4, 5), (4, 6, 1),
     (4, 7, 8), (5, 6, 7), (5, 7, 2)]
n = 8
s = 0
t = 3
k = 21
print(tourGuide(G, n, s, t, k))