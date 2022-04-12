# f(i,e) - minimalna liczba skoków jakie musi wykonać żaba, aby dotrzeć do punktu "i" mająć "e" energii przed zjedzeniem smakołyka z pola
# f(i,e) = min( f(k, e+(i-k)-A[k] ) + 1
#         0<=k<i
from zad4testy import runtests
from math import inf


# Zwraca minimalną liczbę skoków, jakie musi wykonać żaba
def zbigniew(A):
  n = len(A)
  F = [[inf] * n for _ in range(n)]
  F[0][0] = 0
  for i in range(n):
    f(n - 1, i, F, A)
  for line in F:
    print(line)
  return min(F[n - 1])


def f(i, e, F, A):
  n = len(A)
  if e < 0 or e >= n:
    return inf
  if F[i][e] != inf:
    return F[i][e]
  mini = inf
  for k in range(i):
    energy = e + (i - k) - A[k]
    mini = min(mini, f(k, energy, F, A) + 1)
  F[i][e] = mini
  return F[i][e]


runtests(zbigniew)