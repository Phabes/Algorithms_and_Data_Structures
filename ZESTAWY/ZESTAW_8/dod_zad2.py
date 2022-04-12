def checkIfNonDirectedGraph(G):
  for i, v in enumerate(G):
    for number in v:
      if not i in G[number]:
        return False
  return True


G = [
  [4],
  [3, 4],
  [4],
  [1],
  [0, 1]
]
# G = [
#   [4],
#   [3, 4],
#   [4],
#   [1],
#   [0, 1, 2]
# ]
print(checkIfNonDirectedGraph(G))