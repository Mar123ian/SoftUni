def a(n, arr):
    if n >= len(arr):
        print(*arr)
        return
    for i in range(1, len(arr) + 1):
        arr[n] = i
        a(n + 1, arr)


n = int(input())
arr = [0] * n
a(0, arr)
