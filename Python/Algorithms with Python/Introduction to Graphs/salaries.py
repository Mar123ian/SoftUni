def dfs(graph, node, sal, s):
    if graph[node] == []:
        return 1
    s = 0
    for child in graph[node]:
        s += dfs(graph, child, sal, s)
    sal[node] = s
    return sal[node]


n = int(input())
graph = {}
sal = {}
s = 0
sum = 0

for i in range(n):
    line = (input())
    graph[i], sal[i] = [], 0

    for j, word in enumerate(line):
        if word == "Y":
            graph[i].append(j)

for node in graph:
    sum += dfs(graph, node, sal, s)

print(sum)
