from random import randint, seed


def mergesort(T):
  n = len(T)
  mergeSort(T, 0, n - 1)
  return T


def merge(T, left, middle, right):
  n1 = middle - left + 1
  n2 = right - middle

  L = [0] * n1
  R = [0] * n2

  for i in range(n1):
    L[i] = T[left + i]
  for i in range(n2):
    R[i] = T[middle + 1 + i]

  i, j = 0, 0
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      T[left + i + j] = L[i]
      i += 1
    else:
      T[left + i + j] = R[j]
      j += 1
  while i < n1:
    T[left + i + j] = L[i]
    i += 1
  while j < n2:
    T[left + i + j] = R[j]
    j += 1

  # i = 0
  # j = 0
  # k = left
  #
  # while i < n1 and j < n2:
  #   if L[i] <= R[j]:
  #     T[k] = L[i]
  #     i += 1
  #   else:
  #     T[k] = R[j]
  #     j += 1
  #   k += 1
  #
  # while i < n1:
  #   T[k] = L[i]
  #   i += 1
  #   k += 1
  #
  # while j < n2:
  #   T[k] = R[j]
  #   j += 1
  #   k += 1


def mergeSort(T, left, right):
  if left < right:
    middle = (left + (right - 1)) // 2
    mergeSort(T, left, middle)
    mergeSort(T, middle + 1, right)
    merge(T, left, middle, right)


# seed(42)

n = 10
T = [randint(1, 10) for i in range(n)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
  if T[i] > T[i + 1]:
    print("Błąd sortowania!")
    exit()

print("OK")