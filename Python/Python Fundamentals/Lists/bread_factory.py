lst=input().split("|")
energy=100
coins=100
managed=True

for i in lst:
    i=i.split("-")
    event=i[0]
    number=int(i[1])
    if event=="rest":
        ce=energy
        energy+=number
        if energy>100:
            number=100-ce
            energy=100
            
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event=="order":
        
        if energy>=30:
            energy-=30
            coins+=number
            print(f"You earned {number} coins.")
        else:
            energy+=50
            if energy>100:
                energy=100
            print("You had to rest!")
    else:
        if number<=coins:
            coins-=number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            managed=False
            break
if(managed):
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")