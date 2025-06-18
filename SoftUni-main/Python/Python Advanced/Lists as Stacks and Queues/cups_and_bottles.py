from collections import deque

cups=deque(list(map(int,input().split(" "))))
bottles=list(map(int,input().split(" ")))
wasted=0

while bottles and cups:
    bottle=bottles.pop()
    cup=cups.popleft()

    cup=cup-bottle

    if cup<0:
        wasted+=cup

    if cup>0:
        
    
        while cup>0:
            bottle=bottles.pop()
            cup=cup-bottle
        if cup<0:
            wasted+=cup

if bottles:
    print("Bottles: ", end="")
    print(" ".join(list(map(str,bottles))))
if cups:
    print("Cups: ", end="")
    print(" ".join(list(map(str,cups))))

print(f"Wasted litters of water: {abs(wasted)}")




