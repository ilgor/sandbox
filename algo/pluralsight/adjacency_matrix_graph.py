import numpy as np

from algo.pluralsight.graph import Graph


class AdjacencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        matrix_rows_and_cols = (numVertices, numVertices)
        self.matrix = np.zeros(matrix_rows_and_cols)

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight < 1:
            raise ValueError("Edge cannot have value < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_indegree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("Cannot access vertex %d" % v)

        indegree = 0

        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree += 1

        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


# g = AdjacencyMatrixGraph(4, directed=True)
#
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(2, 3)
#
#
# for i in range(4):
#     print("Adjacent to: ", i, g.get_adjacent_vertices(i))
#
# for i in range(4):
#     print("Indegree: ", i, g.get_indegree(i))
#
#
# for i in range(4):
#     for j in g.get_adjacent_vertices(i):
#         print("Edge weight: ", i, " ", j, " weight: ", g.get_edge_weight(i, j))
#
# g.display()
