from collections import deque

def bfs(start, target, graph):
	queue=deque([(start,0)])
	visited=set([start])
	
	while queue:
		node, distantion=queue.popleft()
		
		if node==target:
			return distantion
			
		for child in graph[node]:
			if child not in visited:
				visited.add(child)
				queue.append((child, distantion+1))
        
	return -1


n=int(input())
m=int(input())
graph={}

for i in range(n):
	sourse, destinations=input().split(":")
	graph[sourse]=destinations.split()
	
for i in range(m):
	start, target=input().split("-")
	print(f"{{{start}, {target}}} -> {bfs(start, target, graph)}")
  
