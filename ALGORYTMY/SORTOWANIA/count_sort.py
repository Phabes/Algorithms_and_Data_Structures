from random import randint


def countSort(A, k):
  n = len(A)
  countTab = [0] * k
  for i in range(n):
    countTab[A[i]] += 1
  for i in range(1, k):
    countTab[i] += countTab[i - 1]
  copyTab = [0] * n
  for i in range(n - 1, -1, -1):
    countTab[A[i]] -= 1
    copyTab[countTab[A[i]]] = A[i]
  for i in range(n):
    A[i] = copyTab[i]


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
countSort(tab, n)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")