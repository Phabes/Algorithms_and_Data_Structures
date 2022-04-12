def exchange(A, T):
    n = len(A)
    if T == 0:
        return 0
    smallest=float("inf")
    for i in range(n):
        if T>=A[i]:
            a = exchange(A, T - A[i]) + 1
            if a < smallest:
                smallest = a
    return smallest


A = [1, 5, 8]
T = 15
print(exchange(A, T))