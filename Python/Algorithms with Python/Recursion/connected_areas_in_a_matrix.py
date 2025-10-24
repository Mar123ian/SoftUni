def find_area_size(matrix, r, c, area_size):
    if r < 0 or c < 0 or r > len(matrix) - 1 or c > len(matrix[0]) - 1 or matrix[r][c] == "*":
        return area_size

    else:
        matrix[r][c] = "*"

        area_size = find_area_size(matrix, r + 1, c, area_size)
        area_size = find_area_size(matrix, r, c + 1, area_size)
        area_size = find_area_size(matrix, r, c - 1, area_size)
        area_size = find_area_size(matrix, r - 1, c, area_size)

    return area_size + 1


m = int(input())
n = int(input())

matrix = [list(input()) for i in range(m)]
data = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "-":
            data.append((i, j, find_area_size(matrix, i, j, 0)))

data = sorted(data, key=lambda x: (-x[2], x[0], x[1]))

print(f"Total areas found: {len(data)}")
for i in range(len(data)):
    print(f"Area #{i + 1} at ({data[i][0]}, {data[i][1]}), size: {data[i][2]}")
