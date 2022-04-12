def macierze(A):
  print(A)
  n = len(A)
  print(f(0, n - 1, A))


# Oblicza minimalną liczbę mnożeń skalarnych potrzebnych do obliczenia iloczynu macierzy od i do j
def f(i, j, A):
  # Sprawdzamy czy jest tylko jedna macierz do mnożenia (wtedy nie trzeba nic mnożyć)
  if i == j:
    return 0
  # Wyszukujemy rekurencyjnie najlepsze nawiasowanie
  mini = f(i, i, A) + f(i + 1, j, A) + A[i][0] * A[i][1] * A[j][1]
  for k in range(i + 1, j):
    mini = min(mini, f(i, k, A) + f(k + 1, j, A) + A[i][0] * A[k][1] * A[j][1])
  return mini


A = [(50, 5), (5, 100), (100, 10)]
macierze(A)