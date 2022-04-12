def priorityScheduling(T):
  n = len(T)
  # Sortujemy po końcach przedziłów
  T.sort(key=lambda x: x[1])
  print(T)
  # Zapamiętujemy nasz ostatni wzięty przedział
  remember = 0
  count = 1
  # Sprawdzamy każde wydarzenie, czy jest możliwość uczestnictwa w nim
  for i in range(1, n):
    if T[i][0] >= T[remember][1]:
      count += 1
      remember = i
  # Zwracamy maksymalną ilość wydarzeń w których możemy wziąć udział
  return count


T = [(1, 5), (7, 9), (2, 4), (6, 7), (3, 8), (1, 7), (5, 6)]
print(priorityScheduling(T))