from random import randint


def ferry(A, L):
  print(A)
  # Sprawdzamy, czy jest sens uruchamiać program
  if L < A[0]:
    return None
  n = len(A)
  # Tworzymy tablicę przechowującą nasz dane postaci [i][j][k], gdzie "i" to index pojazdu, "j" zapełnienie lewego pasu, "k" zapełnienie prawego pasu
  F = [[[False] * (L + 1) for _ in range(L + 1)] for _ in range(n)]
  # Warunki początkowe
  F[0][A[0]][0] = True
  F[0][0][A[0]] = True
  # Zmienne, które pomagają określić, od którego miejsca rozpocząć później szukanie rozwiązania
  index = 0
  remL = A[0]
  remR = 0
  # Wypełniamy naszą tablicę
  for i in range(1, n):
    for j in range(L + 1):
      for k in range(L + 1):
        if f(i, j, k, A, F):
          index = i
          remL = j
          remR = k
  # T = [0] * n
  # T[0] = A[0]
  # for i in range(1, n):
  #   T[i] += (A[i] + T[i - 1])
  # print(T)
  return readSolution(index, remL, remR, A, F, [], [])


# Liczy naszą funkcję
def f(i, l, r, A, F):
  if i < 0:
    return False
  if l >= A[i] and not F[i][l][r]:
    F[i][l][r] = f(i - 1, l - A[i], r, A, F)
  if r >= A[i] and not F[i][l][r]:
    F[i][l][r] = f(i - 1, l, r - A[i], A, F)
  return F[i][l][r]

# Odczytuje rozwiązanie, tworząc dwie tablice rozdzielając pojazdy na pasy
def readSolution(i, l, r, A, F, left, right):
  if i == 0:
    if l >= A[0]:  # and F[0][l - A[0]][r]
      return left + [0], right
    else:
      return left, right + [0]
  if l >= A[i] and F[i - 1][l - A[i]][r]:
    return readSolution(i - 1, l - A[i], r, A, F, left + [i], right)
  if r >= A[i] and F[i - 1][l][r - A[i]]:
    return readSolution(i - 1, l, r - A[i], A, F, left, right + [i])
  return left, right


# L = 8
# A = [2, 5, 2, 1, 4, 5, 2, 2, 3]
# L = 10
# A = [4, 6, 2, 4, 1, 8, 3, 5, 7, 4, 8, 3, 5, 6, 3, 1]

n=10
k=20
L=40
A = [randint(1, k) for _ in range(n)]

print(ferry(A, L))
