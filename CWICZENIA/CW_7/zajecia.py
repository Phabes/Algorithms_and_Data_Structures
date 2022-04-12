from cmath import inf

def czolgi2(S, P, L, t):
    n = len(S)
    T = [[inf] * L for _ in range(n+1)]

    def f(i, y):
        if T[i][y] != inf:
            return T[i][y]

        if i == n - 1:
            if y < 0 or t - S[n-1] > L:
                T[i][y] = inf

            elif t - S[n-1] > y:
                T[i][y] = P[n-1] * (L - y)

            else:
                T[i][y] = 0

            return T[i][y]

        if y - (S[i+1]-S[i]) < 0:
            T[i][y] = f(i+1, L-(S[i+1] - S[i])) + P[i]*(L-y)

        else:
            T[i][y] = min(f(i+1, y - (S[i+1] - S[i])), f(i+1, L - (S[i+1]-S[i])) + P[i]*(L-y))

        return T[i][y]

    result = f(0, L-S[0])
    print(result)


S = [1, 3, 4, 6, 10]
P = [1, 5, 1, 2, 1]
czolgi2(S, P, 4, 13)

# [_|__|_|__|____|___]
# __1__0_3__4____4___

print("Algorytmy zachlanne")








