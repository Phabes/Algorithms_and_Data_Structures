from random import randint

def leader(A):
    print(A)
    tab=[]
    limit=len(A)//2+1
    for element in A:
        if element not in tab:
            tab.append(element)
            count=0
            for el in A:
                if el==element:
                    count+=1
                    if count>=limit:
                        return True
    return False

n=7
scope=2
A=[randint(-scope,scope) for _ in range(n)]
print(leader(A))