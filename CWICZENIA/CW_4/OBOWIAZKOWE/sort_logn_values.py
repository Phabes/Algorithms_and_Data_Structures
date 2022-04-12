from random import randint
from math import log2, ceil
import time


def sort(A):
  n = len(A)
  limit = ceil(log2(n))
  copyTab = [0] * n
  countTab = [0] * limit
  valuesTab = []
  for i in range(n):
    if A[i] not in valuesTab:
      valuesTab += [A[i]]
      countTab[len(valuesTab) - 1] += 1
    else:
      index = valuesTab.index(A[i])
      countTab[index] += 1
  print(valuesTab,countTab)
  selection_sort(valuesTab, countTab)
  print(valuesTab,countTab)
  for i in range(1, limit):
    countTab[i] += countTab[i - 1]
  for i in range(n - 1, -1, -1):
    index = valuesTab.index(A[i])
    countTab[index] -= 1
    copyTab[countTab[index]] = A[i]
  for i in range(n):
    A[i] = copyTab[i]


def selection_sort(tab, tab2):
  n = len(tab)
  for i in range(1, n):
    maxi = 0
    for j in range(1, n - i + 1):
      if tab[j] > tab[maxi]:
        maxi = j
    tab[maxi], tab[n - i] = tab[n - i], tab[maxi]
    tab2[maxi], tab2[n - i] = tab2[n - i], tab2[maxi]


n = 1000000
tab = [randint(0, ceil(log2(n)) - 1) for _ in range(n)]
# tab=[4, 0, 0, 4, 4, 0, 4, 0, 4, 3, 3, 4, 1, 4, 0, 0, 3, 3, 4, 3]
# print(tab)
start = time.time()
sort(tab)
end = time.time()
print(end - start)
# print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")
