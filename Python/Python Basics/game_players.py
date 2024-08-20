k=int(input())
l=int(input())
m=int(input())
n=int(input())
valid=0

for i in range(k,9):
    for ii in range(9,l-1,-1):
        for iii in range(m,9):
            for iiii in range(9,n-1,-1):              
                if i%2==0 and iii%2==0 and ii%2!=0 and iiii%2!=0:                    
                    if i==iii and ii==iiii:
                        print("Cannot change the same player.")
                    else:
                        print(f"{i}{ii} - {iii}{iiii}")
                        valid+=1


                if valid >= 6:
                    break
            if valid >= 6:
                break
        if valid >= 6:
            break                
    if valid>=6:
        break
