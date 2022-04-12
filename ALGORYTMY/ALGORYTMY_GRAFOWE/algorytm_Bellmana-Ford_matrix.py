from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.distance = inf
    self.parent = None


# Algorytm Bellmana-Forda przy reprezentacji macierzowej
def algorithm_Bellman_Ford(G):
  n = len(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  # Ustalamy, że dystans od naszego punktu startowego do samego siebie jest równy 0
  T[0].distance = 0
  # Z każdym kolejnym wykonaniem pętli przynajmniej odległość do jednego wierzchołka zostanie obliczona
  for i in range(n - 1):
    check = False
    # Szukamy krawędzi w grafie
    for u in range(n):
      for v in range(n):
        if G[u][v] != inf:
          if (relax(T[u], T[v], G[u][v])):
            check = True
    # Sprawdzamy, czy została dokonana jakakolwiek zmiana odległości
    if not check:
      break
  # Sprawdzamy, czy nie występuje ujemny cykl
  for u in range(n):
    for v in range(n):
      if G[u][v] != inf:
        if T[v].distance > T[u].distance + G[u][v]:
          print("CYKL UJEMNY WYSTĘPUJE")
          return None
  # Czytamy najkrótsze ścieżki dla naszych wierzchołków od punktu startowego
  for i in range(n):
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


G = [
  [inf, 5, inf, inf, inf, inf],
  [inf, inf, inf, 3, 9, inf],
  [3, -4, inf, inf, inf, inf],
  [inf, inf, inf, inf, 3, 2],
  [inf, inf, -1, inf, inf, -5],
  [9, inf, 8, inf, inf, inf]
]

algorithm_Bellman_Ford(G)