def checkWaterVolume(T,A,h1,h2):
    # print(T,A,h1,h2)
    height=(h1+h2)/2
    waterVolume=checkSum(T,height)
    if h1==h2 or waterVolume[0]==A:
        return waterVolume[1]
    if waterVolume[0]>A:
        return checkWaterVolume(T,A,h1,height)
    return checkWaterVolume(T,A,height,h2)

def checkSum(T,height):
    sum=0
    count=0
    for container in T:
        if height>=container[0][1]:
            sum+=(abs(container[0][0]-container[1][0])*abs(container[0][1]-container[1][1]))
            count+=1
        elif height>container[1][1]:
            sum+=(abs(container[0][0]-container[1][0])*abs(height-container[1][1]))
    # print(sum,height)
    return sum,count

T=[
    [(-3,2),(-1,-2)],
    [(2,5),(5,1)],
    [(2,0),(3,-1)]
]
A=12
h1=-20
h2=100
print(checkWaterVolume(T,A,h1,h2))