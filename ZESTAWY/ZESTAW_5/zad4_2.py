# ZADANIE 4.2

def longestIncreasingSubsequence(A):
    n = len(A)
    T = []
    for i in range(n):
        a = binarySearch(T, A[i])
        if len(T) == a:
            T.append(A[i])
        else:
            T[a] = A[i]
        print(a, T)
    return len(T), T


def binarySearch(T, val):
    left = 0
    right = len(T) - 1
    middle = (right + left) // 2
    while left <= right:
        if T[middle] == val:
            return middle
        elif T[middle] < val:
            left = middle + 1
        else:
            right = middle - 1
        middle = (right + left) // 2
    if left == middle or middle == right:
        return left
    return len(T)


A = [3, 5, 1, 7, 2, 4, 8, 6, 1, 3]
print(longestIncreasingSubsequence(A))
