from math import inf


def tank(L, S, P, t):
  S.append(t)
  P.append(0)
  print(S)
  print(P)
  n = len(S)
  # Wyznaczamy punkt startowy i najlepszą stację, do której należy się udać oraz początkowy stan baku
  now = 0
  x = findBest(now, L, S, P)
  current = L
  suma = 0
  while x != n - 1:
    # Sprawdzenie czy dojedziemy do następnej stacji
    if x == now:
      return None
    # Sprawdzamy czy można lepiej gdzieś zatankować niż w miejscu, w którym przebywamy
    if P[now] >= P[x]:
      # Sprawdzamy czy damy radę dojechać do naszego miejsca, w którym zatankujemy bardziej opłacalnie
      if current >= S[x] - S[now]:
        current -= (S[x] - S[now])
      else:  # Tankujemy tyle ile musimy, aby dojechać do stacji, w której zatankujemy bardziej opłacalnie
        suma += ((S[x] - S[now] - current) * P[now])
        current = 0
    else:  # W oklicy nie zatankujemy bardziej opłacalnie, więc tankujemy do pełna
      suma += ((L - current) * P[now])
      current = L - (S[x] - S[now])
    print(x, suma)
    now = x
    x = findBest(now, L, S, P)
  # Sprawdzenie czy musieliśmy zatankować na ostatniej stacji oraz doliczamy koszt tankowania na ostatnim postoju
  if current < S[x] - S[now]:
    suma += ((S[x] - S[now] - current) * P[now])
  return suma


# Znajduje najbliższą najtańszą stację po stacji o indexie i
def findBest(i, L, S, P):
  # Sprawdzamy czy nawet przy pełnym baku jesteśmy w stanie dojechać do następnej stacji
  if S[i + 1] - S[i] > L:
    return i
  n = len(S)
  # Zwraca najbliższą najtańszą stację
  for j in range(i + 1, n):
    if S[j] - S[i] <= L and P[i] >= P[j]:
      return j
    if S[j] - S[i] > L:
      break
  return i + 1


# S = [0, 4, 6, 11, 13, 18, 21]
# P = [inf, 3, 5, 7, 2, 4, 5]
# t = 25
# L = 7
# S = [0, 4, 6, 11, 13]
# P = [inf, 3, 5, 6, 2]
# S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20]
# P = [inf, 4, 3, 2, 3, 3, 5, 4, 2, 4]
# t = 23
# L = 7
# S = [0, 15, 25, 40, 60, 75]
# P = [inf, 4, 5, 4, 3, 2]
# t = 80
# L = 35
# S = [0, 3, 5, 7, 10, 16, 20]
# P = [inf, 1, 2, 3, 4, 5, 6]
# t = 21
# L = 7
# S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20]
# P = [inf, 4, 3, 3, 3, 2, 5, 4, 2, 4]
# t = 23
# L = 7
# S = [0, 2, 4, 6]
# P = [inf, 4, 2, 4]
# t = 9
# L = 7
# S = [0, 8, 11, 15, 16]
# P = [inf, 40, 7, 15, 12]
# t = 23
# L = 10
# S = [0,1, 9, 15, 16, 17, 27, 28]
# P = [inf,1, 100, 10, 15, 1, 30, 30]
# t = 30
# L = 14
# S=[0,1,9,15,16,17,27]
# P=[inf,1,10,10,5,1,30]
# L=14
# t=30
S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20]
P = [inf, 4, 3, 2, 3, 3, 5, 4, 2, 4]
L = 7
t = 25
# S = [0, 1, 2, 3]
# P = [inf, 0.8, 1, 0.8]
# L = 2
# t = 4
print(tank(L, S, P, t))
