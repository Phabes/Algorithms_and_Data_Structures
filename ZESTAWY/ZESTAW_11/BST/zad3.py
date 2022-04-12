class Node():
  def __init__(self, letter):
    self.letter = letter
    self.a = None
    self.c = None
    self.g = None
    self.t = None
    self.flag = False


def checkWord(root, word, i):
  if i == len(word):
    if root.flag == True:
      return False
    root.flag = True
    return True
  print(root.letter, word, i, word[i])
  if word[i] == "A":
    if root.a == None:
      root.a = Node("A")
    return checkWord(root.a, word, i + 1)
  if word[i] == "C":
    if root.c == None:
      root.c = Node("C")
    return checkWord(root.c, word, i + 1)
  if word[i] == "G":
    if root.g == None:
      root.g = Node("G")
    return checkWord(root.g, word, i + 1)
  if root.t == None:
    root.t = Node("T")
  return checkWord(root.t, word, i + 1)


def checkDifference(gens):
  root = Node(None)
  for word in gens:
    if not checkWord(root, word, 0):
      return False
  return True


gens = ["GATTACTAC", "ATTACTCCAGT", "AGTCC", "AGTTGAGA", "CTAGA", "GATTGACTAC", "ATTACTCCAGT", "AGTCCA"]
print(checkDifference(gens))
