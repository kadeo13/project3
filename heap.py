#!/usr/bin/python

class Heap():
	#init heap with array, size, and position
	def __init__(self):
		self.a = []
		self.s = 0
		self.p = []
	
	def newMinHeap(self, v, distance):
		minHeap = [v, distance]
		return minHeap
	
	def minHeaped(self, i):
		smallest = i
		L = 2*i + 1
		R = 2*i + 2

		if L < self.s and self.a[L][1] < self.a[smallest][1]:
			smallest = L

		if R < self.s and self.a[R][1] < self.a[smallest][1]:
			smallest = R

		if smallest != i:
			self.p[self.a[smallest][0]] = i
			self.p[self.a[i][0]] = smallest

			self.swapMinHeap(smallest, i)
			self.minHeaped(smallest)
	
	def swapMinHeap(self, a, b):
		c = self.a[a]
		self.a[a] = self.a[b]
		self.a[b] = c
	
	def extractMin(self):
		if self.isEmpty() == True:
			return

		r = self.a[0]
		lastNode = self.a[self.s - 1]
		self.a[0] = lastNode
		self.p[lastNode[0]] = 0
		self.p[r[0]] = self.s - 1
		self.s -= 1
		self.minHeaped(0)
		return r
	
	def isEmpty(self):
		if self.s == 0:
			return True
		else:
			return False
	
	def decreaseKey(self, v, distance):
		i = self.p[v]
		self.a[i][1] = distance

		while i > 0 and self.a[i][1] < self.a[(i - 1) / 2][1]:
			self.p[self.a[i][0]] = (i-1)/2
			self.p[self.a[(i-1)/2][0]] = i
			self.swapMinHeap(i, (i - 1)/2)
			i = (i-1)/2
	
	def isInMinHeap(self, v):
		if v in range(len(self.p)):
			if self.p[v] < self.s:
				return True
			else:
				return False
		else:
			return False
	
