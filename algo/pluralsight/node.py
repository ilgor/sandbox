"""
A single node in graph represented by an adjacent set. Every node has a vertex id
Each node is associated with a set of adjacent vertices
"""

class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("The vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adjacent_vetices(self):
        return sorted(self.adjacency_set)