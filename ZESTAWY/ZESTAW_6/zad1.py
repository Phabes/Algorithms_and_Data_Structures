def drzewa(A):
  n = len(A)
  if n == 1:
    return A[0]
  elif n == 2:
    return max(A[0], A[1])
  # Tablica przechowująca maksymalny zysk do i-tego drzewa
  F = [0] * n
  # Wypełnienie podstawowych założeń
  F[0] = A[0]
  F[1] = max(A[0], A[1])
  # Obliczenie pozostałych wartości
  for i in range(2, n):
    F[i] = max(F[i - 2] + A[i], F[i - 1])
  print(F)
  return F[n - 1]


A = [6, 5, 7, 6, 4, 6, 9]
print(drzewa(A))