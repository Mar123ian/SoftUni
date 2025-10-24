graph = {}
iscycle = False
while True:
    inp = input()
    if inp == "End":
        break
    parent, child = inp.split("-")

    if parent not in graph.keys():
        graph[parent] = [child]
    else:
        graph[parent].append(child)


def dfs(graph, visited, cycles, node, iscycle):
    visited.add(node)
    cycles.add(node)
    for child in graph[node]:

        if child in cycles:
            return True
        if child not in visited and child in graph.keys():
            iscycle = dfs(graph, visited, cycles, child, iscycle)
    cycles.remove(node)
    return iscycle


visited = set()
cycles = set()

for k in graph.keys():
    if k not in visited and not iscycle:
        iscycle = dfs(graph, visited, cycles, k, iscycle)

if iscycle:
    print("Acyclic: No")
else:
    print("Acyclic: Yes")
