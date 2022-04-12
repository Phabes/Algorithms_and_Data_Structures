# Algorytm działa, gdyż wagi są potegami tej samej liczby (tutaj 2), a z tego wynika, że każdą wagę ładunku jesteśmy w stanie uzyskać przy użyciu lżejszych ładunków,
# jeśli istnieją. Ale biorąc cięższy ładunek, blokujemy możliwość tego, że weźmiemy taką samą ładowność przy użyciu większej ilości ładunków.
def fillMax(W,K):
    W.sort()
    print(W)
    T=[]
    rest=K
    for i in range(len(W)-1,-1,-1):
        if W[i]<=rest:
            T.append(i)
            rest-=W[i]
    return T

W=[2,2,4,8,1,8,16]
K=27
print(fillMax(W,K))