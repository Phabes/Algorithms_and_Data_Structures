# Algorytm kopiuje wartości wezłów, przy usuwaniu elementu z dziećmi po obu stronach

# Reprezentacja węzła w drzewie
class BST_Node():
  def __init__(self, val, parent):
    self.val = val
    self.left = None
    self.right = None
    self.parent = parent


# Znajduje element w drzewie, jeśli taki istnieje
def find(root, val):
  while root != None:
    if root.val == val:
      return root
    elif root.val > val:
      root = root.left
    else:
      root = root.right
  return None


# Wstawia element do drzewa BST, jeśli nie ma takiego elementu już w drzewie
def insert(root, parent, val):
  # Sprawdzenie, czy nie ma takiego elementu
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


# Znajduje następnika
def findNext(root):
  # Sprawdzenie, czy trzeba szukać w górę
  if root.right == None:
    # x = root.val
    # while root.parent != None:
    #     root = root.parent
    #     if root.val > x:
    #         return root
    while root.parent != None:
      if root.parent.left == root:
        return root.parent
      root = root.parent
    return None
  root = root.right
  while root.left != None:
    root = root.left
  return root


# Znajduje poprzednika
def findPrev(root):
  # Sprawdzenie, czy trzeba szukać w górę
  if root.left == None:
    # x = root.val
    # while root.parent != None:
    #     root = root.parent
    #     if root.val < x:
    #         return root
    while root.parent != None:
      if root.parent.right == root:
        return root.parent
      root = root.parent
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


# Usuwa z drzewa BST element o podanej wartości, jeśli takie istnieje
def delete(root, val):
  node = find(root, val)
  # Sprawdzenie, czy taki element jest w drzewie BST
  if node == None:
    return root
  # Sprawdzenie, czy element nie ma dzieci
  if node.left == None and node.right == None:
    if node.parent != None:
      if node.parent.left == node:
        node.parent.left = None
      else:
        node.parent.right = None
    if node == root:
      return None
  # Sprawdzenie, czy element ma tylko prawe poddrzewo
  elif node.left == None:
    node.right.parent = node.parent
    if node.parent != None:
      if node.parent.left == node:
        node.parent.left = node.right
      else:
        node.parent.right = node.right
    if node == root:
      return root.right
  # Sprawdzenie, czy element ma tylko lewe poddrzewo
  elif node.right == None:
    node.left.parent = node.parent
    if node.parent != None:
      if node.parent.left == node:
        node.parent.left = node.left
      else:
        node.parent.right = node.left
    if node == root:
      return root.left
  # Element ma oba poddrzewa
  else:
    # Znajdujemy następnika
    x = findNext(node)
    tmp = x.val
    x.val = node.val
    node.val = tmp
    delete(x, x.val)
  return root


# Wypisuje drzewo BST
def printBST(root):
  if root != None:
    print(root.val, end=" ")
    printBST(root.left)
    printBST(root.right)


# Wypisuje rodziców w drzewie BST
def readParents(root):
  while root != None:
    print(root.val, end=" ")
    root = root.parent
  print()


start = 19
root = BST_Node(start, None)
T = [10, 15, 27, 30, 35, 13, 28, 22, 21, 20, 40, 43, 42]
# T = [10, 15, 27, 30, 35, 13, 28, 22, 20, 21, 40, 43, 42]
# T = [10, 15, 27, 30, 35, 13, 28, 22, 21, 20, 40, 43, 38, 42]
T = [10, 15, 27, 30, 35, 13, 28, 22, 21, 20, 40, 43, 38, 42, 36, 37, 39]
# T = [10, 15, 27, 30, 35, 13, 28, 22, 21, 20, 40, 43, 38, 42, 36, 39]
# T = [27, 30, 35, 38, 28, 22, 21, 20, 40, 43, 42]
# T = [10, 15, 13]
for el in T:
  root = insert(root, root, el)
# root = insert(root, root, 10)
# root = insert(root, root, 15)
# root = insert(root, root, 27)
# root = insert(root, root, 30)
# root = insert(root, root, 35)
# root = insert(root, root, 13)
# root = insert(root, root, 28)
# root = insert(root, root, 22)
# root = insert(root, root, 20)
# root = insert(root, root, 21)
# root = insert(root, root, 40)
# root = insert(root, root, 43)
# # root = insert(root, root, 38)
# root = insert(root, root, 42)
printBST(root)
print()
succ = findNext(root)
if succ == None:
  print(None)
else:
  print(succ.val)
prev = findPrev(root)
if prev == None:
  print(None)
else:
  print(prev.val)
print()

# x = findMax(root)
# print(x.val)
# x = findMin(root)
# print(x.val)
# print()
#
# x = find(root, 21)
# print(x.val)
# x = findNext(x)
# print(x.val)
# x = findPrev(x)
# print(x.val)
# x = find(root, 20)
# print(x.val)
# print()
#
# x = find(root, 15)
# x = findNext(x)
# print(x.val)
# print()
#
# printBST(root)
# print()
# root = delete(root, 20)
# printBST(root)
# print()
# root = delete(root, 18)
# printBST(root)
# print()
# root = delete(root, 35)
# printBST(root)
# print()
# root = delete(root, 30)
# printBST(root)
# print()
# root = delete(root, 19)
# printBST(root)
# print()
# print()
#
# x = find(root, 42)
# readParents(x)
# x = find(root, 28)
# readParents(x)
# x = find(root, 37)
# readParents(x)