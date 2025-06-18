class Edge:
	
	def __init__ (self, first, sec, weight):
		self.first=first
		self.sec=sec
		self.weight=int(weight)
		
def find_first_root(node,parent):
	
	while node!=parent[node]:
		node=parent[node]
	
	return node

m=int(input())
n=int(input())
graph=[]
distance={}
parent={}
sum=0

for i in range(n):
	first, sec, weight=input().split(" - ")
	parent[first]=first
	parent[sec]=sec
	graph.append(Edge(first,sec,weight))

for edge in sorted(graph, key=lambda a: a.weight):
	f=find_first_root(edge.first, parent)
	s=find_first_root(edge.sec, parent)
	
	if f!=s:
		parent[f]=s
		sum+=edge.weight
		
print(f"Total cost: {sum}")
	
