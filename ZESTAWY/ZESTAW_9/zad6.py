from math import inf


# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info
    self.visited = False
    self.parent = None
    self.miniAlicja = inf
    self.path = None
    self.whoStart = None


def DFSVisit(G, vertex, v, s, t):
  if v.number == t:
    changePlanIfNeeded(G, v, s)
    return
  n = len(vertex)
  v.visited = True
  for i in range(n):
    if G[v.number][i] > 0 and not vertex[i].visited:
      vertex[i].parent = v
      DFSVisit(G, vertex, vertex[i], s, t)
  v.visited = False


def twoDrivers(G, s, t):
  n = len(G)
  # Tworzymy tablicę naszych wierzchołków
  vertex = []
  for i in range(n):
    vertex.append(Node(i))
  DFSVisit(G, vertex, vertex[s], s, t)
  return vertex[t].path,vertex[t].whoStart


def changePlanIfNeeded(G, v, s):
  d1, d2 = 0, 0
  count = 0
  path = []
  remeber=v
  while v.parent != None:
    path.append(v.number)
    if count % 2 == 0:
      d1 += G[v.number][v.parent.number]
    else:
      d2 += G[v.number][v.parent.number]
    count += 1
    v = v.parent
  path.append(s)
  path.reverse()
  v=remeber
  mini = min(d1, d2)
  if mini < v.miniAlicja:
    v.miniAlicja = mini
    v.path = path
    if count % 2 == 0:
      if mini == d1:
        v.whoStart = "Bob"
      else:
        v.whoStart = "Alicja"
    else:
      if mini == d1:
        v.whoStart = "Alicja"
      else:
        v.whoStart = "Bob"


# G = [
#   [0, 4, 0, 0, 0, 0, 0, 6],
#   [4, 0, 5, 0, 0, 0, 0, 0],
#   [0, 5, 0, 3, 0, 0, 0, 0],
#   [0, 0, 3, 0, 3, 0, 0, 0],
#   [0, 0, 0, 3, 0, 3, 0, 0],
#   [0, 0, 0, 0, 3, 0, 1, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1],
#   [6, 0, 0, 0, 0, 0, 1, 0]
# ]
G = [
  [0, 4, 0, 0, 0, 0, 0, 0, 1],
  [4, 0, 5, 0, 0, 0, 0, 0, 0],
  [0, 5, 0, 3, 0, 0, 0, 0, 0],
  [0, 0, 3, 0, 3, 0, 0, 0, 0],
  [0, 0, 0, 3, 0, 3, 0, 0, 0],
  [0, 0, 0, 0, 3, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 6],
  [1, 0, 0, 0, 0, 0, 0, 6, 0]
]
s = 0
t = 4
print(twoDrivers(G, s, t))
