from math import inf, ceil


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.distance = inf
    self.throughput = -inf
    self.visited = False
    self.parent = None


# Algorytm Dijkstry dla postaci macierzowej grafu
def tourGuide(G, s, t, k):
  n = len(G)
  T = [Node(i) for i in range(n)]
  T[s].distance = 0
  T[s].throughput = inf
  # Za każdym razem odwiedzimy jeden wierzchołek, czyli w sumie "n"
  for _ in range(n):
    vIndex = findBiggestThroughput(T)
    if vIndex == t or vIndex == None:
      break
    T[vIndex].visited = True
    for i in range(n):
      weight = G[vIndex][i]
      if weight != 0 and not T[i].visited:
        relax(T[vIndex], T[i], weight)
  return ceil(k / T[t].throughput), getPath(T[t]), T[t].distance


# Znajduje wierzchołek jeszcze nieodwiedzony, o największej przepustowości
def findBiggestThroughput(T):
  n = len(T)
  maxi = -inf
  index = None
  for i in range(n):
    if not T[i].visited and T[i].throughput > maxi:
      maxi = T[i].throughput
      index = i
  return index


# Uaktualnia ścieżkę
def relax(u, v, weightUV):
  mini = min(u.throughput, weightUV)
  if v.throughput < mini:
    v.distance = u.distance + weightUV
    v.throughput = mini
    v.parent = u
    return True
  return False


# Odczytuje ścieżkę od punktu startowego, do punktu docelowego
def getPath(v):
  path = []
  while v != None:
    path.append(v.number)
    v = v.parent
  path.reverse()
  return path


def createGraph(E, n):
  G = [[0] * n for _ in range(n)]
  for edge in E:
    G[edge[0]][edge[1]] = edge[2]
    G[edge[1]][edge[0]] = edge[2]
  return G


# G = [
#   [0, 3, 0, 0, 0, 3, 5],
#   [3, 0, 7, 0, 0, 0, 3],
#   [0, 7, 0, 5, 4, 0, 2],
#   [0, 0, 5, 0, 2, 0, 0],
#   [0, 0, 4, 2, 0, 1, 1],
#   [3, 0, 0, 0, 1, 0, 0],
#   [5, 3, 2, 0, 1, 0, 0]
# ]
# G = [
#   [0, 1, 0, 0, 0, 3, 5, 0],
#   [1, 0, 7, 0, 0, 0, 3, 0],
#   [0, 7, 0, 3, 4, 0, 2, 0],
#   [0, 0, 3, 0, 5, 0, 0, 0],
#   [0, 0, 4, 5, 0, 0, 1, 8],
#   [3, 0, 0, 0, 0, 0, 7, 2],
#   [5, 3, 2, 0, 1, 7, 0, 0],
#   [0, 0, 0, 0, 8, 2, 0, 0]
# ]
# G = [
#   [0, 4, 0, 0, 0, 3, 5, 0],
#   [4, 0, 7, 0, 0, 0, 3, 0],
#   [0, 7, 0, 3, 4, 0, 2, 0],
#   [0, 0, 3, 0, 5, 0, 0, 0],
#   [0, 0, 4, 5, 0, 0, 1, 8],
#   [3, 0, 0, 0, 0, 0, 7, 2],
#   [5, 3, 2, 0, 1, 7, 0, 0],
#   [0, 0, 0, 0, 8, 2, 0, 0]
# ]
G = [(0, 1, 4), (0, 5, 3), (0, 6, 5), (1, 2, 7), (1, 6, 3), (2, 3, 3), (2, 4, 4), (2, 6, 2), (3, 4, 5), (4, 6, 1),
     (4, 7, 8), (5, 6, 7), (5, 7, 2)]
n = 8
s = 0
t = 3
k = 21
print(tourGuide(createGraph(G, n), s, t, k))