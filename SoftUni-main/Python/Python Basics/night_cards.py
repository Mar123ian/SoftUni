people=int(input())
nights=int(input())
cards=int(input())
tickets=int(input())


all=(1.25*(people*(nights*20+cards*1.6+tickets*6)))
print(f"{all:.2f}")
