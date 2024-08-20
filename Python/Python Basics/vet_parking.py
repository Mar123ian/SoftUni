days=int(input())
hours=int(input())
total=0
totald=0

for i in range(1,days+1):
    for ii in range(1,hours+1):
        if i%2==0 and ii%2!=0:
            totald+=2.5
        elif i%2!=0 and ii%2==0:
            totald+=1.25
        else:
            totald+=1
    total+=totald
    print(f"Day: {i} - {totald:.2f} leva")
    totald=0
print(f"Total: {total:.2f} leva")
