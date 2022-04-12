# Zadanie a

def tank(L, S, P, t):
  n = len(S)
  # Tablica, która przechowuje minimalną liczbę tankowań aby dotrzeć do stacji i (ostatni element to cel podróży)
  T = [0 for _ in range(n + 1)]
  rememberLast = 0
  # Obliczamy minimalną liczbę tankowań dla punktu i
  for i in range(n):
    if S[i] - S[i - 1] > L:
      return None
    if S[i] - rememberLast > L:
      for j in range(i, n + 1):
        T[j] += 1
      rememberLast = S[i - 1]
  if t - rememberLast > L:
    T[n] += 1
  rememberLast = S[n - 1]
  print(T, rememberLast)
  return T[n]


L = 20
S = [4, 6, 11, 13, 18, 21, 25]
P = [3, 5, 7, 2, 4, 5, 6]
t = 39
print(tank(L, S, P, t))
