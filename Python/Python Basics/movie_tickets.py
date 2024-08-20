a1=int(input())
a2=int(input())
n=int(input())
askii=a1
s2=1
s2f=1
s3=1
s3f=1
s4=askii
for i in range(askii,a2):
    for ii in range(s2,n):
        for iii in range(s3,n // 2):
            if askii%2!=0 and (s2+s3+askii)%2!=0:
                    print(f"{chr(askii)}-{s2}{s3}{askii}")

            s3 += 1
        s2 += 1
        s3 = s3f
    askii+=1
    s2=s2f
    s3=s3f
