from random import randint, seed, shuffle


def findElementK(tab, left, right, index):
  if left == right:
    return tab[left]
  q = randomPartition(tab, left, right)
  if q == index:
    return tab[q]
  if q < index:
    return findElementK(tab, q + 1, right, index)
  return findElementK(tab, left, q - 1, index)


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


n = 8
T = [i + 1 for i in range(n)]
shuffle(T)
print(T)
k = 6
print(findElementK(T, 0, len(T) - 1, k))