class BST_Node():
  def __init__(self, val, parent):
    self.val = val
    self.left = None
    self.right = None
    self.parent = parent


def find(root, val):
  while root != None:
    if root.val == val:
      return root
    elif root.val > val:
      root = root.left
    else:
      root = root.right
  return None


def insert(root, parent, val):
  if root == None:
    return BST_Node(val, parent)
  else:
    if root.val == val:
      return root
    elif root.val > val:
      root.left = insert(root.left, root, val)
    else:
      root.right = insert(root.right, root, val)
  return root


def findNext(root):
  if root.right == None:
    x = root.val
    while root.parent != None:
      root = root.parent
      if root.val > x:
        return root
    return None
  root = root.right
  if root == None:
    return None
  while root.left != None:
    root = root.left
  return root


def findPrev(root):
  if root.left == None:
    x = root.val
    while root.parent != None:
      root = root.parent
      if root.val < x:
        return root
    return None
  root = root.left
  while root.right != None:
    root = root.right
  return root


# Znajduje min w drzewie BST
def findMin(root):
  while root.left != None:
    root = root.left
  return root


# Znajduje max w drzewie BST
def findMax(root):
  while root.right != None:
    root = root.right
  return root


# Usuwa
def delete(root):
  if root.left == None and root.right == None:
    if root.parent.left == root:
      root.parent.left = None
    else:
      root.parent.right = None
  elif root.left == None:
    if root.parent.left == root:
      root.parent.left = root.right
    else:
      root.parent.right = root.right
    root.right.parent = root.parent
  elif root.right == None:
    if root.parent.left == root:
      root.parent.left = root.left
    else:
      root.parent.right = root.left
    root.left.parent = root.parent
  else:
    x = findNext(root)
    root.left.parent = x
    root.right.parent = x
    x.parent = root.parent
    if root.parent.left == root:
      root.parent.left = x
    else:
      root.parent.right = x
    if x.left == None:
      x.left = root.left
    if x.right == None:
      x.right = root.right


# Wypisuje drzewo BST
def printBST(root):
  if root != None:
    print(root.val, end=" ")
    printBST(root.left)
    printBST(root.right)


root = BST_Node(19, None)
root = insert(root, root, 10)
root = insert(root, root, 15)
root = insert(root, root, 27)
root = insert(root, root, 30)
root = insert(root, root, 35)
# root = insert(root, root, 38)
root = insert(root, root, 13)
root = insert(root, root, 28)
root = insert(root, root, 22)
root = insert(root, root, 21)
root = insert(root, root, 20)
root = insert(root, root, 40)
root = insert(root, root, 43)
root = insert(root, root, 42)
printBST(root)
print()
succ = findNext(root)
if succ == None:
  print(None)
else:
  print(succ.val)
print()
prev = findPrev(root)
if prev == None:
  print(None)
else:
  print(prev.val)
print()

x = findMax(root)
print(x.val)
x = findMin(root)
print(x.val)
print()

x = find(root, 21)
print(x.val)
x = findNext(x)
print(x.val)
x = findPrev(x)
print(x.val)
x = find(root, 20)
print(x.val)
# x = findPrev(x)
# print(x.val)
print()

x = find(root, 15)
x = findNext(x)
print(x.val)
print()

x = find(root, 20)
delete(x)
printBST(root)
print()
x = find(root, 35)
delete(x)
printBST(root)
print()
x = find(root, 30)
delete(x)
printBST(root)
print()