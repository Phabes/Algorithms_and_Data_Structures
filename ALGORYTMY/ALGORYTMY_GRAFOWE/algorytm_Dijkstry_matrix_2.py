from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.distance = inf
    self.visited = False
    self.parent = None


# Algorytm Dijkstry dla postaci macierzowej grafu
def algorithm_Dijkstra(G, s, t):
  n = len(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[s].distance = 0
  # Za każdym razem odwiedzimy jeden wierzchołek, czyli w sumie "n"
  vIndex = findShortestNotVisited(T)
  while vIndex != t and vIndex != None:
    T[vIndex].visited = True
    for i in range(n):
      weight = G[vIndex][i]
      if weight != -1 and not T[i].visited:
        relax(T[i], T[vIndex], weight)
    vIndex = findShortestNotVisited(T)
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(n):
    print("Distance from", s, " to", i, ":", T[i].distance)
    readPath(T[i])
    print()


def findShortestNotVisited(T):
  n = len(T)
  mini = inf
  index = None
  for i in range(n):
    if not T[i].visited and T[i].distance < mini:
      mini = T[i].distance
      index = i
  return index


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