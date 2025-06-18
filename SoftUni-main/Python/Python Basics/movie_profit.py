text=str(input())
days=int(input())
tickets=int(input())
price=float(input())
percent=int(input())
allpp=float((days*tickets*price)*percent/100)
allp=float((days*tickets*price)-allpp)
final=f"{allp:.2f}"
print(f"The profit from the movie {text} is {final} lv.")
