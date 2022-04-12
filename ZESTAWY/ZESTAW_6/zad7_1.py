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
  F = [[False] * maxi for _ in range(maxi)]
  for block in T:
    F[block[0]][block[1]] = True
  f(a, b, F, T)
  for line in F:
    print(line)
  return F[a][b]


def f(i, j, F, T):
  # print(i, j, F[i][j])
  if F[i][j]:
    return True
  for k in range(i + 1, j):
    if f(i, k, F, T) and f(k, j, F, T):
      F[i][j] = True
  return F[i][j]


a = 6
b = 11
# T = [(0, 2), (4, 6), (6, 8), (2, 3), (3, 4)]
# T = [(0, 2), (4, 6), (6, 8), (2, 3)]
# T = [(0, 2), (4, 6), (6, 8), (2, 3), (8, 11), (10, 12), (12, 14)]
T = [(0, 2), (4, 6), (6, 8), (2, 3), (3, 4), (8, 11), (10, 12), (12, 14)]
print(forge(T, a, b))