# Reprezentacja wierzchołka
class Node():
  def __init__(self, val, parent, amount):
    self.val = val
    self.parent = parent
    self.amount = amount
    self.left = None
    self.right = None


def insert(root, parent, val, amount):
  if root == None:
    return Node(val, parent, amount)
  else:
    if root.val == val:
      return root
    elif root.val > val:
      root.left = insert(root.left, root, val, amount)
    else:
      root.right = insert(root.right, root, val, amount)
  return root

# ZADANIE 1.1
def find(root, i):
  if root == None:
    return None
  if root.left == None:
    if i == 1:
      return root
    return find(root.right, i - 1)
  if root.left.amount >= i:
    return find(root.left, i)
  if root.left.amount + 1 == i:
    return root
  return find(root.right, i - root.left.amount - 1)

# ZADANIE 1.2
def which(x):
  count=1
  if x.left!=None:
    count+=x.left.amount
  while x.parent!=None:
    if x==x.parent.right:
      if x.parent.left!=None:
        count+=x.parent.left.amount
      count+=1
    x=x.parent
  return count

root = Node(7, None, 8)
root = insert(root, root, 7, 8)
root = insert(root, root, 3, 3)
root = insert(root, root, 1, 1)
root = insert(root, root, 6, 1)
root = insert(root, root, 20, 4)
root = insert(root, root, 18, 1)
root = insert(root, root, 21, 2)
root = insert(root, root, 23, 1)
x=find(root, 5)
if x==None:
  print(None)
else:
  print(x.val)
  print(which(x))