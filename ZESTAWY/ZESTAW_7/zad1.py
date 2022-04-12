def findRanges(X):
    # nlogn
    X.sort()
    n=len(X)
    end=X[0]+1
    count=1
    for i in range(1,n):
        if X[i]>end:
            end=X[i]+1
            count+=1
    return count


X=[0.5,2.6,0.25,1.6]
print(findRanges(X))
X=[0.5,2.61,0.25,1.6]
print(findRanges(X))