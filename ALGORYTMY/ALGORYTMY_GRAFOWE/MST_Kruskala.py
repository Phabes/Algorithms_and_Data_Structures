# Reprezentacja wierzchołka
class Node():  # makeSet
  def __init__(self, val):
    self.val = val
    self.rank = 0
    self.parent = self


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


# Sprawdzenie, czy każdy wierzchołek jest dobrze określony
def checkG(G):
  for i in range(len(G)):
    for j in range(len(G[i])):
      if i not in G[G[i][j]]:
        print(i, G[i][j])


# Sprawdzenie, czy wagi krawędzi są odpowiednio przypisane
def checkW(W):
  n = len(W)
  for i in range(n):
    for j in range(i, n):
      if W[i][j] != W[j][i]:
        print(i, j)


# Algorytm Kruskala
def MST_Kruskal(G, W):
  n = len(G)
  print(W)
  # Sortujemy krawędzie po wagach
  W.sort(key=lambda x: x[2])
  print(W)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  A = []
  for edge in W:
    u, v, w = edge
    x = find(T[u])
    y = find(T[v])
    print(x.val, y.val, edge)
    # Sprawdzamy, czy Au{edge} nie zawiera cyklu
    if x.val != y.val:
      # Łączymy nasze wierzchołki w unię i możemy naszą krawędź dodać do naszego minimalnego drzewa rozpinającego
      union(x, y)
      A.append(edge)
  return A


# G = [
#     [1, 5],
#     [0, 2, 3],
#     [1, 3, 5],
#     [1, 2, 4, 5],
#     [3, 5],
#     [0, 2, 3, 4]
# ]
# W = [(0, 1, 5), (0, 5, 2), (1, 2, 6), (1, 3, 4), (2, 3, 9), (2, 5, 3), (3, 4, 1), (3, 5, 8), (4, 5, 7)]
# W=[
#     [0,5,0,0,0,2],
#     [5,0,6,4,0,0],
#     [0,6,0,9,0,3],
#     [0,4,9,0,1,8],
#     [0,0,0,1,0,7],
#     [2,0,3,8,7,0]
# ]
# W=[
#     [5,2],
#     [5,6,4],
#     [6,9,3],
#     [4,9,1,8],
#     [1,7],
#     [2,3,8,7],
# ]
G = [
  [1, 5],
  [0, 2, 5],
  [1, 3, 4, 5],
  [2, 4],
  [2, 3, 5],
  [0, 1, 2, 4]
]
W = [(0, 1, 1), (0, 5, 12), (1, 2, 5), (1, 5, 7), (2, 3, 3000), (2, 4, 4), (2, 5, 6), (3, 4, 9), (4, 5, 8)]
# checkG(G)
# checkW(W)
print(MST_Kruskal(G, W))