from random import randint,seed

def findRange(T):
    n=len(T)
    tab=[[T[0]]]
    for i in range(1,n):
        added=False
        for j in range(len(tab)):
            if checkInclusion(T[i],tab[j][0]):
                tab[j]=[T[i]]+tab[j]
                added=True
                break
            elif checkInclusion(tab[j][0],T[i]):
                index=1
                for k in range(1,len(tab[j])):
                    if checkInclusion(tab[j][k],T[i]):
                        index=k+1
                tab[j].insert(index,T[i])
                added=True
                break
        if not added:
            tab.append([T[i]])
    print(tab)
    length=len(tab)
    biggestCount=-1
    for i in range(length):
        count=len(tab[i])-1
        for j in range(length):
            if i!=j:
                length2=len(tab[j])
                for k in range(1,length2):
                    if checkInclusion(tab[i][0],tab[j][k]):
                        count+=length2-k
                        break
        if count>biggestCount:
            biggestCount=count
            biggestIndex=i
    return biggestCount,tab[biggestIndex][0]

# check if p1 includes p2
def checkInclusion(p1,p2):
    if p1[0]<=p2[0] and p1[1]>=p2[1]:
        return True
    return False

seed(21)
n=10

T=[[randint(-100,100),randint(101,200)] for _ in range(n)]
print(findRange(T))