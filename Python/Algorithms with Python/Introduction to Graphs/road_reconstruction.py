n=int(input())
m=int(input())
graph={}
data=[]
for i in range(m):
    inp = input()
    
    parent, child = inp.split(" - ")
    data.append((parent,child))
    
    if parent not in graph.keys():
        graph[parent] = [child]
    else:
        graph[parent].append(child)
        
    if child not in graph.keys():
        graph[child] = [parent]
    else:
        graph[child].append(parent)
        
def dfs(graph,visited,node):
	
	visited.add(node)
	for child in graph[node]:
		if child not in visited:
			dfs(graph,visited,child)
output=[]	
print("Important streets:")
for p,c in data:
	visited=set()
	graph[p].remove(c)
	graph[c].remove(p)
	i=0
	for node in graph.keys():
		if node not in visited:
			dfs(graph,visited,node)
			i+=1
		if i>1:
			output.append(sorted([p,c]))
			break
	
	graph[p].append(c)
	graph[c].append(p)
	
sorted(output,key=lambda x:x[0])
for el in output:
	print(*el)
	

