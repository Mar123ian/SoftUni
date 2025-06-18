from collections import deque
import heapq

class Graph:
	
	def __init__ (self):		
		self.distance={}
		self.parent={}
		self.graph={}
		self.weights={}
		self.visited=set()
		
	def isvisited(self, node):
		if node in self.visited:
			return True
		return False
		
	def addinvisited(self, node):
		self.visited.add(node)
		
	def addnode(self, node, child, weight):
		if first not in self.graph:
			self.graph[first]=[]
			self.distance[first]=float("inf")
			self.parent[first]=None
			
		if sec not in self.graph:
			self.graph[sec]=[]
			self.distance[sec]=float("inf")
			self.parent[sec]=None
			
	
		
		self.graph[first].append((sec,-int(weight)))
		self.graph[sec].append((first,-int(weight)))
		
		
	def getchildren(self, node):
		return self.graph[node]
		
	def changedistance(self, node, new_dist):
		self.distance[node]=new_dist
	
	def addparrent(self,node,child):
		self.parent[child]=node
	
	def getdistance(self,child):
		return self.distance[child]
		
	def addweight(self, node, weight):
		self.weights[node]=-weight
		
	def printoutput(self, target,start):
		node=target
		values=deque()
		self.weights[start]=1		
		result=100
		while node is not None:
			values.appendleft(node)
			result*=(self.weights[node]/100)
			node=self.parent[node]
		print(f"Most reliable path reliability: {result*100:.2f}%")
		print(" -> ".join(values))
		
m=int(input())
n=int(input())
graph=Graph()

for i in range(n):
	first, sec, weight=input().split()
	graph.addnode(first,sec,weight)
	
start=input()
target=input()
pk=[(0,start)]

while pk:
	min_distantion, node=heapq.heappop(pk)
	graph.addinvisited(node)
	
	if node==target:
		break
			
	for child, weight in graph.getchildren(node):
		new_dist=min_distantion+weight		
		
		if new_dist<graph.getdistance(child) and not graph.isvisited(child):			
			graph.addweight(child, weight)		
			graph.changedistance(node, new_dist)			
			graph.addparrent(node,child)		
			heapq.heappush(pk,(new_dist,child))
					
graph.printoutput(target,start)



