from random import randint


def selectionSort(tab):
  n = len(tab)
  for i in range(1, n):
    maxi = 0
    for j in range(1, n - i + 1):
      if tab[j] > tab[maxi]:
        maxi = j
    tab[maxi], tab[n - i] = tab[n - i], tab[maxi]


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
selectionSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")