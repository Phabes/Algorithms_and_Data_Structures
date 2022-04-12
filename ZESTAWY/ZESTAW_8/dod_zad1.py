from queue import PriorityQueue
from math import inf


# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, i, j, depth):
    self.i = i
    self.j = j
    self.depth = depth
    self.visited = False
    self.parent = None
    self.wave = -1


def captain(M, T):
  y = len(M)
  x = len(M[0])
  G = createGraph(M, T)
  return BFS(G, T, 0, 0, y - 1, x - 1)


def createGraph(M, T):
  y = len(M)
  x = len(M[0])
  G = [[Node(i, j, M[i][j]) for j in range(x)] for i in range(y)]
  return G


def BFS(G, T, sY, sX, tY, tX):
  y = len(G)
  x = len(G[0])
  G[sY][sX].visited = True
  G[sY][sX].wave = 0
  q = PriorityQueue()
  q.put((0, sY, sX))
  while not q.empty():
    waveNum, i, j = q.get()
    if i == tY and j == tX:
      return True
    if i - 1 >= 0 and not G[i - 1][j].visited and G[i - 1][j].depth > T:
      update(q, G[i][j], G[i - 1][j])
    if i + 1 < y and not G[i + 1][j].visited and G[i + 1][j].depth > T:
      update(q, G[i][j], G[i + 1][j])
    if j - 1 >= 0 and not G[i][j - 1].visited and G[i][j - 1].depth > T:
      update(q, G[i][j], G[i][j - 1])
    if j + 1 < x and not G[i][j + 1].visited and G[i][j + 1].depth > T:
      update(q, G[i][j], G[i][j + 1])
  return False


# Uaktualnia informacje na temat wierzchołka oraz wstawia jego index do kolejki
def update(q, oldV, newV):
  newV.visited = True
  newV.parent = (oldV.i, oldV.j)
  newV.wave = oldV.wave + 1
  q.put((newV.wave, newV.i, newV.j))


M = [
  [inf, 2, 8, 5, 6, 2],
  [6, 4, 7, 9, 3, 2],
  [6, 8, 6, 6, 2, 4],
  [4, 6, 7, 4, 7, inf]
]
T = 3
print(captain(M, T))
