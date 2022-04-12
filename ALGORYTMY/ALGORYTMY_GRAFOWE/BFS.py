from queue import PriorityQueue


# Reprezentacja wierzchołka grafu
class Node():
  def __init__(self, info):
    self.number = info[0]
    self.name = info[1]
    self.visited = False
    self.parent = None
    self.wave = -1


# Przeszukiwanie wszerz
def BFS(V, E, s):
  # Tworzymy tablicę naszych wierzchołków
  T = []
  for v in V:
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
    for e in E:
      if vIndex == e[0] and not T[e[1]].visited:
        update(T, q, vIndex, e[1])
      elif vIndex == e[1] and not T[e[0]].visited:
        update(T, q, vIndex, e[0])
  # Wypisujemy, w której fali każdy punkt został osiągnięty
  for v in T:
    print(v.name, v.wave)


# Uaktualnia informacje na temat wierzchołka oraz wstawia jego index do kolejki
def update(T, q, index, coord):
  T[coord].visited = True
  T[coord].parent = index
  T[coord].wave = T[index].wave + 1
  q.put((T[coord].wave, coord))


V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i")]
E = [(0, 1), (0, 2), (2, 3), (1, 4), (3, 4), (2, 5), (4, 5), (5, 6), (6, 7)]
# G=[V,E]
s = 0
BFS(V, E, s)