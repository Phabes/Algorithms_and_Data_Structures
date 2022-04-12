# Znajduje uniwersalne ujściec
def universalOutfall(G):
  n = len(G)
  for i in range(n):
    found = True
    for j in range(n):
      if i != j and (G[i][j] == 1 or G[j][i] == 0):
        found = False
        break
    if found:
      return i
  return None


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
  [1, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 0, 0]
]
print(universalOutfall(G))