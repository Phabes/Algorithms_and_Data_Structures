from random import randint


def countSort(A, index):
  n = len(A)
  factor = n ** index
  countTab = [0] * n
  for i in range(n):
    countTab[(A[i] // factor) % n] += 1
  for i in range(1, n):
    countTab[i] += countTab[i - 1]
  copyTab = [0] * n
  for i in range(n - 1, -1, -1):
    index = (A[i] // factor) % n
    countTab[index] -= 1
    copyTab[countTab[index]] = A[i]
  for i in range(n):
    A[i] = copyTab[i]


def sort(A,power):
  for i in range(power):
    countSort(A, i)


n = 101
power=2
tab = [randint(0, n ** power - 1) for _ in range(n)]
print(tab)
sort(tab,power)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")