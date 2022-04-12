# FUNKCJA: f(i,w) - największy zysk jaki mżna osiągnąć wybierając sposród przedmiotów od 0 do i, nie przekraczając wagi w
# Wybiera przedmioty o jak największym symarycznym zysku, nie przekraczając łącznie maksymalnego udźwigu plecaka
def knapsack(W, P, maxW):
  print(W)
  print(P)
  print(maxW)
  n = len(W)
  # Wypełniamy naszą tablicę zysków (F) zerami (n wierszy - każdy przedmiot, maxW+1 kolumn - możliwe wagi)
  # To jest równoważne z zapisem poniższym tylko jest uniwersalniejsze
  # F=[None]*n
  # for i in range(n):
  #   F[i]=[0]*(maxW+1)
  # Zapis w Pythonie
  F = [[0] * (maxW + 1) for _ in range(n)]
  # Pierwszy wiersz (F[0]) wypełniamy od wagi pierwszego przedmiotu (W[0]) do maksymalnego udźwigu plecaka (maxW) wartością pierwszego przedmiotu (P[0])
  for w in range(W[0], maxW + 1):
    F[0][w] = P[0]
  # Uzupełniamy kolejne wiersze (F[i])
  for i in range(1, n):
    for w in range(1, maxW + 1):
      # Wybieramy większy zysk nie biorąc i-tego przedmiotu (F[i - 1][w]) albo biorąc i-ty przedmiot (F[i - 1][w - W[i]] + P[i])
      F[i][w] = F[i - 1][w]
      if w >= W[i]:
        F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
  # Zwracamy nasz maksymalny zysk oraz indeksy więtych przedmiotów
  return F[n - 1][maxW], getSolution(F, W, P, n - 1, maxW)


# Odtwarza rozwiązanie zadania
def getSolution(F, W, P, i, w):
  # Sprawdzamy czy jest to ostatni rozpatrywany przedmiot
  if i == 0:
    # Sprawdzamy czy jesteśmy wstanie wziąć pierwszy element
    if w >= W[0]:
      return [0]
    return []
  # Sprawdzamy czy i-ty przedmiot zmieści się w plecaku i czy faktycznie był wzięty
  if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
    return getSolution(F, W, P, i - 1, w - W[i]) + [i]
  return getSolution(F, W, P, i - 1, w)


W = [4, 5, 12, 9, 1, 13]
P = [10, 8, 4, 5, 3, 7]
maxW = 24
# P = [10, 8, 4, 5, 3]
# W = [4, 5, 12, 9, 1]
# MaxW = 24
print(knapsack(W, P, maxW))