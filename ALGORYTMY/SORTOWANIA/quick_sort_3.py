from random import randint


def quickSort(tab, left, right):
  while left < right:
    q = randomPartition(tab, left, right)
    if q - left < right - q:
      quickSort(tab, left, q - 1)
      left = q + 1
    else:
      quickSort(tab, q + 1, right)
      right = q - 1


def randomPartition(tab, left, right):
  i = randint(left, right)
  # i=(left+right)//2
  tab[right], tab[i] = tab[i], tab[right]
  return partition(tab, left, right)


def partition(tab, left, right):
  x = tab[right]
  i = left - 1
  for j in range(left, right):
    if tab[j] <= x:
      i += 1
      tab[i], tab[j] = tab[j], tab[i]
  tab[i + 1], tab[right] = tab[right], tab[i + 1]
  return i + 1


tab = [randint(1, 20) for _ in range(100)]
quickSort(tab, 0, len(tab) - 1)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")