from queue import PriorityQueue


class Node():
  def __init__(self, number):
    self.number = number
    self.branch = -1


# Sprawdza dwudzielność grafu spójnego przy pomocy BFS'a
def checkDualityBFS(G, s):
  n = len(G)
  T = [Node(i) for i in range(n)]
  T[s].branch = 0
  q = PriorityQueue()
  q.put(s)
  # Powtarzamy czynności dopóki, jest jeszcze coś w kolejce
  while not q.empty():
    # Pobieramy index z kolejki
    vIndex = q.get()
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz pobrany się łączy
    for i in range(n):
      if G[vIndex][i] == 1:
        # Sprawdzamy, czy wierzchołek nie był odwiedzony
        if T[i].branch == -1:
          T[i].branch = (T[vIndex].branch + 1) % 2
          q.put(i)
        # Sprawdzamy, czy wierzchołki tego samego koloru nie są w tej samej grupie (wtedy nie jest dwudzielny)
        elif T[i].branch == T[vIndex].branch:
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
print(checkDualityBFS(G, s))