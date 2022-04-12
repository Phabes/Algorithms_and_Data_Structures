from random import randint,seed

def findRange(T):
    print(T)
    n=len(T)
    tab=[[T[0],[]]]
    print(tab)
    for i in range(1,n):
        if not findPlace(tab,T[i]):
            tab.append([T[i],[]])
        print("XDD",tab)
    print(tab)
    for i in range(len(tab)):
        print(tab[i][0])

def findPlace(tab,p):
    n=len(tab)
    for i in range(n):
        print("SD",tab[i][0],p,i)
        if checkInclusion(tab[i][0],p):
            print("SD2",tab[i][0],p,i)
            if len(tab[i][1])==0:
                print("SD3",tab[i][0],p,i)
                tab[i][1].append([p,[]])
                return True
            if not findPlace(tab[i][1],p):
                tab[i][1].append([p, []])
                return True
    return False

# check if p1 includes p2
def checkInclusion(p1,p2):
    if p1[0]<=p2[0] and p1[1]>=p2[1]:
        return True
    return False

seed(21)
n=10

T=[[randint(-100,100),randint(101,200)] for _ in range(n)]
print(findRange(T))