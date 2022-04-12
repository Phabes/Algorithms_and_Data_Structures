class Node():
  def __init__(self, number):
    self.number = number
    self.visited = False
    self.timeConvert = -1


# Liczy silnie spójne składowe
def silnieSpojneSkladowe(G):
  # Odwiedzamy wierzchołek
  def DFSVisit(G, T, index):
    nonlocal time, order
    n = len(T)
    T[index].visited = True
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wcześniejszy się łączy
    for i in range(n):
      if G[T[index].number][i] == 1 and not T[i].visited:
        DFSVisit(G, T, i)
    time += 1
    # Zapamiętujemy czas przetworzenia
    T[index].timeConvert = time
    order.append(index)

  n = len(G)
  T = [Node(i) for i in range(n)]
  time = 0
  order = []
  # Wykonujemy pierwszego DFS'a, który oblicza nam czasy przetworzenia wierzchołków
  for i in range(n):
    if not T[i].visited:
      DFSVisit(G, T, i)
  # Odwracamy krawędzie
  reverseEdges(G)
  # Tworzymy kolejność wierzchołków według malejących czasów przetworzenia (musimy odwrócić tablicę)
  order.reverse()
  for i in range(n):
    T[i].visited = False
  time = 0
  count = 0
  # Drugi DFS, według malejących czasów przetworzenia
  for i in range(n):
    index = order[i]
    if not T[index].visited:
      count += 1
      DFSVisit(G, T, index)
  # Przywracamy graf do stanu początkowego
  reverseEdges(G)
  return count


# Odwraca kierunek krawędzi
def reverseEdges(G):
  n = len(G)
  for i in range(n):
    for j in range(i, n):
      tmp = G[i][j]
      G[i][j] = G[j][i]
      G[j][i] = tmp


G = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
]
print(silnieSpojneSkladowe(G))