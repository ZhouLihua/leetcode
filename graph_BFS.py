#!/usr/bin/env python

"""
Breadth First Search or BFS for a Graph

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post).
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again.
To avoid processing a node more than once, we use a boolean visited array.
For simplicity, it is assumed that all vertices are reachable from the starting vertex.
"""

from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if v not in self.graph[u]:
            self.graph[u].append(v)

    def BFS(self, u):
        visited = [False for _ in range(len(self.graph))]
        queue = []

        queue.append(u)
        visited[u] = True

        while queue:
            s = queue.pop(0)
            print s, " "
            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.BFS(2)

