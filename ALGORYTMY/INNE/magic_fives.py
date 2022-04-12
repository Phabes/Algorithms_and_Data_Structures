from random import randint, shuffle, seed
from math import ceil


# Wyszukuje k-ty element, który po posortowaniu tablicy A byłby pod indeksem k
def linearselect(A, k):
  n = len(A)
  bucketNumber = ceil(n / 5)
  # Podział tablicy A na mniejsze tablice o rozmiarze co najwyżej 5
  B = [[] for _ in range(bucketNumber)]
  for i in range(n):
    B[i // 5] += [A[i]]
  C = []
  # Wyszukanie median tablic z tablicy B
  for i in range(bucketNumber):
    C += [findMedian2(B[i])]
  # Wyszukanie rekurencyjne mediany median z tablicy C
  x = findMedian(C)
  q = partition2(A, 0, n, x)
  # Sprawdzenie, z której strony będzie nasz szukany element
  if q <= k:
    return select(A, q, n - 1, k)
  return select(A, 0, q - 1, k)


# Wyszukiwanie elementu
def select(A, left, right, k):
  # Jeśli początek i koniec są równe to znaleźliśmy element
  if left == right:
    return A[right]
  q = partition(A, left, right)
  # Nasz element jest tym, względem którego dzieliliśmy
  if k == q:
    return A[k]
  # Sprawdzenie, po której stronie należy szukać elementu
  elif k < q:
    return select(A, left, q - 1, k)
  return select(A, q + 1, right, k)


# Dzielenie tablicy względem losowego element z tablicy
def partition(A, left, right):
  index = randint(left, right)
  A[right], A[index] = A[index], A[right]
  x = A[right]
  i = left - 1
  for j in range(left, right):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i + 1], A[right] = A[right], A[i + 1]
  return i + 1


# Dzielenie tablicy względem mediany median
def partition2(A, left, right, x):
  i = left - 1
  for j in range(left, right):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  return i + 1


# Wyszukiwanie mediany rekurencyjnie
def findMedian(A):
  n = len(A)
  find = n // 2
  return select(A, 0, n - 1, find)


# Wyszukiwanie mediany poprzez sortowanie przez wybieranie
def findMedian2(A):
  n = len(A)
  findIndex = n // 2
  for i in range(findIndex + 1):
    maxi = 0
    for j in range(1, n - i):
      if A[j] > A[maxi]:
        maxi = j
    A[maxi], A[n - 1 - i] = A[n - 1 - i], A[maxi]
  return A[findIndex]


seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect(A, i)
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
print("OK")