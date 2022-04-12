# f(i) - minimalny koszt dotarcia do "i-tej" stacji, tankując zawsze do pełna
# f(i) = min( f(k)+(S[i]-S[k])*P[i] )
#       0<=k<i
from math import inf


def minCost(S, P, L):
  n = len(S)
  F = [inf] * n
  F[0] = 0
  f(n - 1, F, S, P)
  print(F)
  stationsUsed = readSolution(F, S, P, [], n - 1, L)
  return F[n - 1], stationsUsed


def f(i, F, S, P):
  for k in range(i):
    if S[i] - S[k] <= L:
      F[i] = min(F[i], f(k, F, S, P) + (S[i] - S[k]) * P[i])
  return F[i]


def readSolution(F, S, P, taken, i, L):
  if i == 0:
    return taken
  for k in range(i):
    if S[i] - S[k] <= L and F[i] == F[k] + (S[i] - S[k]) * P[i]:
      return readSolution(F, S, P, taken + [k], k, L)


# S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20, 25]
# P = [0, 4, 3, 2, 3, 3, 5, 4, 2, 4, 0]
# L = 7
S = [0, 1, 2, 3, 4]
P = [0, 4, 5, 4, 0]
L = 2
# S = [0, 1, 9, 15, 16, 17, 27, 28, 30]
# P = [0, 1, 100, 10, 15, 1, 30, 30, 0]
# L = 14
print(minCost(S, P, L))
