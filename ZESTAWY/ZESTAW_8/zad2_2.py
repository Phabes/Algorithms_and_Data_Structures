# Znajduje uniwersalne ujściec
def universalOutfall(G):
  n = len(G)
  i = 0
  j = 0
  while True:
    if i >= n or j >= n:
      mini = min(i, j)
      if checkEnd(G, mini):
        return mini
      else:
        i = mini + 1
        j = i
        if i >= n:
          break
    if G[i][j] == 0:
      j += 1
    else:
      i += 1
  return None


def checkEnd(G, i):
  n = len(G)
  for j in range(n):
    if i != j:
      if G[i][j] == 1 or G[j][i] == 0:
        return False
  return True


# G = [
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1],
#   [0, 0, 0, 0, 0]
# ]
# G = [
#   [0, 0, 0, 1, 0],
#   [1, 0, 0, 1, 0],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 1, 0]
# ]
G = [
  [0, 0, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 0]
]
print(universalOutfall(G))