from random import randint
from math import ceil, log2
import time


def binarySearch(T, k):
  l = 0
  r = len(T) - 1
  while l <= r:
    p = (l + r) // 2
    if T[p] == k:
      return p
    elif T[p] < k:
      l = p + 1
    else:
      r = p - 1
  return -1


def sortLog(T, n):  # O(n * log(logn))
  log = ceil(log2(n))
  values = []
  counter = -1
  for el in T:
    x = binarySearch(values, el)
    if x == -1:
      j = counter
      values.append(el)
      while j >= 0 and values[j] > el:
        values[j + 1] = values[j]
        j -= 1
      values[j + 1] = el
      counter += 1

  counters = [0] * log
  for el in T:
    x = binarySearch(values, el)
    counters[x] += 1
  for i in range(1, log):
    counters[i] += counters[i - 1]

  sorted = [0] * n
  for i in range(n - 1, -1, -1):
    x = binarySearch(values, T[i])
    counters[x] -= 1
    sorted[counters[x]] = T[i]

  return sorted


n = 1000000
tab = [randint(1, ceil(log2(n))) for _ in range(n)]
# print(tab)
start = time.time()
tab = sortLog(tab, n)
end = time.time()
print(end - start)
# print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")