from copy import deepcopy

def possible_permutations(lst):
    result=[]
    length=len(lst)

    def a(lst, o):

        if len(o)>=length:
            result.append(list(o))
            return

        for i in lst:
            o.append(i)
            new=deepcopy(lst)
            new.remove(i)
            a(new,o)
            o.pop()

    a(lst, [])
    for el in result:
        yield el





[print(n) for n in possible_permutations([1, 2, 3])]
