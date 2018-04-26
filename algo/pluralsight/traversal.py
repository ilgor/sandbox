from queue import Queue

from algo.pluralsight.adjacency_matrix_graph import *


def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print("visited: ", vertex)

        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1:
                queue.put(v)


def depth_first(graph, visited, current=0):
    if visited[current] == 1:
        return

    visited[current] = 1

    print("Visited: ", current)

    for vertex in graph.get_adjacent_vertices(current):
        depth_first(graph, visited, vertex)


g = AdjacencyMatrixGraph(9, directed=False)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

print("=" * 25)
print("Breadth-first")
print("=" * 25)
breadth_first(g, 0)

print("=" * 25)
print("Depth-first")
print("=" * 25)
visited = np.zeros(g.numVertices)
depth_first(g, visited)

