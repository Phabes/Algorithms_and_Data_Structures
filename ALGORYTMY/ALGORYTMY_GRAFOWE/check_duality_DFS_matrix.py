class Node():
  def __init__(self, number):
    self.number = number
    self.branch = -1


# Sprawdza dwudzielność grafu spójnego przy pomocy DFS'a
def checkDualityDFS(G, s):
  n = len(G)
  T = [Node(i) for i in range(n)]
  T[s].branch = 0
  x = DFSVisit(G, T, s)
  return x


# Odwiedzamy wierzchołek
def DFSVisit(G, T, index):
  n = len(T)
  # Wyszukujemy wszystkie wierzchołki, z którymi nasz wcześniejszy się łączy
  for i in range(n):
    if G[T[index].number][i] == 1:
      # Sprawdzamy, czy wierzchołek nie był odwiedzony
      if T[i].branch == -1:
        T[i].branch = (T[index].branch + 1) % 2
        if not DFSVisit(G, T, i):
          return False
      # Sprawdzamy, czy wierzchołki tego samego koloru nie są w tej samej grupie (wtedy nie jest dwudzielny)
      elif T[i].branch == T[index].branch:
        return False
  return True


G = [
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 1, 1, 0, 1, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 1],
  [0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0]
]
s = 0
print(checkDualityDFS(G, s))