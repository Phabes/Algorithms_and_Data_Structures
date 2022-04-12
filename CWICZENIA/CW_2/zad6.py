from random import randint,seed

def findRange(T):
    print(T)
    n=len(T)
    biggestCount=-1
    for i in range(n):
        count=0
        for j in range(n):
            if i!=j and checkInclusion(T[i],T[j]):
                count+=1
        if count>biggestCount:
            biggestCount=count
            biggestIndex=i
    return biggestCount,T[biggestIndex]

def checkInclusion(p1,p2):
    if p1[0]<=p2[0] and p1[1]>=p2[1]:
        return True
    return False

seed(21)
n=10

T=[[randint(-100,100),randint(101,200)] for _ in range(n)]
print(findRange(T))