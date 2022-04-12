def findCheapestWay(A):
    y=len(A)
    x = len(A[0])
    T=[[0]*x for _ in range(y)]
    for i in range(y):
        for j in range(x):
            T[i][j]=A[i][j]
            if i==0 and j>0:
                T[i][j]+=T[i][j-1]
            elif j==0 and i>0:
                T[i][j]+=T[i-1][j]
            elif j!=0 and i!=0:
                T[i][j]+=min(T[i-1][j],T[i][j-1])
    for line in T:
        print(line)
    return T[y-1][x-1]

A=[
    [1,1,4,1],
    [2,3,5,6],
    [4,1,7,8],
    [5,2,2,1]
]
print(findCheapestWay(A))