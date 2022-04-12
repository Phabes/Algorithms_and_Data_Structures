from random import randint


def heapSort(T):
  n = len(T)
  buildHeap(T, n)
  for i in range(n - 1, 0, -1):
    T[0], T[i] = T[i], T[0]
    heapify(T, i, 0)


def buildHeap(T, n):
  for i in range(parent(n - 1), -1, -1):
    heapify(T, n, i)


def heapify(T, n, i):
  l = left(i)
  r = right(i)
  m = i
  if l < n and T[l] > T[m]:
    m = l
  if r < n and T[r] > T[m]:
    m = r
  if m != i:
    T[i], T[m] = T[m], T[i]
    heapify(T, n, m)


def left(i):
  return 2 * i + 1


def right(i):
  return 2 * i + 2


def parent(i):
  return (i - 1) // 2


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
heapSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")