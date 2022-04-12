# ZADANIE 3 ORAZ ZADANIE 4.1
def longestCommonSubstring(A, B):
    n=len(A)
    m=len(B)
    T=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                T[i][j]=T[i-1][j-1]+1
            else:
                T[i][j]=max(T[i-1][j],T[i][j-1])
    for line in T:
        print(line)
    return T[n][m]


A = [4,2,5,8,7,5]
B = A.copy()
B.sort()
print(longestCommonSubstring(A, B))
