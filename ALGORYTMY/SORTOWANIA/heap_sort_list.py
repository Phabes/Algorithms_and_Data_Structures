# Nie zrobione
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


def heapSort(L, n):
  return L


# seed(42)

n = 10
k = 100
T = [randint(1, k) for i in range(n)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = heapSort(L, n)
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