# Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). Proszę zaproponować
# jak najszybszy algorytm, który znajduje ścieżkę z danego wierzchołka s do danego wierzchołka t taką, że:
#   a) Każda kolejne krawędź ma mniejszą wagę niż poprzednia
#   b) Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag

from math import floor

class Node():
    def __init__(self, value, weight, enter_c=0):
        self.value = value
        self.cost = weight
        self.enter_c = enter_c

class PriorityQueue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def Insert(self, node):
        self.queue.append(node)
        self.size += 1
        self.heapify_up(self.size-1)

    def Pop(self):
        to_return = self.queue[0]
        self.queue[0], self.queue[self.size-1] = self.queue[self.size-1], self.queue[0]
        self.queue.pop()
        self.size -= 1
        self.heapify_down(0)
        return to_return

    def getParent(self, i):
        return floor((i-1)/2)

    def getLeft(self, i):
        return 2*i + 1

    def getRight(self, i):
        return 2*i + 2

    def heapify_down(self, i):
        min_index = i
        left = self.getLeft(i)
        right = self.getRight(i)

        if left < self.size and self.queue[left].cost < self.queue[min_index].cost:
            min_index = left

        if right < self.size and self.queue[right].cost < self.queue[min_index].cost:
            min_index = right

        if min_index != i:
            self.queue[i], self.queue[min_index] = self.queue[min_index], self.queue[i]
            self.heapify_down(min_index)

    def heapify_up(self, i):
        if i != 0:
            parent_i = self.getParent(i)

            if self.queue[parent_i].cost > self.queue[i].cost:
                self.queue[parent_i], self.queue[i] = self.queue[i], self.queue[parent_i]
                self.heapify_up(parent_i)

    def printQueue(self):
        for elem in self.queue:
            print("[{}, {}, {}]".format(elem.value, elem.cost, elem.enter_c), end=' ')
        print("")

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

def decreasing_costs(G, V, s, t):

    def relax(u_val, v_val, v_cost, enter_c):
        nonlocal distance
        nonlocal parent
        nonlocal prioQueue
        nonlocal failed
        nonlocal moved_on

        if (distance[v_val] > distance[u_val] + v_cost and enter_c > v_cost) or failed[v_val]:
            distance[v_val] = distance[u_val] + v_cost
            parent[v_val] = u_val
            prioQueue.Insert(Node(v_val, distance[v_val], v_cost))
            failed[v_val] = False
            moved_on = True

    def get_route(parent, i, path):
        if i >= 0:
            get_route(parent, parent[i], path)
            path.append(i)

    distance = [float('inf') for _ in range(V)]
    distance[s] = 0

    failed = [False for _ in range(V)]

    parent = [-1 for _ in range(V)]
    prioQueue = PriorityQueue()
    prioQueue.Insert(Node(s, 0, float('inf')))

    # i = 0;

    while not prioQueue.isEmpty():
        u = prioQueue.Pop()
        # print("-"*10)
        # print(u.value, u.cost, u.enter_c)
        if u.value == t:
            break
        moved_on = False

        for (v_val, v_cost) in G[u.value]:
            relax(u.value, v_val, v_cost, u.enter_c)

        # print(moved_on)

        if not moved_on:
            failed[u.value] = True

        # print("failed: ", failed)
        # print("parent: ", parent)
        # print("distance: ", distance)
        # prioQueue.printQueue()

        # if i == 0:
        #     break
        # i += 1

    if distance[t] == float('inf') or distance[t] == 0:
        print("{} —> {} (None)".format(s, t))
    else:
        path = []
        get_route(parent, t, path)
        print("{} —> {} ({}) path: {}".format(s, t, distance[t], path))

