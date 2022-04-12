from random import randint, shuffle, seed


def linearselect(A, k):
  return select(A, 0, len(A) - 1, k)


def select(A, p, r, k):
  if p == r:
    return A[r]
  q = partition(A, p, r)
  if k == q:
    return A[k]
  elif k < q:
    return select(A, p, q - 1, k)
  return select(A, q + 1, r, k)


def partition(tab, left, right):
  x = tab[right]
  i = left - 1
  for j in range(left, right):
    if tab[j] <= x:
      i += 1
      tab[i], tab[j] = tab[j], tab[i]
  tab[i + 1], tab[right] = tab[right], tab[i + 1]
  return i + 1


seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect(A, i)
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)
print("OK")