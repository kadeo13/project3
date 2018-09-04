#!/usr/bin/python

from collections import defaultdict
from heap import Heap
import sys

class Graph:
	#init graph with vertices and graph
	def __init__(self, V):
		self.V = V
		self.G = defaultdict(list)
	
	#adds edge to node
	def addEdge(self, n1, n2, distance):
		newN = [n2, distance]
		self.G[n1].insert(0, newN)
		newN = [n1, distance]
		self.G[n2].insert(0, newN)
	
	#prints vertex and distance
	def printGraph(self, distance, n):
		print "Vertex    Distance from source "
		space = "      "
		for i in range(n):
			print i, space, distance[i]
	
	#Finds shortest path for each node
	def dijkstra(self, init):
		V = self.V
		d = []

		minHeap = Heap()
		for v in range(V):
			d.append(sys.maxint)
			minHeap.a.append(minHeap.newMinHeap(v, d[v]))
			minHeap.p.append(v)

		minHeap.p[init] = init
		d[init] = 0
		minHeap.decreaseKey(init, d[init])

		minHeap.s = V

		while minHeap.isEmpty() == False:
			newHeapN = minHeap.extractMin()
			n = newHeapN[0]

			for j in self.G[n]:
				v = j[0]
				k = j[1]
				if minHeap.isInMinHeap(v) and d[n] == sys.maxint and k < d[v]:
					d[v] = k 
					minHeap.decreaseKey(v, d[v])

		self.printGraph(d, V)	
