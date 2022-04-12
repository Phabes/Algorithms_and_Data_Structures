from random import randint


def quickSort(tab, left, right):
  i, j = left, right
  el = tab[(left + right) // 2]
  while i < j:
    while tab[i] < el:
      i += 1
    while tab[j] > el:
      j -= 1
    if i <= j:
      tab[i], tab[j] = tab[j], tab[i]
      i += 1
      j -= 1
    if left < j:
      quickSort(tab, left, j)
    if right > i:
      quickSort(tab, i, right)


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