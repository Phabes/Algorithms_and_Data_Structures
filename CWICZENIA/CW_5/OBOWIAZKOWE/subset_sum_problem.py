# FUNKCJA: f(i,s) - czy możliwe jest uzyskanie sumy (s), używając dolownego podciągu wartości od 0 do i włącznie
def subsetSum(A, T):
  print(A)
  print(T)
  n = len(A)
  return check(A, n, T, 0, [])


def check(A, n, T, index, taken):
  if T == 0:
    print(taken)
    return True
  if index == n:
    return False
  return check(A, n, T - A[index], index + 1, taken + [index]) or check(A, n, T, index + 1, taken)


T = [13, 7, 21, 42, 8, 2, 44]
# T = [2,3,7,8,10]
# T = [13]
suma = 23
print(subsetSum(T, suma))
