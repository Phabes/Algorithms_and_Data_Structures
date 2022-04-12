def longestCommonSubstring(A, B, i, j):
    if i < 0 or j < 0:
        return 0
    if A[i] == B[j]:
        return longestCommonSubstring(A, B, i - 1, j - 1) + 1
    a = longestCommonSubstring(A, B, i - 1, j)
    b = longestCommonSubstring(A, B, i, j - 1)
    return max(a, b)


A = "DAMIAN"
# B="KACZKA"
B = "XDITN"
# B="WOJTEK"
lenA = len(A)
lenB = len(B)
print(longestCommonSubstring(A, B, lenA - 1, lenB - 1))
