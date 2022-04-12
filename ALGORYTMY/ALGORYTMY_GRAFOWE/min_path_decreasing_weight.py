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
def algorithm_Dijkstra(V, E, u, v):
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(V)]
  print(E)
  E.sort(key=lambda edge: edge[2], reverse=True)
  print(E)

  # # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[u].distance = 0
  q = PriorityQueue()
  # W kolejce będą krotki postaci (dystans od punktu startowego, index)
  q.put((T[u].distance, T[u].number))
  while not q.empty():
    x = q.get()
    # print(x)
    vIndex = x[1]
    print(vIndex)
    # Oznaczamy wierzchołek jako odwiedzony już, żeby nie brać go już później pod uwagę w rozważaniu najkrótszej ścieżki do niego, gdyż została ona już wyznaczona
    T[vIndex].visited = True
    # if xIndex==v: # Jeśli interesuje nas tylko ścieżka do wierzchołka v
    #     break
    # Sprawdzamy wszystkie wychodzące krawędzie z naszego wierzchołka
    for edge in E:
      weight = edge[2]
      a = edge[0]
      b = edge[1]
      if a == vIndex:
        # Sprawdzamy, czy istnieje krawędź między wierzchołkami i czy przypadkiem wierzchołek nie był już odwiedzony
        if not T[b].visited and checkDecreasing(T[vIndex], T[b], G):
          # if not T[b].visited:
          # Sprawdzamy, czy znaleziono lepszą ścieżkę do wierzchołka u
          if relax(T[vIndex], T[b], weight):
            q.put((weight + x[0], b))
      if b == vIndex:
        # Sprawdzamy, czy istnieje krawędź między wierzchołkami i czy przypadkiem wierzchołek nie był już odwiedzony
        if not T[b].visited and checkDecreasing(T[vIndex], T[b], G):
          # if not T[a].visited:
          # Sprawdzamy, czy znaleziono lepszą ścieżkę do wierzchołka u
          if relax(T[vIndex], T[a], weight):
            q.put((weight + x[0], a))
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(V):
    print("Distance from 0 to", i, ":", T[i].distance)
    readPath(T[i])
    print()


def checkDecreasing(u, v, G):
  if u.parent == None:
    return True
  if G[u.parent.number][u.number] > G[u.number][v.number]:
    return True
  print(u.parent.number, u.number, v.number)
  return False


# Uaktualnia najkrótszą ścieżkę do punktu v
def relax(u, v, weightUV):
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


# G = [
#   [-1, 1, 5, -1, -1],
#   [1, -1, 2, 8, 7],
#   [5, 2, -1, 3, -1],
#   [-1, 8, 3, -1, 1],
#   [-1, 7, -1, 1, -1]
# ]
# G = [
#   [-1, 1, -1, -1, -1, 12],
#   [1, -1, 5, -1, -1, 7],
#   [-1, 5, -1, 3000, 2, 6],
#   [-1, -1, 3000, -1, 9, -1],
#   [-1, -1, 2, 9, -1, 3],
#   [12, 7, 6, -1, 3, -1]
# ]
G = [
  [-1, 4, -1, -1, -1, -1, -1, 8, -1],
  [4, -1, 8, -1, -1, -1, -1, 11, -1],
  [-1, 8, -1, 7, -1, 4, -1, -1, 2],
  [-1, -1, 7, -1, 9, 14, -1, -1, -1],
  [-1, -1, -1, 9, -1, 10, -1, -1, -1],
  [-1, -1, 4, 14, 10, -1, 2, -1, -1],
  [-1, -1, -1, -1, -1, 2, -1, 1, 6],
  [8, 11, -1, -1, -1, -1, 1, -1, 7],
  [-1, -1, 2, -1, -1, -1, 6, 7, -1]
]
V = 9
E = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9), (3, 5, 14), (4, 5, 10),
     (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]

algorithm_Dijkstra(V, E, 0, 4)