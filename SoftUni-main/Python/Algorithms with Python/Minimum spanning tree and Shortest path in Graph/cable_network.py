from queue import PriorityQueue

class Edge:
	
	def __init__ (self, first, sec, weight):
		self.first=first
		self.sec=sec
		self.weight=int(weight)
		
	def __gt__(self,other):
		return self.weight>other.weight
		
target=int(input())	
m=int(input())
n=int(input())
graph={}
visited=set()
q=PriorityQueue()

for i in range(n):
	
	data=input().split()	
	first, sec, weight=data[0:3]	
		
	if first not in graph:
		graph[first]=[]
		
	if sec not in graph:
		graph[sec]=[]
						
	a=Edge(first,sec,weight)
	b=Edge(sec,first,weight)
	graph[first].append(a)
	graph[sec].append(b)
	
	if len(data)==4:
		visited.update([first,sec])

def prim(graph,visited,target):
	w=0;
	
	for parent in visited:
		for child in graph[parent]:
			if child.sec not in visited:
				q.put(child)
				
	while not q.empty():		
		edge=q.get()
		
		if edge.sec in visited or edge.first not in visited:		
			continue
			
		visited.add(edge.sec)
		
		if w+edge.weight>=target:
			return w
			
		w+=edge.weight		
		
		for child in graph[edge.sec]:
			
			if child.sec not in visited:			
				q.put(child)
				
	return w
		
print(f"Budget used: {prim(graph,visited,target)}")