#----TEST A----
G_1 = [
    [(1, 10), (2, 5)], # 0
    [(0, 10), (3, 8), (6, 12)], # 1
    [(0, 5), (3, 4), (4, 3)],   # 2
    [(1, 8), (2, 4), (6, 7)],   # 3
    [(2, 3), (5, 2)],   # 4
    [(4, 2), (6, 11)],   # 5
    [(1, 12), (3, 7), (5, 11), (7, 2)], # 6
    [(6, 2)]    # 7
]
# results:
# 0 —> 0 (None)
# 0 —> 1 (10) path: [0, 1]
# 0 —> 2 (5) path: [0, 2]
# 0 —> 3 (9) path: [0, 2, 3]
# 0 —> 4 (8) path: [0, 2, 4]
# 0 —> 5 (10) path: [0, 2, 4, 5]
# 0 —> 6 (25) path: [0, 1, 3, 6]
# 0 —> 7 (27) path: [0, 1, 3, 6, 7]
# 1 —> 0 (10) path: [1, 0]
# 1 —> 1 (None)
# 1 —> 2 (12) path: [1, 3, 2]
# 1 —> 3 (8) path: [1, 3]
# 1 —> 4 (15) path: [1, 3, 2, 4]
# 1 —> 5 (17) path: [1, 3, 2, 4, 5]
# 1 —> 6 (12) path: [1, 6]
# 1 —> 7 (14) path: [1, 6, 7]
# 2 —> 0 (5) path: [2, 0]
# 2 —> 1 (None)
# 2 —> 2 (None)
# 2 —> 3 (4) path: [2, 3]
# 2 —> 4 (3) path: [2, 4]
# 2 —> 5 (5) path: [2, 4, 5]
# 2 —> 6 (None)
# 2 —> 7 (None)
# 3 —> 0 (None)
# 3 —> 1 (8) path: [3, 1]
# 3 —> 2 (4) path: [3, 2]
# 3 —> 3 (None)
# 3 —> 4 (7) path: [3, 2, 4]
# 3 —> 5 (9) path: [3, 2, 4, 5]
# 3 —> 6 (7) path: [3, 6]
# 3 —> 7 (9) path: [3, 6, 7]
# 4 —> 0 (None)
# 4 —> 1 (None)
# 4 —> 2 (3) path: [4, 2]
# 4 —> 3 (None)
# 4 —> 4 (None)
# 4 —> 5 (2) path: [4, 5]
# 4 —> 6 (None)
# 4 —> 7 (None)
# 5 —> 0 (None)
# 5 —> 1 (None)
# 5 —> 2 (22) path: [5, 6, 3, 2]
# 5 —> 3 (18) path: [5, 6, 3]
# 5 —> 4 (2) path: [5, 4]
# 5 —> 5 (None)
# 5 —> 6 (11) path: [5, 6]
# 5 —> 7 (13) path: [5, 6, 7]
# 6 —> 0 (22) path: [6, 1, 0]
# 6 —> 1 (12) path: [6, 1]
# 6 —> 2 (11) path: [6, 3, 2]
# 6 —> 3 (7) path: [6, 3]
# 6 —> 4 (13) path: [6, 5, 4]
# 6 —> 5 (11) path: [6, 5]
# 6 —> 6 (None)
# 6 —> 7 (2) path: [6, 7]
# 7 —> 0 (None)
# 7 —> 1 (None)
# 7 —> 2 (None)
# 7 —> 3 (None)
# 7 —> 4 (None)
# 7 —> 5 (None)
# 7 —> 6 (2) path: [7, 6]
# 7 —> 7 (None)
V_1 = len(G_1)

