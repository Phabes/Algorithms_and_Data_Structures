from math import inf


class Node():
  def __init__(self, val):
    self.val = val
    self.children = []
    self.best = 0


def printTree(v):
  print(v.val, v.best)
  for child in v.children:
    printTree(child)

def findBest(v,best):
  best=max(best,v.best)
  for child in v.children:
    best=findBest(child,best)
  return best


def tree(root):
  f(root)
  best=findBest(root,-inf)
  return best

def f(v):
  best = -inf
  for child in v.children:
    best = max(best, f(child) + v.val)
  v.best = max(v.best, v.val, best)
  return v.best


T = [2, -1, -3, 8, 0, 1, 2]
root = Node(-10)
A = [Node(T[i]) for i in range(len(T))]
root.children = [A[0], A[1]]
A[0].children = [A[2], A[3]]
A[3].children = [A[4], A[5]]
A[4].children = [A[6]]
printTree(root)
print()
print(tree(root))
print()
printTree(root)
