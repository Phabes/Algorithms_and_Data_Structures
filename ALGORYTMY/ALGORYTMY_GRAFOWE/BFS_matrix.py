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
  T = []
  for v in range(n):
    T.append(Node(v))
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
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i wstawiamy je do kolejki
    for i in range(n):
      if G[vIndex][i] == 1 and not T[i].visited:
        update(T, q, vIndex, i)
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
#   [0, 1, 1, 0, 0, 0, 0, 0, 0],
#   [1, 0, 0, 0, 1, 0, 0, 0, 0],
#   [1, 0, 0, 1, 0, 1, 0, 0, 0],
#   [0, 0, 1, 0, 1, 0, 0, 0, 0],
#   [0, 1, 0, 1, 0, 1, 0, 0, 0],
#   [0, 0, 1, 0, 1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 1, 0, 1, 0],
#   [0, 0, 0, 0, 0, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
G = [
  [0, 1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 1],
  [1, 0, 0, 0, 0, 1],
  [0, 0, 0, 1, 1, 0],
]
s = 0
BFS(G, s)