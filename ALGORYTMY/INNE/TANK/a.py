def minFuels(S, L, t):
  currentPosition = 0
  found = False
  countFuels = 0
  while not found:
    found = checkIfInRange(t,S[currentPosition], L)
    if not found:
      countFuels += 1
      currentPosition = findFurthestStation(S, currentPosition, L)
      if currentPosition == None:
        return False
  return countFuels


def findFurthestStation(S, start, d):
  n = len(S)
  currDistance = S[start]
  index = start + 1
  while index < n and checkIfInRange(S[index], d, currDistance):
    index += 1
  index -= 1
  if start == index:
    return None
  return index


def checkIfInRange(end,currentDistance, d):
  if end - currentDistance <= d:
    return True
  return False


S = [0, 2, 4, 6, 9, 11, 13, 16, 18, 20, 25]
d = 7
t = 32
print(minFuels(S, d, t))
