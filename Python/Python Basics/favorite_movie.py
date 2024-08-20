i=1
biggest=""
biggestp=0
current=0
length=0

while True:
    film = input()
    if film=="STOP":
        print(f"The best movie for you is {biggest} with {biggestp} ASCII sum.")
        break
    if i == 7 :
        print("The limit is reached.")
        print(f"The best movie for you is {biggest} with {biggestp} ASCII sum.")
        break



    for ii in range(0, len(film)):
        current+=ord(film[ii])
        length+=1
    for iii in range(0, len(film)):
        if film[iii].isupper():
            current-=length
        elif film[iii].islower():
            current -= length*2
    if current>biggestp:
        biggestp=current
        biggest=film

    i += 1
    length=0
    current=0
