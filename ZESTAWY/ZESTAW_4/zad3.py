def anagram1(A, B, alphabet):
  n = len(A)
  k=len(alphabet)
  countTab = [0] * k
  countZero = k
  for i in range(n):
    x=findIndexInAlphabet(alphabet,A[i])
    countTab[x] += 1
    countZero+=checkIndex(countTab,x)
    x=findIndexInAlphabet(alphabet,B[i])
    countTab[x] += 1
    countZero+=checkIndex(countTab,x)
  if countZero==0:
    return True
  return False


def findIndexInAlphabet(alphabet, letter):
  return alphabet.index(letter)

def checkIndex(countTab,index):
  if countTab[index] == 1:
    return -1
  elif countTab[index] == 0:
    return 1
  return 0

word1="aga"
word2="agi"
alphabet=["a","i","g"]
print(anagram1(word1, word2, alphabet))
