from math import inf


def macierze(A):
  print(A)
  n = len(A)
  # Tablica do pamiętania najlepszych rozwiązań
  T = [[inf] * n for _ in range(n)]
  # Chcemy rozwiązać problem mnożenia wszystkich macierzy (od 0 do n-1)
  f(0, n - 1, A, T)  # print(f(0, n - 1, A, T))
  for line in T:
    print(line)
  # T[1][4] - najmniejszy koszt mnożenia macierzy od 1 do 4
  return T[0][n - 1]  # print(f(0, n - 1, A, T))


def f(i, j, A, T):
  # Wykorzystanie spamiętywania
  if T[i][j] != inf:
    return T[i][j]
  # Sprawdzamy czy jest tylko jedna macierz do mnożenia (wtedy nie trzeba nic mnożyć)
  if i == j:
    T[i][j] = 0
  else:
    # Wyszukujemy rekurencyjnie najlepsze nawiasowanie
    mini = f(i, i, A, T) + f(i + 1, j, A, T) + A[i][0] * A[i][1] * A[j][1]
    for k in range(i + 1, j):
      mini = min(mini, f(i, k, A, T) + f(k + 1, j, A, T) + A[i][0] * A[k][1] * A[j][1])
    T[i][j] = mini
  return T[i][j]


# A = [(50, 5), (5, 100), (100, 10)]
A = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
print(macierze(A))
