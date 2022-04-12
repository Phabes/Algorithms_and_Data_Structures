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
  for i in range(1, n):
    for e in range(n):
      mini = inf
      for k in range(1, i + 1):
        energy = e + k - A[i - k]
        if energy >= 0 and energy < n:
          mini = min(mini, F[i - k][energy] + 1)
      F[i][e] = mini
  for line in F:
    print(line)
  return min(F[n - 1])


runtests(zbigniew)