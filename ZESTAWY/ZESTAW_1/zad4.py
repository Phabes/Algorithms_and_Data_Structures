from math import inf


def findMinMax(T):
  n = len(T)
  mini, maxi = inf, -inf
  i, j = 0, n - 1
  count = 0
  while i <= j:
    if T[i] < T[j]:
      mini2 = T[i]
      maxi2 = T[j]
      count += 1
    else:
      mini2 = T[j]
      maxi2 = T[i]
      count += 1
    if mini2 < mini:
      mini = mini2
    if maxi2 > maxi:
      maxi = maxi2
    count += 2
    i += 1
    j -= 1
  print(mini, maxi, count, n)


T = [6, 2, 6, 7, 2, 4, 6, 33, 6, 1, 6, 8, 5, 22, 3, 7]
findMinMax(T)
