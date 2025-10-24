def a(arr, i):
    if i == len(arr) // 2:
        print(*arr)
        return
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    a(arr, i + 1)


arr = input().split()
a(arr, 0)
