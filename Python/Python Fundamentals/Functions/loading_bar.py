n=int(input())

def loading_bar(n):
    bar=[]
    percent=n
    if n!=0:
        n=int(n/10)
    for _ in range(n):
        bar.append("%")
    for _ in range(10-n):
        bar.append(".")

    if percent!=100:
        bar=f'{percent}% [{"".join(bar)}]\nStill loading...'
    else:
        bar=f'{percent}% Complete!\n[{"".join(bar)}]'
    return bar

print(loading_bar(n))
