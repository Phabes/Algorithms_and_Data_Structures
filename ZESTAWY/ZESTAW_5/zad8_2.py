def findCheapestWay(A,i,j):
    if i==j==0:
        return A[0][0]
    if i==0:
        return findCheapestWay(A,0,j-1)+A[0][j]
    if j==0:
        return findCheapestWay(A,i-1,0)+A[i][0]
    a=findCheapestWay(A,i-1,j)+A[i][j]
    b=findCheapestWay(A,i,j-1)+A[i][j]
    return min(a,b)

A=[
    [1,1,4,1],
    [2,3,5,6],
    [4,1,7,8],
    [5,2,2,1]
]
n=len(A)
m=len(A[0])
print(findCheapestWay(A,n-1,m-1))