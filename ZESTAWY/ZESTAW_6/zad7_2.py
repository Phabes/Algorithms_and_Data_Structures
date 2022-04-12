from math import inf


def forge(T, a, b):
  mini = inf
  maxi = -inf
  for block in T:
    if block[0] < mini:
      mini = block[0]
    if block[1] > maxi:
      maxi = block[1]
  maxi += 1
  F = [[inf] * maxi for _ in range(maxi)]
  for block in T:
    F[block[0]][block[1]] = min(F[block[0]][block[1]], block[2])
  f(a, b, F, T)
  for line in F:
    print(line)
  return F[a][b]


def f(i, j, F, T):
  # print(i, j, F[i][j])
  for k in range(i + 1, j):
    F[i][j] = min(F[i][j], f(i, k, F, T) + f(k, j, F, T))
  return F[i][j]


a = 0
b = 5
# T = [(0, 3, 2), (3, 5, 8), (0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)]
T = [(0, 3, 4), (3, 5, 8), (0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)]
# T = [(0, 3, 1), (3, 5, 1), (0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1)]
print(forge(T, a, b))