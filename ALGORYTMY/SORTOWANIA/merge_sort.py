from random import randint


def mergeSort(T):
  n = len(T)
  if n <= 1:
    return T
  half = n // 2
  sorted1 = T[:half]
  sorted2 = T[half:]
  mergeSort(sorted1)
  mergeSort(sorted2)
  nSorted1 = len(sorted1)
  nSorted2 = len(sorted2)
  i = j = 0
  while i < nSorted1 and j < nSorted2:
    if sorted2[j] > sorted1[i]:
      T[i + j] = sorted1[i]
      i += 1
    else:
      T[i + j] = sorted2[j]
      j += 1
  while i < nSorted1:
    T[i + j] = sorted1[i]
    i += 1
  while j < nSorted2:
    T[i + j] = sorted2[j]
    j += 1
  return T


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
mergeSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")