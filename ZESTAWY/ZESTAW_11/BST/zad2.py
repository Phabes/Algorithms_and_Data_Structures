class BST_Node():
  def __init__(self, val, parent):
    self.val = val
    self.left = None
    self.right = None
    self.parent = parent


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


# Znajduje min w drzewie BST
def findMin(root):
  while root.left != None:
    root = root.left
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

def sumTree(root):
  x=findMin(root)
  suma=0
  while x!=None:
    suma+=x.val
    x=findNext(x)
  return suma

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
print(sumTree(root))