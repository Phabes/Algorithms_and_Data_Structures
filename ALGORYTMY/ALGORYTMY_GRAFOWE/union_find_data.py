class Node():  # makeSet
  def __init__(self, val):
    self.val = val
    self.rank = 0
    self.parent = self


def find(x):  # find
  if x != x.parent:
    x.parent = find(x.parent)
  return x.parent


def union(x, y):  # union
  x = find(x)
  y = find(y)
  if x == y:
    return
  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1


def show(A):
  n = len(A)
  print()
  for i in range(n):
    print(find(A[i]).val)


A = []
for i in range(4):
  A.append(Node(i))
for i in range(4):
  print(find(A[i]).val)
union(A[0], A[2])
show(A)
union(A[1], A[3])
show(A)
union(A[1], A[1])
show(A)
union(A[1], A[2])
show(A)