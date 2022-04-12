class Node():
  def __init__(self, number):
    self.number = number
    self.visited = False
    self.timeConvert = -1


# Liczy silnie spójne składowe
def silnieSpojneSkladowe(G):
  # Odwiedzamy wierzchołek
  def DFSVisit(G, vertexes, index):
    nonlocal time
    n = len(vertexes)
    vertexes[index].visited = True
    # Wyszukujemy wszystkie wierzchołki, z którymi nasz wcześniejszy się łączy
    for i in range(n):
      if G[vertexes[index].number][i] == 1 and not vertexes[i].visited:
        DFSVisit(G, vertexes, i)
    time += 1
    # Zapamiętujemy czas przetworzenia
    vertexes[index].timeConvert = time

  n = len(G)
  vertexes = [Node(i) for i in range(n)]
  time = 0
  # Wykonujemy pierwszego DFS'a, który oblicza nam czasy przetworzenia wierzchołków
  for i in range(n):
    if not vertexes[i].visited:
      DFSVisit(G, vertexes, i)
  # Odwracamy krawędzie
  reverseEdges(G)
  # Tworzymy kolejność wierzchołków według malejących czasów przetworzenia
  order = [(v.number, v.timeConvert) for v in vertexes]
  order.sort(key=lambda vertex: vertex[1], reverse=True)
  for i in range(n):
    vertexes[i].visited = False
  time = 0
  count = 0
  # Drugi DFS, według malejących czasów przetworzenia
  for i in range(n):
    index = order[i][0]
    if not vertexes[index].visited:
      count += 1
      DFSVisit(G, vertexes, index)
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