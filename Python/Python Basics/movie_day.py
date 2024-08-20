time=int(input())
scenes=int(input())
timesc=int(input())
final=abs(time-scenes*timesc-0.15*time)
finall=f"{final:.0f}"
if scenes*timesc+0.15*time<=time:
    print(f"You managed to finish the movie on time! You have {finall} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {finall} minutes.")
