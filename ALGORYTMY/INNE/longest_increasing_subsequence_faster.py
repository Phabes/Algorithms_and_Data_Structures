# nlogn
def LIS(T):
  n = len(T)
  # Tablica mówiąca, że na pozycji "i" jest index, pod którym w tablicy wejściowej jest najmniejsza liczba, która kończy podciąg
  # długości "i+1"
  F = [-1] * n
  # Tablica parent'ów
  P = [-1] * n
  # Tablica mówiąca, że na pozycji "i" jest liczba, która mówi jak długi jest najdłuższy spójny podciąg kończący się na elemencie "i"
  X = [1] * n
  length = 0
  F[0] = 0
  for i in range(1, n):
    if T[i] <= T[F[0]]:
      F[0] = i
    elif T[i] > T[F[length]]:
      P[i] = F[length]
      length += 1
      F[length] = i
      X[i] = length + 1
    else:
      x = binarySearch(T, F, T[i], 1, length - 1)
      F[x] = i
      P[i] = F[x - 1]
      X[i] = x + 1
  print(F)
  print(P)
  print(X)
  D = getLIS(T, P, F[length])
  # D = getLIS(T, P, F, length + 1)
  return D


def binarySearch(T, F, val, start, end):
  left = start
  right = end
  while left <= right:
    middle = (right + left) // 2
    if T[F[middle]] == val:
      return middle
    elif T[F[middle]] < val:
      left = middle + 1
    else:
      right = middle - 1
  return right + 1


def getLIS(T, P, index):
  D = []
  while index != -1:
    D.append(T[index])
    index = P[index]
  D.reverse()
  return D


# def getLIS(T, P, F, length):
#   D = [0] * length
#   i = length - 1
#   index = F[length - 1]
#   while i != -1:
#     D[i] = T[index]
#     index = P[index]
#     i -= 1
#   return D


# T = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
# T = [2, 5, 3, 7, 11, 8, 10, 13, 6]
# T = [1, 2, 3, 4, 5, 6]
T = [2, 2, 2, 3, 2, 2, 3, 2]
# T = [9, 7, 5, 3, 2, 1]
print(LIS(T))