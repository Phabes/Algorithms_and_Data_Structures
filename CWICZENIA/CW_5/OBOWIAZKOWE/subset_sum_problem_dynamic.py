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
  # Wypełniamy tablicę (F) fałszami (n+1 wierszy - każda rozpatrywana wartość jak również żadna z nich, T+1 kolumn - możliwe sumy)
  F = [[False] * (T + 1) for _ in range(n + 1)]
  # Pierwszą kolumnę (suma równa 0) można wypełnić prawdami, gdyż aby otrzymać sumę równą 0 nie bierzemy żadnego przedmiotu
  for i in range(n):
    F[i][0] = True
  # Uzupełniamy kolejne wiersze (F[i])
  for i in range(1, n + 1):
    # Sprawdza czy ropatrywany element jest równy poszukiwanej sumie
    if A[i - 1] == T:
      return True, [i - 1]
    for j in range(1, T + 1):
      # WARTOŚĆ F[i][j]
      # TRUE: Uzyskaliśmy określoną sumę (j) nie biorąc elementu i-1 (F[i - 1][j]) albo biorąc nasz element (F[i - 1][j - A[i - 1]])
      # FALSE: Nie uzyskaliśmy określonej sumy (j) nie biorąc elementu i-1 (F[i - 1][j]) albo biorąc nasz element (F[i - 1][j - A[i - 1]]) dalej jej nie otrzymaliśmy
      F[i][j] = F[i - 1][j]
      if j >= A[i - 1] and F[i - 1][j - A[i - 1]]:
        F[i][j] = F[i - 1][j - A[i - 1]]
  for i in range(n):
    print(F[i])
  # Zwracamy wartość czy udało nam się znaleźć jakikolwiek podciąg, który sumuje się do T oraz indeksy wziętych wartości
  return F[n - 1][T], getSolution(A, F, n - 1, T), getSolution2(A, F, n, T)


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
  if j >= A[i - 1] and F[i - 1][j - A[i - 1]]:
    return getSolution(A, F, i - 1, j - A[i - 1]) + [i - 1]
  return []


def getSolution2(A, F, i, T):
  P = []
  while T > 0:
    while F[i - 1][T]:
      i -= 1
    P.append(i - 1)
    T -= A[i - 1]
  P.reverse()
  return P


T = [13, 7, 21, 42, 8, 2, 44, 52]
# T = [2,3,7,8,10]
# T = [13,2]
# T = [13]
# T = []
suma = 51
print(subsetSum(T, suma))