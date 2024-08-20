dm=float(input())
sm=float(input())
minuses=float(input())
price=float(input())
all=5*dm+5*sm-minuses
a=price-all
if price<=all:
    print(f"Profit: {all:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {a:.2f} BGN.")
