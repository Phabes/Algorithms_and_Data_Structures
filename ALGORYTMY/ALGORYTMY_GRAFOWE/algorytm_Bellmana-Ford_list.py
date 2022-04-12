from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.distance = inf
    self.parent = None


# Algorytm Bellmana-Forda przy reprezentacji listy krawędzi
def algorithm_Bellman_Ford(V, E):
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(V)]
  # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[0].distance = 0
  # Z każdym kolejnym wykonaniem pętli przynajmniej odległość do jednego wierzchołka zostanie obliczona
  for i in range(V - 1):
    check = False
    # Dla każdej krawędzi wykonujemy relaksację
    for e in E:
      if relax(T[e[0]], T[e[1]], e[2]):
        check = True
    # Sprawdzamy, czy została dokonana jakakolwiek zmiana odległości
    if not check:
      break
  # Sprawdzamy, czy nie występuje ujemny cykl
  for e in E:
    if T[e[1]].distance > T[e[0]].distance + e[2]:
      print("CYKL UJEMNY WYSTĘPUJE")
      return None
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(V):
    print("Distance from 0 to", i, ":", T[i].distance)
    readPath(T[i])
    print()


# Uaktualnie najkrótszą ścieżkę do punktu v
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


V = 6
E = [(0, 1, 5), (1, 3, 3), (1, 4, 9), (2, 0, 3), (2, 1, -4), (3, 4, 3), (3, 5, 2), (4, 2, -1), (4, 5, -5), (5, 0, 9),
     (5, 2, 8)]

algorithm_Bellman_Ford(V, E)