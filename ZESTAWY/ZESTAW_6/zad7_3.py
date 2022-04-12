from math import inf


def forge(T, k):
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
    F[block[0]][block[1]] = 1
  f(mini, maxi - 1, F, T)
  for line in F:
    print(line)
  longest = -inf
  for i in range(maxi):
    for j in range(maxi):
      if F[i][j] <= k:
        length = j - i
        longest = max(longest, length)
  return longest


def f(i, j, F, T):
  # print(i, j, F[i][j])
  for k in range(i + 1, j):
    F[i][j] = min(F[i][j], f(i, k, F, T) + f(k, j, F, T))
  return F[i][j]


k = 3
T = [(0, 2), (4, 6), (6, 8), (2, 3), (3, 4)]
# T = [(0, 2), (4, 6), (6, 8), (2, 3)]
# T = [(0, 2), (4, 6), (6, 8), (2, 3), (3, 4), (8, 11), (10, 12), (12, 14)]
print(forge(T, k))