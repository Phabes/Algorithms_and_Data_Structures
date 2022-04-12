# Założenie: Graf jest spójny na początku programu (można sprawdzić puszczając BFS'a)
# Jeśli najmniejszym stopniem wierzchołka w grafie jest 1, to nie ma problemu, gdyż usunięcie go zawsze pozostawi graf spójny.
# Natomiast jeśli najmniejszy stopień wierzchołka w grafie jest większy od 1, to również nie ma problemu, gdyż jedyną
# sytuacją, w której graf stanie się niespójny jest, gdy usuniemy krawędź do wierzchołka ze stopniem 1, a wiemy że takiego nie ma.
from math import inf


# Czyta krawędzie
def readEdges(V, E):
  n = len(E)
  for i in range(n):
    for j in range(i + 1, n):
      if E[i][j] == 1:
        print(V[i][1], V[j][1])


# Usuwamy wierzchołek z grafu, a co za tym idzie wszystkie wierzchołki z niego wychodzące
def deleteNodes(V, E):
  T = countEdges(E)
  q = []
  index = findMin(T)
  while index != inf:
    print(T)
    print(V[index])
    q.append(V[index])
    deleteEdges(T, E, index)
    index = findMin(T)
  return q


# Usuwa wszystkie krawędzie wychodzące z wierzchołka (index)
def deleteEdges(T, E, index):
  T[index] = 0
  n = len(T)
  for j in range(n):
    if E[index][j] == 1:
      E[index][j] = 0
      E[j][index] = 0
      T[j] -= 1


# Znajduje index, pod którym jest wierzchołek, z którego wychodzi najmniej krawędzi sposród pozostałych
def findMin(T):
  mini = inf
  index = inf
  n = len(T)
  for i in range(n):
    # Sprawdzenie, czy wierzchołek nadal jest w grafie
    if T[i] != 0:
      # Sprawdzenie czy znaleźliśmy lepszego kandydata do usunięcia
      if T[i] < mini:
        mini = T[i]
        index = i
  return index


# Zlicza ile krawędzi wychodzi z każdego wierzchołka (+1 aby ostatni wierzchołek też usunęło)
def countEdges(E):
  n = len(E)
  T = [1] * n
  for i in range(n):
    for j in range(i + 1, n):
      if E[i][j] == 1:
        T[i] += 1
        T[j] += 1
  return T


# def countEdges2(E):
#   n = len(E)
#   T = []
#   for i in range(n):
#     count = 0
#     for j in range(n):
#       if E[i][j] == 1:
#         count += 1
#     T.append(count)
#   return T

V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i"), (9, "j"), (10, "k")]
# E = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (3, 4), (4, 5), (4, 9), (5, 6), (5, 8), (5, 9), (6, 7), (7, 8),
#      (9, 10)]
E = [  # 0  1  2  3  4  5  6  7  8  9  10
  [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 0
  [1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],  # 1
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 3
  [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],  # 4
  [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],  # 5
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 6
  [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],  # 7
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],  # 8
  [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],  # 9
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]  # 10
]
# G=[V,E]
# readEdges(V, E)
print(deleteNodes(V, E))