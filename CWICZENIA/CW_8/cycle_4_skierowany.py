class Vertex:
    def __init__(self, label):
        self.label = label

def find_cycle(V, adj_M):
    n = len(V)
    connectors_M = [[-1] * n for _ in range(n)]

    for i in range(n):
        _in = []
        _out = []
        for j in range(n):
            # po wierszu
            if adj_M[i][j] == 1:
                _out.append(j)
            # po kolumnie
            if adj_M[j][i] == 1:
                _in.append(j)

        for x in _in:
            for y in _out:
                if x != y:
                    connectors_M[x][y] = i
                    if connectors_M[y][x] != -1 and connectors_M[y][x] != i:
                        return V[x], V[connectors_M[x][y]], V[y], V[connectors_M[y][x]]



# przykład
v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8 = Vertex("0"), Vertex("1"), Vertex("2"), Vertex("3"), Vertex("4"), Vertex("5"), Vertex("6"), Vertex("7"), Vertex("8")
vertices = [v_0, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8]
adj_matrix = [[0, 0, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0]]

res = find_cycle(vertices, adj_matrix)
[print(x.label, end=" ") for x in res]