def binarySearch(T, val):
  left = 0
  right = len(T) - 1
  while left <= right:
    middle = (right + left) // 2
    if T[middle] == val:
      return middle
    elif T[middle] < val:
      left = middle + 1
    else:
      right = middle - 1
  return -1


T = [3, 4, 8]
k = 5
print(binarySearch(T, k))
k = 8
print(binarySearch(T, k))
