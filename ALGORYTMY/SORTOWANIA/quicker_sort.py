from random import randint


def quickerSort(tab, left, right):
  if left < right:
    q = partition(tab, left, right)
    quickerSort(tab, left, q[0] - 1)
    quickerSort(tab, q[1] + 1, right)


def partition(tab, left, right):
  x = tab[right]
  i = left - 1
  A = []
  for j in range(left, right):
    if tab[j] <= x:
      i += 1
      if tab[j] == x:
        A += [i]
      tab[i], tab[j] = tab[j], tab[i]
  tab[i + 1], tab[right] = tab[right], tab[i + 1]
  n = len(A)
  x = i
  j = n - 1
  while j != -1:
    tab[A[j]], tab[x] = tab[x], tab[A[j]]
    j -= 1
    x -= 1
  return i + 1 - n, i + 1


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
quickerSort(tab, 0, len(tab) - 1)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")