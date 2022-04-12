from queue import PriorityQueue
from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.distance = inf
    self.visited = False
    self.parent = None


# Algorytm Dijkstry
def algorithm_Dijkstra(G, s, t):
  n = len(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[s].distance = 0
  q = PriorityQueue()
  # W kolejce będą krotki postaci (dystans od punktu startowego, index)
  q.put((T[s].distance, T[s].number))
  while not q.empty():
    x = q.get()
    # print(x)
    vIndex = x[1]
    # if xIndex==t:
    #     break
    # Oznaczamy wierzchołek jako odwiedzony już, żeby nie brać go już później pod uwagę w rozważaniu najkrótszej ścieżki do niego, gdyż została ona już wyznaczona
    T[vIndex].visited = True
    # Sprawdzamy wszystkie wychodzące krawędzie z naszego wierzchołka
    for i in range(n):
      weight = G[vIndex][i]
      # Sprawdzamy, czy istnieje krawędź między wierzchołkami i czy przypadkiem wierzchołek nie był już odwiedzony
      if weight != -1 and not T[i].visited:
        # Sprawdzamy, czy znaleziono lepszą ścieżkę do wierzchołka u
        if relax(T[i], T[vIndex], weight):
          q.put((weight + x[0], i))
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(n):
    print("Distance from", s, " to", i, ":", T[i].distance)
    readPath(T[i])
    print()


# Uaktualnia najkrótszą ścieżkę do punktu v
def relax(v, u, weightUV):
  if v.distance > u.distance + weightUV:
    v.distance = u.distance + weightUV
    v.parent = u
    return True
  return False


# Odczytuje ścieżkę od punktu startowego
def readPath(v):
  if v != None:
    readPath(v.parent)
    print(v.number, " --> ", end="")


G = [
  [-1, 1, 5, -1, -1],
  [1, -1, 2, 8, 7],
  [5, 2, -1, 3, -1],
  [-1, 8, 3, -1, 1],
  [-1, 7, -1, 1, -1]
]
# G = [
#     [-1, 1, -1, -1, -1, 12],
#     [1, -1, 5, -1, -1, 7],
#     [-1, 5, -1, 3000, 4, 6],
#     [-1, -1, 3000, -1, 9, -1],
#     [-1, -1, 4, 9, -1, 8],
#     [12, 7, 6, -1, 8, -1]
# ]


s = 0
t = 4
algorithm_Dijkstra(G, s, t)
