from random import randint, seed


def heap_sort(T):
  n = len(T)
  buildHeap(T, n)
  # for i in range(n-1,0,-1):
  #     T[0],T[i]=T[i],T[0]
  #     heapify(T,i,0)


def buildHeap(T, n):
  for i in range(parent(n - 1), -1, -1):
    heapify(T, n, i)


def heapify(T, n, i):
  l = left(i)
  r = right(i)
  m = i
  if l < n and T[l] > T[m]:
    m = l
  if r < n and T[r] > T[m]:
    m = r
  if m != i:
    T[i], T[m] = T[m], T[i]
    heapify(T, n, m)


def left(i):
  return 2 * i + 1


def right(i):
  return 2 * i + 2


def parent(i):
  return (i - 1) // 2


def addToHeap(T, val):
  T += [val]
  # I SP, EFEKTYWNIEJSZY
  repairHeap(T, len(T) - 1)
  # # II SP, ALE NIE EFEKTYWNY
  # buildHeap(T,len(T))


def repairHeap(T, i):
  p = parent(i)
  if T[p] < T[i] or p == 0:
    T[p], T[i] = T[i], T[p]
    if p != 0:
      repairHeap(T, p)


def addToHeap2(T, val):
  T += [val]
  i = len(T) - 1
  p = parent(i)
  while i > 0 and T[p] < val:
    T[p], T[i] = T[i], T[p]
    i = p
    p = parent(p)
  T[i] = val


import math
from io import StringIO


def show_tree(tree, total_width=60, fill=' '):
  print(tree)
  output = StringIO()
  last_row = -1
  for i, n in enumerate(tree):
    if i:
      row = int(math.floor(math.log(i + 1, 2)))
    else:
      row = 0
    if row != last_row:
      output.write('\n')
    columns = 2 ** row
    col_width = int(math.floor((total_width * 1.0) / columns))
    output.write(str(n).center(col_width, fill))
    last_row = row
  print(output.getvalue())
  print('-' * total_width)


seed(7)

n = 10
tab = [randint(1, 20) for i in range(10)]
heap_sort(tab)
show_tree(tab)
val = 20
# addToHeap(tab,val)
addToHeap2(tab, val)
show_tree(tab)
