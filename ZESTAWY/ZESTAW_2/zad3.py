def findSum(T, x):
  i, j = 0, len(T) - 1
  while i < j:
    suma = T[i] + T[j]
    if suma == x:
      return (i, j)
    elif suma < x:
      i += 1
    else:
      j -= 1
  return False


T = [1, 5, 11, 12, 24, 28, 31, 32, 35, 37]
x = 70
print(findSum(T, x))
x = 60
print(findSum(T, x))
