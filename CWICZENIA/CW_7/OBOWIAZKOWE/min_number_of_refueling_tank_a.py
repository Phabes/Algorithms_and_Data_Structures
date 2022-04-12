# Zadanie a

def tank(L, S, P, t):
  n = len(S)
  # Nie ma tylu stacji
  if n < t:
    return None
  # Tablica, która przechowuje minimalną liczbę tankowań aby dotrzeć do stacji i
  T = [0 for _ in range(t)]
  rememberLast = 0
  # Obliczamy minimalną liczbę tankowań dla punktu i
  for i in range(t):
    if S[i] - S[i - 1] > L:
      return None
    if S[i] - rememberLast > L:
      for j in range(i, t):
        T[j] += 1
      rememberLast = S[i - 1]
  print(T)
  return T[t - 1]


L = 20
S = [4, 6, 11, 13, 18, 21, 25]
P = [3, 5, 7, 2, 4, 5, 6]
t = len(S)
print(tank(L, S, P, t))
