from random import randint

# LIS - n^2
def lis(A):
  n = len(A)
  # Każdy element jest najdłuższym rosnącym podciągiem
  longestSubsequence = [1] * n
  # Tablica rodziców, która pomoże odtworzyć nasz rosnący podciąg
  parents = [-1] * n
  for i in range(1, n):
    for j in range(i):
      # Sprawdzamy czy i-ty element jest przedłużeniem jakiegoś istniejącego najdłuższego podciągu rosnącego
      if A[j] < A[i] and longestSubsequence[j] + 1 > longestSubsequence[i]:
        # Ustawiamy długość naszego najdłuższego rosnącego podciągu
        longestSubsequence[i] = longestSubsequence[j] + 1
        # Zapisujemy rodzica
        parents[i] = j
  # Znajdujemy maximum
  maxi = max(longestSubsequence)
  # Znajdujemy index maximum
  index = longestSubsequence.index(maxi)
  readParents(A, parents, index)
  print()
  print(maxi)


# Odtwarza rozwiązanie zadania (rekurencyjnie)
def readParents(A, parents, i):
  # Sprawdzamy czy ten element nie był pierwszym elementem naszego najdłuższego rosnącego podciągu
  if parents[i] != -1:
    readParents(A, parents, parents[i])
  print(A[i], end=" ")


n = 10
k = 10
T = [randint(1, k) for _ in range(n)]
T = [7, 10, 7, 4, 3, 8, 3, 7, 9, 5]
print(T)
lis(T)