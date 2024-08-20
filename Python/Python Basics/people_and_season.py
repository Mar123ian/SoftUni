people=int(input())
season=input()
all=0

if season=="spring" and people<=5:
    all=50*people
if season=="summer" and people<=5:
    all=0.85*48.5*people
if season=="autumn" and people<=5:
    all=60*people
if season=="winter" and people<=5:
    all=1.08*86*people
if season=="spring" and people>5:
    all=48*people
if season=="summer" and people>5:
    all=0.85*45*people
if season=="autumn" and people>5:
    all=49.50*people
if season=="winter" and people>5:
    all=1.08*85*people
   
print(f"{all:.2f} leva.")
