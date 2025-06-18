n=int(input())
s=0
r=0
v=0
op=0
opr=0
rrr=0
for i in range(n):
    r=int(input())
    rr=r
    if r<100:
        v=r//10
        r=r-v*10
    else:
        v=r//100
        r=r-v*100
        v=r//10
        r=r-v*10
    s=rr//10

    if r==2:
        op=0*s
    if r==3:
        op=0.5*s
    if r==4:
        op=0.7*s
    if r==5:
        op=0.85*s
    if r==6:
        op=s
    opr+=op
    rrr+=r
rrrr=rrr/n

print(f"{opr:.2f}")
print(f"{rrrr:.2f}")
