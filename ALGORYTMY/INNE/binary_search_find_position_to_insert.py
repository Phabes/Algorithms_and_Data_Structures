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
  return right + 1


T = [3, 4, 8, 20, 33, 90]
k = 5
print(binarySearch(T, k))
k = 32
print(binarySearch(T, k))