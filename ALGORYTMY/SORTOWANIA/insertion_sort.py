from random import randint


def insertionSort(tab):
  n = len(tab)
  for i in range(1, n):
    rem = tab[i]
    j = i - 1
    while j >= 0 and tab[j] > rem:
      tab[j + 1] = tab[j]
      j -= 1
    tab[j + 1] = rem


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
insertionSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")