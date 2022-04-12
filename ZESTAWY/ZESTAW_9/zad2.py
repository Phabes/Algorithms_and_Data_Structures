class Node():
  def __init__(self, number):
    self.number = number
    self.visited = False


def DFSVisit(G, vertexes, v):
  n = len(vertexes)
  v.visited = True
  for i in range(n):
    if G[v.number][i] > 0 and not vertexes[i].visited:
      DFSVisit(G, vertexes, vertexes[i])


def goodStart(G):
  n = len(G)
  vertexes = [Node(i) for i in range(n)]
  for i in range(n):
    DFSVisit(G, vertexes, vertexes[i])
    check=True
    for v in vertexes:
      if not v.visited:
        check=False
      v.visited = False
    if check:
      return i
  return None


G = [
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [1, 1, 0, 0, 1],
  [0, 0, 0, 0, 0]
]
# G = [
#   [0, 0, 0, 0, 0],
#   [1, 0, 0, 0, 0],
#   [0, 0, 0, 0, 1],
#   [1, 1, 0, 0, 1],
#   [0, 0, 0, 0, 0]
# ]
print(goodStart(G))
