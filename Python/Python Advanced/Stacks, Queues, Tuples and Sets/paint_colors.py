from collections import deque

input = deque(input().split())
output = []
colors = ["red", "yellow", "blue", "orange", "purple", "green"]

while len(input) > 1:
    middle = len(input) // 2 - 1
    left = input.popleft()
    right = input.pop()

    if left + right in colors:
        output.append(left + right)

    elif right + left in colors:
        output.append(right + left)

    else:
        left = left[:len(left) - 1]
        right = right[:len(right) - 1]

        if left:
            input.insert(middle, left)
            middle += 1
        if right:
            input.insert(middle, right)
if input:
    el = input.pop()
    if el in colors:
        output.append(el)

if ("red" not in output or "yellow" not in output) and "orange" in output:
    output.remove("orange")

if ("red" not in output or "blue" not in output) and "purple" in output:
    output.remove("purple")

if ("blue" not in output or "yellow" not in output) and "green" in output:
    output.remove("green")

print(output)
