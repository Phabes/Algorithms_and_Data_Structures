from queue import PriorityQueue

S = ["a", "ba", "cc", "d", "e", "f"]
F = [10, 11, 7, 13, 1, 20]


def huffman(S, F):
  n = len(S)
  # PriorityQueue zastępuje nam kopiec binarny, z którego wyciągamy dwa najmniejsze elementy
  q = PriorityQueue()
  # Wkładamy do naszego kopca kolejne symbole wraz z ich częstościami (kopiec będzie wybierał po najmniejszej częstości)
  for i in range(n):
    q.put((F[i], [S[i]]))
  # Tablica przechowująca kod Huffmana dla poszczególnych symboli
  T = [""] * n
  # Łączymy dwa najmniejsze liście
  while q.qsize() >= 2:
    # Pobieramy dwa najmniejsze liście
    first = q.get()
    second = q.get()
    # Dla każdego symbolu, które użyliśmy dodajemy rozgałęzienie (0 lub 1)
    for i in range(len(first[1])):
      index = findIndex(S, first[1][i])
      T[index] += "1"
    for i in range(len(second[1])):
      index = findIndex(S, second[1][i])
      T[index] += "0"
    freq = first[0] + second[0]
    symbol = first[1] + second[1]
    # Wstawiamy nowy liść powstały z dwóch najmniejszych
    q.put((freq, symbol))
  readSolution(S, F, T)


# Znajduje pod którym indexem jest dany symbol
def findIndex(S, symbol):
  # print(symbol)
  for i in range(len(S)):
    if S[i] == symbol:
      return i


# Odczytuje rozwiązanie dla każdego symbolu ze zbioru S oraz wypisuje łączną długość takiego napisu
def readSolution(S, F, T):
  n = len(S)
  sum = 0
  for i in range(n):
    sum += (len(T[i]) * F[i])
    print(S[i], " : ", T[i])
  print("dlugosc napisu: ", sum)


huffman(S, F)