#----TEST B----
G_2 = [
    [(1, 6), (6, 2)],
    [(5, 5), (2, 5)],
    [(3, 2), (4, 3)],
    [],
    [(7, 4), (8, 2)],
    [(2, 4), (6, 3), (7, 3)],
    [(0, 2), (7, 2), (8, 5)],
    [],
    []
]
# result:
# 0 —> 0 (None)
# 0 —> 1 (6) path: [0, 1]
# 0 —> 2 (11) path: [0, 1, 2]
# 0 —> 3 (13) path: [0, 1, 2, 3]
# 0 —> 4 (14) path: [0, 1, 2, 4]
# 0 —> 5 (11) path: [0, 1, 5]
# 0 —> 6 (2) path: [0, 6]
# 0 —> 7 (14) path: [0, 1, 5, 7]
# 0 —> 8 (16) path: [0, 1, 2, 4, 8]
# 1 —> 0 (10) path: [1, 5, 6, 0]
# 1 —> 1 (None)
# 1 —> 2 (5) path: [1, 2]
# 1 —> 3 (7) path: [1, 2, 3]
# 1 —> 4 (8) path: [1, 2, 4]
# 1 —> 5 (5) path: [1, 5]
# 1 —> 6 (8) path: [1, 5, 6]
# 1 —> 7 (8) path: [1, 5, 7]
# 1 —> 8 (10) path: [1, 2, 4, 8]
# 2 —> 0 (None)
# 2 —> 1 (None)
# 2 —> 2 (None)
# 2 —> 3 (2) path: [2, 3]
# 2 —> 4 (3) path: [2, 4]
# 2 —> 5 (None)
# 2 —> 6 (None)
# 2 —> 7 (None)
# 2 —> 8 (5) path: [2, 4, 8]
# 3 —> 0 (None)
# 3 —> 1 (None)
# 3 —> 2 (None)
# 3 —> 3 (None)
# 3 —> 4 (None)
# 3 —> 5 (None)
# 3 —> 6 (None)
# 3 —> 7 (None)
# 3 —> 8 (None)
# 4 —> 0 (None)
# 4 —> 1 (None)
# 4 —> 2 (None)
# 4 —> 3 (None)
# 4 —> 4 (None)
# 4 —> 5 (None)
# 4 —> 6 (None)
# 4 —> 7 (4) path: [4, 7]
# 4 —> 8 (2) path: [4, 8]
# 5 —> 0 (5) path: [5, 6, 0]
# 5 —> 1 (None)
# 5 —> 2 (4) path: [5, 2]
# 5 —> 3 (6) path: [5, 2, 3]
# 5 —> 4 (7) path: [5, 2, 4]
# 5 —> 5 (None)
# 5 —> 6 (3) path: [5, 6]
# 5 —> 7 (3) path: [5, 7]
# 5 —> 8 (9) path: [5, 2, 4, 8]
# 6 —> 0 (2) path: [6, 0]
# 6 —> 1 (None)
# 6 —> 2 (None)
# 6 —> 3 (None)
# 6 —> 4 (None)
# 6 —> 5 (None)
# 6 —> 6 (None)
# 6 —> 7 (2) path: [6, 7]
# 6 —> 8 (5) path: [6, 8]
# 7 —> 0 (None)
# 7 —> 1 (None)
# 7 —> 2 (None)
# 7 —> 3 (None)
# 7 —> 4 (None)
# 7 —> 5 (None)
# 7 —> 6 (None)
# 7 —> 7 (None)
# 7 —> 8 (None)
# 8 —> 0 (None)
# 8 —> 1 (None)
# 8 —> 2 (None)
# 8 —> 3 (None)
# 8 —> 4 (None)
# 8 —> 5 (None)
# 8 —> 6 (None)
# 8 —> 7 (None)
# 8 —> 8 (None)
V_2 = len(G_2)

