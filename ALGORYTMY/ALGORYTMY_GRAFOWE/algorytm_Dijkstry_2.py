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
def algorithm_Dijkstra(G, W):
  n = len(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[0].distance = 0
  q = PriorityQueue()
  # W kolejce będą krotki postaci (dystans od punktu startowego, index)
  q.put((T[0].distance, T[0].number))
  while not q.empty():
    x = q.get()
    # print(x)
    vIndex = x[1]
    # Oznaczamy wierzchołek jako odwiedzony już, żeby nie brać go już później pod uwagę w rozważaniu najkrótszej ścieżki do niego, gdyż została ona już wyznaczona
    T[vIndex].visited = True
    # Sprawdzamy wszystkie wychodzące krawędzie z naszego wierzchołka
    for i in range(len(G[vIndex])):
      uIndex = G[vIndex][i]
      # Sprawdzamy, czy wierzchołek, z którym łączy się nasz pobrany wierzchołek nie był już odwiedzony
      if not T[uIndex].visited:
        weight = W[vIndex][uIndex]
        # Sprawdzamy, czy znaleziono lepszą ścieżkę do wierzchołka u
        if relax(T[uIndex], T[vIndex], weight):
          q.put((weight + x[0], uIndex))
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(n):
    print("Distance from 0 to", i, ":", T[i].distance)
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
  [1, 5],
  [0, 2, 5],
  [1, 3, 4, 5],
  [2, 4],
  [2, 3, 5],
  [0, 1, 2, 4]
]
# W = [(0, 1, 1), (0, 5, 12), (1, 2, 5), (1, 5, 7), (2, 3, 3000), (2, 4, 4), (2, 5, 6), (3, 4, 9), (4, 5, 8)]
W = [
  [0, 1, 0, 0, 0, 12],
  [1, 0, 5, 0, 0, 7],
  [0, 5, 0, 3000, 4, 6],
  [0, 0, 3000, 0, 9, 0],
  [0, 0, 4, 9, 0, 8],
  [12, 7, 6, 0, 8, 0],
]
# G = [
#     [1, 5],
#     [0, 2, 3],
#     [1, 3, 5],
#     [1, 2, 4, 5],
#     [3, 5],
#     [0, 2, 3, 4]
# ]
# W = [
#     [0, 5, 0, 0, 0, 2],
#     [5, 0, 6, 4, 0, 0],
#     [0, 6, 0, 9, 0, 3],
#     [0, 4, 9, 0, 1, 8],
#     [0, 0, 0, 1, 0, 7],
#     [2, 0, 3, 8, 7, 0]
# ]

algorithm_Dijkstra(G, W)