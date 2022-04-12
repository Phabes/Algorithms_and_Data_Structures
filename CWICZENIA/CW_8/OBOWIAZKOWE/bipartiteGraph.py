from queue import PriorityQueue


# Reprezentacja wierzchołka grafu
class Summit():
    def __init__(self, info):
        self.number = info[0]
        self.name = info[1]
        self.visited = False
        self.parent = None
        self.branch = None


# Sprawdza, czy graf jest dwudzielny
def checkDuality(V, E):
    # Tworzymy tablicę naszych wierzchołków oraz kolejkę
    summits = []
    for v in V:
        summits.append(Summit(v))
    q = PriorityQueue()
    # Przechodzimy po każdym wierzchołku
    for summit in summits:
        # Sprawdzamy, czy wierzchołek nie został przydzielony do którejś strony i jeśli nie to przypisujemy go do lewej strony
        if summit.branch==None:
            summit.visited = True
            summit.branch = "left"
            q.put(summit.number)
            # Powtarzamy czynności dopóki kolejka nie jest pusta
            while not q.empty():
                # Pobieramy index z kolejki
                index = q.get()
                # Wyszukujemy wszystkie wierzchołki, z którymi nasz wierzchołek ma krawedź oraz które nie były odwiedzone i wstawiamy je do kolejki
                for e in E:
                    if index == e[0] and not summits[e[1]].visited:
                        update(summits, q, index, e[1])
                    elif index == e[1] and not summits[e[0]].visited:
                        update(summits, q, index, e[0])
    # Wypisuje nasze wierzchołki oraz po której stronie grafu dwudzielnego się znajduje
    for summit in summits:
        print(summit.name, summit.branch)
    # Sprawdza, czy jakaś krawędź nie jest po tej samej stronie grafu dwudzielnego
    for e in E:
        if summits[e[0]].branch == summits[e[1]].branch:
            print(summits[e[0]].name, summits[e[1]].name, e[0], e[1])
            return False
    # Jest to graf dwudzielny
    return True


# Uaktualnia informacje na temat wierzchołka i wstawia go do kolejki
def update(summits, q, index, coord):
    summits[coord].visited = True
    summits[coord].parent = index
    if summits[index].branch == "left":
        summits[coord].branch = "right"
    else:
        summits[coord].branch = "left"
    q.put(coord)


# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h")]
# E = [(0, 1), (0, 2), (2, 3), (1, 4), (3, 4), (2, 5), (4, 5), (5, 6), (6, 7)]
# print(checkDuality(V, E))
# E = [(0, 1), (0, 2), (2, 3), (1, 4), (2, 5), (5, 6), (6, 7)]
# print(checkDuality(V, E))
# V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g")]
# E = [(0, 1), (1, 2), (1, 4), (2, 6), (3, 4), (4, 5)]
# print(checkDuality(V, E))
# E = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 6), (3, 4), (4, 5)]
# print(checkDuality(V, E))
V = [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e"), (5, "f"), (6, "g"), (7, "h"), (8, "i"), (9, "j")]
E = []
print(checkDuality(V, E))
E = [(0, 1), (1, 2), (1, 4), (2, 6), (3, 4), (4, 5), (7, 8), (7, 9), (8, 9)]
print(checkDuality(V, E))
E = [(0, 1), (1, 2), (1, 4), (2, 6), (3, 4), (4, 5), (7, 8)]
print(checkDuality(V, E))
E = [(0, 1), (1, 2), (1, 4), (2, 6), (3, 4), (4, 5)]
print(checkDuality(V, E))
# G=[V,E]