#----TEST C----
G_3 = [
    [(1, 4), (4, 8)],
    [(4, 3)],
    [(3, 3)],
    [],
    [(7, 2), (5, 4)],
    [(2, 1), (3, 5)],
    [(4, 10)],
    []
]
# results:
# 0 —> 0 (None)
# 0 —> 1 (4) path: [0, 1]
# 0 —> 2 (12) path: [0, 1, 4, 5, 2]
# 0 —> 3 (None)
# 0 —> 4 (7) path: [0, 1, 4]
# 0 —> 5 (11) path: [0, 1, 4, 5]
# 0 —> 6 (None)
# 0 —> 7 (9) path: [0, 1, 4, 7]
# 1 —> 0 (None)
# 1 —> 1 (None)
# 1 —> 2 (None)
# 1 —> 3 (None)
# 1 —> 4 (3) path: [1, 4]
# 1 —> 5 (None)
# 1 —> 6 (None)
# 1 —> 7 (5) path: [1, 4, 7]
# 2 —> 0 (None)
# 2 —> 1 (None)
# 2 —> 2 (None)
# 2 —> 3 (3) path: [2, 3]
# 2 —> 4 (None)
# 2 —> 5 (None)
# 2 —> 6 (None)
# 2 —> 7 (None)
# 3 —> 0 (None)
# 3 —> 1 (None)
# 3 —> 2 (None)
# 3 —> 3 (None)
# 3 —> 4 (None)
# 3 —> 5 (None)
# 3 —> 6 (None)
# 3 —> 7 (None)
# 4 —> 0 (None)
# 4 —> 1 (None)
# 4 —> 2 (5) path: [4, 5, 2]
# 4 —> 3 (None)
# 4 —> 4 (None)
# 4 —> 5 (4) path: [4, 5]
# 4 —> 6 (None)
# 4 —> 7 (2) path: [4, 7]
# 5 —> 0 (None)
# 5 —> 1 (None)
# 5 —> 2 (1) path: [5, 2]
# 5 —> 3 (5) path: [5, 3]
# 5 —> 4 (None)
# 5 —> 5 (None)
# 5 —> 6 (None)
# 5 —> 7 (None)
# 6 —> 0 (None)
# 6 —> 1 (None)
# 6 —> 2 (15) path: [6, 4, 5, 2]
# 6 —> 3 (None)
# 6 —> 4 (10) path: [6, 4]
# 6 —> 5 (14) path: [6, 4, 5]
# 6 —> 6 (None)
# 6 —> 7 (12) path: [6, 4, 7]
# 7 —> 0 (None)
# 7 —> 1 (None)
# 7 —> 2 (None)
# 7 —> 3 (None)
# 7 —> 4 (None)
# 7 —> 5 (None)
# 7 —> 6 (None)
# 7 —> 7 (None)
V_3 = len(G_3)

G_4 = [
    [],
    [(3, 1), (5, 12), (2, 2)],
    [],
    [(2, 3), (4, 4)],
    [(5, 5)],
    []
]
# results:
# 0 —> 0 (None)
# 0 —> 1 (None)
# 0 —> 2 (None)
# 0 —> 3 (None)
# 0 —> 4 (None)
# 0 —> 5 (None)
# 1 —> 0 (None)
# 1 —> 1 (None)
# 1 —> 2 (2) path: [1, 2]
# 1 —> 3 (1) path: [1, 3]
# 1 —> 4 (None)
# 1 —> 5 (12) path: [1, 5]
# 2 —> 0 (None)
# 2 —> 1 (None)
# 2 —> 2 (None)
# 2 —> 3 (None)
# 2 —> 4 (None)
# 2 —> 5 (None)
# 3 —> 0 (None)
# 3 —> 1 (None)
# 3 —> 2 (3) path: [3, 2]
# 3 —> 3 (None)
# 3 —> 4 (4) path: [3, 4]
# 3 —> 5 (None)
# 4 —> 0 (None)
# 4 —> 1 (None)
# 4 —> 2 (None)
# 4 —> 3 (None)
# 4 —> 4 (None)
# 4 —> 5 (5) path: [4, 5]
# 5 —> 0 (None)
# 5 —> 1 (None)
# 5 —> 2 (None)
# 5 —> 3 (None)
# 5 —> 4 (None)
# 5 —> 5 (None)
V_4 = len(G_4)

# for i in range(V_2):
#     for j in range(V_2):
#         decreasing_costs(G_2, V_2, i, j)
decreasing_costs(G_2, V_2, 0, 0)