def dfs(matrix, key, visited, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
        return

    if matrix[i][j] != key:
        return
    if visited[i][j]:
        return
    visited[i][j] = True
    dfs(matrix, key, visited, i+1, j)
    dfs(matrix, key, visited, i, j+1)
    dfs(matrix, key, visited, i-1, j)
    dfs(matrix, key, visited, i, j-1)


n = int(input())
m = int(input())
matrix = []
visited = []
total = 0
data = {}
for i in range(n):
    matrix.append(list(input()))
    visited.append([False]*m)

for i in range(n):
    for j in range(m):
        key = matrix[i][j]
        if not visited[i][j]:
            dfs(matrix, key, visited, i, j)
            if key in data.keys():
                data[key] += 1
            else:
                data[key] = 1
            total += 1

data = sorted(data.items(), key=lambda a: a[0])
print(f"Areas: {total}")

for k, v in data:
    print(f"Letter '{k}' -> {v}")
