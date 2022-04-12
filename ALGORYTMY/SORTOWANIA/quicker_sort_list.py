from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None


def tab2list(A):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next


def printlist(L):
  while L != None:
    print(L.value, "->", end=" ")
    L = L.next
  print("|")


def qsort(L, n):
  if n > 1:
    less, lessCount, equal, equalCount, bigger, biggerCount = partition(L, n)
    less = qsort(less, lessCount)
    bigger = qsort(bigger, biggerCount)
    equal = addAtTheEnd(equal, bigger)
    less = addAtTheEnd(less, equal)
    L = less
  return L


def partition(L, n):
  x = randomPivot(L, n)
  less = equal = bigger = None
  lessCount = equalCount = biggerCount = 0
  while L != None:
    tmp = L.next
    L.next = None
    if L.value < x.value:
      lessCount += 1
      less = addAtTheEnd(less, L)
    elif L.value == x.value:
      equalCount += 1
      equal = addAtTheEnd(equal, L)
    else:
      biggerCount += 1
      bigger = addAtTheEnd(bigger, L)
    L = tmp
  return less, lessCount, equal, equalCount, bigger, biggerCount


def randomPivot(L, n):
  x = randint(0, n - 1)
  count = 0
  while count != x:
    count += 1
    L = L.next
  return L


def addAtTheEnd(L, p):
  first = L
  if L == None:
    return p
  while L.next != None:
    L = L.next
  L.next = p
  return first


# seed(42)

n = 10
k = 100
T = [randint(1, k) for i in range(n)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L, n)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next

print("OK")