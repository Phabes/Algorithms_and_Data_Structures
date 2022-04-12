# FUNKCJA: f(i,s) - czy możliwe jest uzyskanie sumy (s), używając dowolnego podciągu wartości od 0 do i
def subsetSum(A, T):
  print(A)
  print(T)
  n = len(A)
  # Sprawdzenie czy tablica wartości (A) jest pusta
  if n == 0:
    # Sprawdzenie czy szukaną wartością jest 0
    if T == 0:
      return True, []
    return False, []
  # Wypełniamy tablicę (F) fałszami (n wierszy - każda rozpatrywana wartość, T+1 kolumn - możliwe sumy)
  F = [[False] * (T + 1) for _ in range(n)]
  # Pierwszą kolumnę (suma równa 0) można wypełnić prawdami, gdyż aby otrzymać sumę równą 0 nie bierzemy żadnego przedmiotu
  for i in range(n):
    F[i][0] = True
  # Uzupełniamy kolejne wiersze (F[i])
  for i in range(n):
    for j in range(1, T + 1):
      # Nie bierzemy tej liczby do naszego podciągu
      if i > 0:
        F[i][j] = F[i - 1][j]
      # Liczba może być przedłużeniem naszego podciągu
      if not F[i][j] and j >= A[i]:
        F[i][j] = F[i - 1][j - A[i]]
      # Liczba jest równa szukanej sumie
      if not F[i][j]:
        F[i][j] = T == A[i]
  for i in range(n):
    print(F[i])
  # Zwracamy wartość czy udało nam się znaleźć jakikolwiek podciąg, który sumuje się do T oraz indeksy wziętych wartości
  return F[n - 1][T], getSolution(A, F, n - 1, T)


def getSolution(A, F, i, j):
  # Sprawdzamy czy jest to ostatnia rozpatrywana wartość
  if i == 0:
    # Sprawdzamy czy pierwsza wartość była wzięta w naszym rozwiązaniu
    if j != 0 and F[i][j]:
      return [i]
    return []
  # Sprawdzamy czy wartość i-ta była pominięta
  if F[i - 1][j]:
    return getSolution(A, F, i - 1, j)
  # Sprawdzamy czy wartość była wzięta w naszym rozwiązaniu
  if j >= A[i] and F[i - 1][j - A[i]]:
    return getSolution(A, F, i - 1, j - A[i]) + [i]
  return []


T = [13, 7, 21, 42, 8, 2, 44, 52]
# T = [2,3,7,8,10]
# T = [13,8]
# T = [13]
# T = []
suma = 51
print(subsetSum(T, suma))
