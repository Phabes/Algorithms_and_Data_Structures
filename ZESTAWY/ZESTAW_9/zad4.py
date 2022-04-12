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
  T[s].distance = 1
  # W kolejce będą krotki postaci (dystans od punktu startowego, index)
  for _ in range(n):
    vIndex = findShortestNotVisited(T)
    if vIndex==t or vIndex==None:
      break
    T[vIndex].visited = True
    for i in range(n):
      weight = G[vIndex][i]
      if weight != 0 and not T[i].visited:
        relax(T[vIndex],T[i],weight)
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(n):
    print("Distance from", s, " to", i, ":", T[i].distance)
    readPath(T[i])
    print()
  return T[t].distance


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
def relax(u, v, weightUV):
  if v.distance > u.distance * weightUV:
    v.distance = u.distance * weightUV
    v.parent = u
    return True
  return False


# Odczytuje ścieżkę od punktu startowego
def readPath(v):
  if v != None:
    readPath(v.parent)
    print(v.number, " --> ", end="")


# G = [
#   [0, 0, 0, 0, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 0, 0, 0],
#   [1, 1, 0, 0, 1],
#   [0, 0, 0, 0, 0]
# ]
G = [
  [0, 5, 0, 0, 0, 3],
  [5, 0, 0, 2, 0, 0],
  [0, 0, 0, 2, 0, 0],
  [0, 2, 2, 0, 2, 4],
  [0, 0, 0, 2, 0, 10],
  [3, 0, 0, 4, 10, 0],
]
s=0
t=4
print(algorithm_Dijkstra(G, s, t))
