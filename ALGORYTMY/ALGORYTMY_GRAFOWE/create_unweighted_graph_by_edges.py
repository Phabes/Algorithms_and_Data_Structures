def create(E, n):
  G = [[0] * n for _ in range(n)]
  for edge in E:
    G[edge[0]][edge[1]] = 1
    G[edge[1]][edge[0]] = 1
  for line in G:
    print(line)


n = 8
E = [(0, 1), (0, 4), (1, 2), (2, 3), (2, 4), (3, 6), (3, 5), (4, 7), (5, 6)]
create(E, n)