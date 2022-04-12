def exchange(A, T):
    n = len(A)
    if T == 0:
        return 0
    if T < 0:
        return float("inf")
    smallest = exchange(A, T - A[0]) + 1
    for i in range(1, n):
        a = exchange(A, T - A[i]) + 1
        if a < smallest:
            smallest = a
    return smallest


A = [1, 5, 8]
T = 15
print(exchange(A, T))