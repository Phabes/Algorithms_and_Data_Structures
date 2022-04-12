def exchange(A, T):
    F = [T + 1 for _ in range(T + 1)]
    F[0] = 0
    for i in range(1, T + 1):
        for coin in A:
            if i >= coin:
                F[i] = min(F[i], F[i - coin] + 1)
    print(F)
    return F[T]


A = [1, 5, 8]
T = 15
print(exchange(A, T))
