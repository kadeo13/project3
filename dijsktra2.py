#!/usr/bin/python

from graph import Graph

G = Graph(6)
G.addEdge(1, 2, 4)
G.addEdge(1, 3, 1)
G.addEdge(1, 4, 5)
G.addEdge(1, 5, 8)
G.addEdge(1, 6, 10)
G.addEdge(3, 2, 2)
G.addEdge(4, 5, 2)
G.addEdge(5, 6, 1)
G.dijkstra(0)
