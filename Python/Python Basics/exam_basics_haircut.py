c=int(input())
p=0

while True:
    com=str(input())
    if com=="haircut":
        com=str(input())
        if com=="ladies":
            p+=20
        elif com=="mens":
            p+=15
        elif com=="kids":
            p+=10

    elif com=="color":
        com=str(input())
        if com=="touch up":
            p+=20
        elif com=="full color":
            p+=30

    elif com=="closed":
        if p>=c:
            print("You have reached your target for the day!")
        else:
            print(f"Target not reached! You need {c-p}lv. more.")
        print(f"Earned money: {p}lv.")
        break

    if p >= c:
        print("You have reached your target for the day!")
        print(f"Earned money: {p}lv.")
        break
