from random import randint


def quickSort(tab, left, right):
  if left < right:
    q = partition(tab, left, right)
    quickSort(tab, left, q - 1)
    quickSort(tab, q + 1, right)


def partition(tab, left, right):
  x = tab[right]
  i = left - 1
  for j in range(left, right):
    if tab[j] <= x:
      i += 1
      tab[i], tab[j] = tab[j], tab[i]
  tab[i + 1], tab[right] = tab[right], tab[i + 1]
  return i + 1


n = 20
tab = [randint(0, n - 1) for _ in range(100)]
print(tab)
quickSort(tab, 0, len(tab) - 1)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")