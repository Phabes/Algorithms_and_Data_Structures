def klocki(A):
  n = len(A)
  # Tablica przechowująca minimalną liczbę klocków jakie należy usunąć
  T = [0] * n
  # Dla każdego klocka obliczamy wartość naszej fukcji
  for i in range(1, n):
    T[i] = T[i - 1]
    if checkInclusion(A[i - 1], A[i]):
      T[i] += 1
  print(T)
  return T[n - 1]

# Sprawdza czy nachodzi jakieś nachodzenie na siebie przedziałów
def checkInclusion(c1, c2):
  if c1[0] > c2[0] and c1[0] < c2[1]:
    return True
  if c1[1] > c2[0] and c1[1] < c2[1]:
    return True
  if c1[0] <= c2[0] and c1[1] >= c2[1]:
    return True
  return False


A = [(1, 5), (0, 7), (8, 11), (11, 15), (12, 14), (0, 13)]
print(klocki(A))