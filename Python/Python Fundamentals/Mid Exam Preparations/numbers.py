lst = [int(el) for el in input().split()]
lst = list(filter(lambda a: a > sum(lst) / len(lst), sorted(lst, reverse=True)))
print(*lst[:5]) if lst else print("No")
