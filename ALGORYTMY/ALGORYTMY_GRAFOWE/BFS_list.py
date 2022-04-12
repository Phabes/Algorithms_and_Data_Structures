from queue import PriorityQueue


# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info
    self.visited = False
    self.parent = None
    self.wave = -1


# Przeszukiwanie wszerz
def BFS(G, s):
  n = len(G)
  # Tworzymy tablicę naszych wierzchołków
  T = [Node(v) for v in range(n)]
  # "Kamień" wrzucamy do wierzchołka o indexie s, któy wstawiamy do kolejki
  T[s].visited = True
  T[s].wave = 0
  q = PriorityQueue()
  q.put((0, s))
  # Powtarzamy czynności dopóki, jest jeszcze coś w kolejce
  while not q.empty():
    # Pobieramy index z kolejki
    x = q.get()
    wave, vIndex = x
    n = len(G[vIndex])
    # Sprawdzamy wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i wstawiamy je do kolejki
    for i in range(n):
      x = G[vIndex][i]
      if not T[x].visited:
        update(T, q, vIndex, x)
  # Wypisujemy, w której fali każdy punkt został osiągnięty
  for v in T:
    print(v.number, v.wave)


# Uaktualnia informacje na temat wierzchołka oraz wstawia jego index do kolejki
def update(T, q, index, coord):
  T[coord].visited = True
  T[coord].parent = index
  T[coord].wave = T[index].wave + 1
  q.put((T[coord].wave, coord))


# G = [
#   [2],
#   [2],
#   [0, 1, 3],
#   [2, 4],
#   [3, 5, 6],
#   [4],
#   [4]
# ]
G = [
  [1, 4],
  [0, 2],
  [1, 3],
  [2, 5],
  [0, 5],
  [4, 3]
]
s = 0
BFS(G, s)