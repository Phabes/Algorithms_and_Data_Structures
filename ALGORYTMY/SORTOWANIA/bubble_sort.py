from random import randint


def bubbleSort(tab):
  n = len(tab)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if tab[j] > tab[j + 1]:
        tab[j], tab[j + 1] = tab[j + 1], tab[j]


n = 20
tab = [randint(0, n - 1) for _ in range(20)]
print(tab)
bubbleSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")