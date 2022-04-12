from random import random
from math import floor


def bucketSort(A):
  n = len(A)
  buckets = [[] for _ in range(n)]
  step = 1 / n
  for element in A:
    # buckets[floor(element/step)].append(element)
    buckets[floor(element / step)] += [element]
  index = 0
  for bucket in buckets:
    selectionSort(bucket)
    for element in bucket:
      A[index] = element
      index += 1


def selectionSort(tab):
  n = len(tab)
  for i in range(1, n):
    maxi = 0
    for j in range(1, n - i + 1):
      if tab[j] > tab[maxi]:
        maxi = j
    tab[maxi], tab[n - i] = tab[n - i], tab[maxi]


n = 20
tab = [random() for _ in range(20)]
print(tab)
bucketSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")