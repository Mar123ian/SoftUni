from collections import deque

price =int(input())
size =int(input())
bullets =list(map(int,input().split()))
locks =deque(list(map(int,input().split())))
value =int(input())

bullet_number=0
total_bullets=0
total_locks=len(list(locks))
destroyed=0


while bullets and locks:

    lock=locks.popleft()
    while bullets:
        bullet=bullets.pop()

        if lock>=bullet:
            print("Bang!")
            bullet_number+=1
            total_bullets+=1
            destroyed+=1
            if bullet_number==size and bullets:
                print("Reloading!")
                bullet_number=0
            break
        else:
            print("Ping!")
            bullet_number+=1
            total_bullets+=1
            if bullet_number==size and bullets:
                print("Reloading!")
                bullet_number=0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${value-price*total_bullets}" )

else:
    print(f"Couldn't get through. Locks left: {total_locks-destroyed}")

