# FUNKCJA: f(i,j) -> minimalna waga dla przedmiotów od 0 do i które mają zysk j lub większy jeśli jest to możliwe do uzyskania, jeśli nie to jest to suma wag wszystkich przedmiotów
def knapsack_v2(P, W, maxW):
  print(W)
  print(P)
  print(maxW)
  price_sum = 0
  weight_sum = 0
  n = len(W)
  # Liczy maksymalną wagę i zysk
  for i in range(n):
    price_sum += P[i]
    weight_sum += W[i]
  # Wypełniamy naszą tablicę wag (F) maksymalną możliwą wagą (weight_sum) (n wierszy - każdy przedmiot, price_sum+1 kolumn - możliwe zyski)
  # To jest równoważne z zapisem poniższym tylko jest uniwersalniejsze
  # for i in range(n):
  #   for j in range(price_sum + 1):
  #     F[i].append(weight_sum)
  # Zapis w Pythonie
  F = [[weight_sum + 1] * (price_sum + 1) for _ in range(n)]
  # Móc wziąć pierwszy element oznacza, że minimalna waga jaką możemy wziąć jest równa wadze tego przedmiotu
  F[0][P[0]] = W[0]
  # Minimalna waga jaką chcemy mieć używając i przedmiotów nie chcąc mieć żadnego zysku (F[i][0]) jest równa 0
  for i in range(n):
    F[i][0] = 0
  for i in range(1, n):
    for j in range(price_sum + 1):
      # Wybieramy najmniejszą wagę nie biorąc i-tego przedmiotu albo (F[i - 1][j]) albo biorą i-ty przedmiot (F[i - 1][j - P[i]] + W[i]))
      F[i][j] = F[i - 1][j]
      if j >= P[i]:
        F[i][j] = min(F[i][j], F[i - 1][j - P[i]] + W[i])
  for i in F:
    print(i)
  # Liczymy ile zysków jesteśmy w stanie uzyskać używając wszystkich przedmiotów nie przekraczając wagi maxW
  for p in range(price_sum, -1, -1):
    if F[n - 1][p] != weight_sum + 1 and F[n - 1][p] <= MaxW:
      return p, getSolution(F, W, P, n - 1, p)


# Odtwarza rozwiązanie zadania
def getSolution(F, W, P, i, p):
  # Sprawdzamy czy szukany zysk jest równy 0
  if p == 0:
    return []
  # Sprawdzamy czy jest to ostatni przedmiot
  if i == 0:
    return [0]
  # Sprawdzamy czy nie wzięliśmy i-tego przedmiotu
  if F[i - 1][p] == F[i][p]:
    return getSolution(F, W, P, i - 1, p)
  return getSolution(F, W, P, i - 1, p - P[i]) + [i]


W = [4, 5, 12, 9, 1]
P = [10, 8, 4, 5, 3]
MaxW = 24
# W = [4, 5, 12, 9, 1, 13]
# P = [10, 8, 4, 5, 3, 7]
# maxW = 24
print(knapsack_v2(P, W, MaxW))