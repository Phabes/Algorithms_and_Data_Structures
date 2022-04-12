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
  vertexes = []
  for v in range(n):
    vertexes.append(Node(v))
  # "Kamień" wrzucamy do wierzchołka o indexie s, któy wstawiamy do kolejki
  vertexes[s].visited = True
  vertexes[s].wave = 0
  q = PriorityQueue()
  q.put(s)
  # Powtarzamy czynności dopóki, jest jeszcze coś w kolejce
  while not q.empty():
    # Pobieramy index z kolejki
    index = q.get()
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i wstawiamy je do kolejki
    for i in range(n):
      if G[index][i] == 1 and not vertexes[i].visited:
        update(vertexes, q, index, i)
  # Wypisujemy, w której fali każdy punkt został osiągnięty
  for v in vertexes:
    print(v.number, v.wave)


# Uaktualnia informacje na temat wierzchołka oraz wstawia jego index do kolejki
def update(vertexes, q, index, coord):
  vertexes[coord].visited = True
  vertexes[coord].parent = index
  vertexes[coord].wave = vertexes[index].wave + 1
  q.put(coord)


# G = [
#   [0, 0, 0, 0, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0],
#   [1, 1, 0, 0, 1],
#   [0, 0, 0, 0, 0]
# ]
G = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0]
]
s = 3
print(BFS(G, s))
