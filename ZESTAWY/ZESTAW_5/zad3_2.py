def longestCommonSubstring(A, B, i, j, longest):
    if i < 0 or j < 0:
        return longest
    if A[i] == B[j]:
        return longestCommonSubstring(A, B, i - 1, j - 1, longest + 1)
    a = longestCommonSubstring(A, B, i - 1, j, longest)
    b = longestCommonSubstring(A, B, i, j - 1, longest)
    if a > b:
        return a
    return b


A = "DAMIAN"
# B="KACZKA"
B = "XDITN"
lenA = len(A)
lenB = len(B)
print(longestCommonSubstring(A, B, lenA - 1, lenB - 1, 0))
