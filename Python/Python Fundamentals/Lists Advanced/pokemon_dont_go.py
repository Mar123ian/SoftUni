lst=(input()).split()
lst=list(map(int,lst))
result=0

while lst:
    index=int(input())
    
    if index<0:
        el=lst.pop(0)
        lst.insert(0,lst[-1])
    elif index>len(lst)-1:
        el=lst.pop(-1)
        lst.append(lst[0])
    else:
        el=lst.pop(index)
    
    lst=list(map(lambda x: x+el  if x<=el else x-el,lst))
    result+=el
print(result)
