def radixSort(A):
  if len(A):
    strLen = len(A[0])
    for i in range(strLen - 1, -1, -1):
      countSort(A, i)


def countSort(A, letterIndex):
  n = len(A)
  # Jest 26 liter w łacinie
  amount = 26
  countTab = [0] * amount
  for word in A:
    countTab[ord(word[letterIndex]) - 97] += 1
  for i in range(1, amount):
    countTab[i] += countTab[i - 1]
  copyTab = [0] * n
  for i in range(n - 1, -1, -1):
    index = ord(A[i][letterIndex]) - 97
    countTab[index] -= 1
    copyTab[countTab[index]] = A[i]
  for i in range(n):
    A[i] = copyTab[i]


n = 20
tab = ["kra", "art", "kat", "kit", "ati", "kil"]
print(tab)
radixSort(tab)
print(tab)
for i in range(len(tab) - 1):
  if tab[i] > tab[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")