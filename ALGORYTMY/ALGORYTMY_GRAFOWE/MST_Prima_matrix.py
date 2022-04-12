from queue import PriorityQueue
from math import inf


# Reprezentacja wierzchołka
class Node():
  def __init__(self, number):
    self.number = number
    self.weight = inf
    self.visited = False
    self.parent = None


# Algorytm Prima
def MST_Prime(G):
  n = len(G)
  # Tworzymy tablicę reprezentującą nasze wierzchołki
  T = [Node(i) for i in range(n)]
  # Zmieniamy wagę naszego pierwszego wierzchołka na 0 i wrzucamy go do kolejki
  T[0].weight = 0
  # W kolejce będą krotki postaci (waga, index)
  q = PriorityQueue()
  q.put((T[0].weight, T[0].number))
  # Dopóki kolejka priorytetowa nie jest pusta, to ściagamy wierzchołek o najmniejszej wadze
  while not q.empty():
    x = q.get()
    print(x)
    vIndex = x[1]
    # Oznaczamy wierzchołek jako odwiedzony już, żeby nie brać go już później pod uwagę w minimalnym drzewie rozpinającym
    T[vIndex].visited = True
    # Sprawdzamy wszystkie wychodzące krawędzie z naszego wierzchołka
    for i in range(n):
      # uIndex = G[vIndex][i]
      uIndex = i
      weight = G[vIndex][uIndex]
      # Sprawdzamy, czy wierzchołek, z którym łączy się nasz pobrany wierzchołek nie był już odwiedzony
      if weight != 0 and not T[uIndex].visited:
        # Sprawdzamy, czy waga tej krawędzi jest mniejsza od aktualnie najniższej wagi wierzchołka
        if weight < T[uIndex].weight:
          T[uIndex].weight = weight
          T[uIndex].parent = T[vIndex]
          # T[uIndex].parent = vIndex # Wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
          q.put((weight, uIndex))
  A = []
  # Tworzymy tablicę naszych krawędzi minimalnego drzewa rozpinającego
  for i in range(n):
    if T[i].parent != None:
      x = [T[i].parent.number, i]
      # x = [T[i].parent, i] # Gdy jest wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
      x.sort()
      A.append((x[0], x[1], G[i][T[i].parent.number]))
      # A.append((x[0], x[1], W[i][T[i].parent])) # Gdy jest wskazanie tylko na index, pod którym jest wierzchołek, a nie na wierzchołek
  return A


G = [
  [0, 5, 0, 0, 0, 3, 0],
  [5, 0, 0, 0, 0, 2, 0],
  [0, 0, 0, 3, 0, 4, 3],
  [0, 0, 3, 0, 5, 1, 0],
  [0, 0, 0, 5, 0, 5, 0],
  [3, 2, 4, 1, 5, 0, 9],
  [0, 0, 3, 0, 0, 9, 0]
]

print(MST_Prime(G))