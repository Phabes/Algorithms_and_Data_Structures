from random import randint, seed


class Node:
  def __init__(self):
    self.next = None
    self.value = None


# Sortuje listę jednokierunkową
def qsort(L):
  L = quickSortList(L, None)
  return L


# Sortuje zadaną część listy
def quickSortList(first, last):
  if first != last:
    first, pivotStart, pivotEnd = partition(first, last)
    # Sortujemy lewą część od pivot'a
    first = quickSortList(first, pivotStart)
    # Sortujemy prawą część od pivot'a
    pivotEnd.next = quickSortList(pivotEnd.next, last)
  return first


# Dzieli zadaną część listy na elementy mniejsze, równe i większe od pivot'a, zwraca krotkę postaci (pierwszy element posortowanej listy, pivot, ostatnie powtórzenie pivot'a)
def partition(first, last):
  pivot = first
  prev = first
  p = first.next
  # Tutaj zostaną zapamiętane wszystkie elementy równe pivot'owi
  pivot_copies = Node()
  while p != last:
    if p.value < pivot.value:
      prev.next = p.next
      p.next = first
      first = p
      p = prev.next
    elif p.value > pivot.value:
      prev = p
      p = p.next
    else:
      prev.next = p.next
      p.next = pivot_copies.next
      pivot_copies.next = p
      p = prev.next
  pivot_copies = pivot_copies.next
  # Sprawdzamy, czy były jakieś elementy równe pivot'owi
  if pivot_copies != None:
    tmp = pivot.next
    pivot.next = pivot_copies
    while pivot_copies.next != None:
      pivot_copies = pivot_copies.next
    pivot_copies.next = tmp
    return first, pivot, pivot_copies
  return first, pivot, pivot


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


# seed(42)

n = 100
T = [randint(1, 100) for i in range(n)]
L = tab2list(T)

print("przed sortowaniem: L =", end=" ")
printlist(L)
L = qsort(L)
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