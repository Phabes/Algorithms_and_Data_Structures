def sortWordsAtIndex(A, letterIndex):
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


def findMaxLength(A):
  biggest = 0
  for word in A:
    if len(word) > biggest:
      biggest = len(word)
  return biggest


def sortString(A):
  n = len(A)
  biggest = findMaxLength(A)
  buckets = [[] for _ in range(biggest + 1)]
  for word in A:
    buckets[len(word)].append(word)
  words = []
  for i in range(biggest, 0, -1):
    words = buckets[i] + words
    if i > 0:
      sortWordsAtIndex(words, i - 1)
  for i in range(n):
    A[i] = words[i]


A = ["sbsdnsa", "bq", "qabdsddu", "x", "aavd", "aa", "bsijijij", "ssbsa", "aaa", "aavdp"]
# A = ['aab', 'bsbsbd', 'baaad', 'sagh', 'aaaaaa', 'asdf', 'a']
# A = ["aaab", "aaa", "abc", "bcaa", "aa", "acab", "hwdp"]
print(A)
sortString(A)
print(A)
for i in range(len(A) - 1):
  if A[i] > A[i + 1]:
    print("Błąd sortowania")
    exit(0)
print("OK")