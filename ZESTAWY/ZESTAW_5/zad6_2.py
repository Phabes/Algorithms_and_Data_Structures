def maxiMin(A, k):
    n = len(A)
    T = [[-1] * n for _ in range(k + 1)]
    return f(k, n - 1, A, T)


def f(i, j, A, T):
    if T[i][j] >= 0:  # TABLICA
        return T[i][j]
    if i == 0:
        T[i][j] = 0  # TABLICA
        return 0
    if i == 1:
        summ = 0
        for s in range(j + 1):
            summ += A[s]
        T[i][j] = summ  # TABLICA
        return summ

    max_now = 0
    for p in range(j):
        summ = 0
        for l in range(p, j + 1):
            summ += A[l]
        fval = f(i - 1, p - 1, A, T)  # TU BYŁO    fval = f(i - 1, p, A, T)
        min_local = min(fval, summ)
        max_now = max(max_now, min_local)
    T[i][j] = max_now  # TABLICA
    return max_now


A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3
print(maxiMin(A, k))
