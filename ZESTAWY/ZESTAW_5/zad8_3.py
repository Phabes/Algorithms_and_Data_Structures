from math import inf


def chip(A):
  n = len(A)
  m = len(A[0])
  F = [[inf] * m for _ in range(n)]
  F[0][0] = A[0][0]
  for i in range(n):
    for j in range(m):
      if i > 0:
        F[i][j] = min(F[i][j], F[i - 1][j] + A[i][j])
      if j > 0:
        F[i][j] = min(F[i][j], F[i][j - 1] + A[i][j])
  for line in F:
    print(line)
  return F[n - 1][n - 1]


A = [
  [1, 1, 4, 1, 2],
  [2, 3, 5, 6, 4],
  [4, 1, 7, 8, 5],
  [5, 2, 2, 1, 3]
]
print(chip(A))
