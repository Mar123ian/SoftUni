from collections import deque


class Edge:

    def __init__(self, first, sec, weight):
        self.first = first
        self.sec = sec
        self.weight = int(weight)


def print_output(stop, distance, parent):
    output = deque()
    node = stop
    distantion = distance[node]
    while node != None:
        output.appendleft(node)
        node = parent[node]
    print(*output)
    print(distantion)


m = int(input())
n = int(input())
graph = []
distance = {}
parent = {}

for i in range(n):
    first, sec, weight = input().split()

    parent[first] = None
    distance[first] = float("inf")
    distance[sec] = float("inf")
    parent[sec] = None
    graph.append((Edge(first, sec, weight)))

start = input()
stop = input()
distance[start] = 0

for _ in range(n - 1):
    isready = True
    for edge in graph:
        dist = edge.weight + distance[edge.first]

        if dist < distance[edge.sec]:
            distance[edge.sec] = dist
            parent[edge.sec] = edge.first
            isready = False
    if isready:
        break

if not isready:
    for edge in graph:
        dist = edge.weight + distance[edge.first]
        if dist < distance[edge.sec]:
            print("Undefined")
            break
    else:
        print_output(stop, distance, parent)

else:
    print_output(stop, distance, parent)
