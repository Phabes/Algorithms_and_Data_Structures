def maxiMin(A, k):
    n = len(A)
    # Jeśli nie ma pracowników to nie rozdamy im pracy
    if k == 0:
        return 0
    # Tablica, której wiersz oznacza ilość pracowników, a kolumna ilość płotków branych pod uwagę (pierwszy wiersz jest wypełniony zerami, gdyż bez pracowników nie rozdamy pracy)
    T = [[0] * n for _ in range(k + 1)]
    suma = 0
    # Kolejne komórki w drugim wierszu wypełniamy sumą długości ogrodzeń od początki do płotu i
    for i in range(n):
        suma += A[i]
        T[1][i] = suma
    # Dla każdej możliwej ilości pracowników (i)
    for i in range(2, k + 1):
        # Wybieramy, do którego ogrodzenia (j) malujemy
        for j in range(n):
            # Na początek ustalamy nasz maksymalny min
            # T[i-1][m] - oznacza, że i-1 pracowników maluje do m-tego ogrodzenia
            # sumElements(A,m+1,j+1)) - oznacza, że ostatni (i-ty) pracownik maluje pozostałe ogrodzenia (od m+1 do j)
            mini = min(T[i - 1][0], sumElements(A, 1, j + 1))
            maxi = mini
            for m in range(1, j):
                mini = min(T[i - 1][m], sumElements(A, m + 1, j + 1))
                maxi = max(maxi, mini)
            T[i][j] = maxi
    for line in T:
        print(line)
    # Odczytujemy rozwiązanie
    print(readSol(A, T, k, n - 1))
    # Zwracamy naszą szukaną wartość (k pracowników maluje n ogrodzeń)
    return T[k][n - 1]


# Gromadzi indexy ogrodzeń, od których kolejni malarze pracują
def readSol(A, T, i, j):
    # Sprawdzenie czy czasem nie doszliśmy do 0 pracowników
    if i == 0:  # może wystarczy i==0
        return []
    # Patrzymy czy odpowiedni podział już był dla mniejszej ilości pracowników
    for k in range(j, -1, -1):
        if (T[i - 1][k] == T[i][j]):
            return readSol(A, T, i - 1, k) + [k + 1]
    sum = 0
    # W innym przypadku odpowiedni podział znajduje się na końcu
    for k in range(j, -1, -1):
        sum += A[k]
        if sum == T[i][j]:
            return readSol(A, T, i - 1, k - 1) + [k]
    return []


# Sumuje elementy tablicy od elementu o indexie start do indexu end-1
def sumElements(A, start, end):
    sum = 0
    for i in range(start, end):
        sum += A[i]
    return sum


A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3
print(maxiMin(A, k))