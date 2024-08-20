a=int(input())
b=int(input())
 
def factoriel(num):
    result=1
    for i in range(1,num):
        result*=i+1
    return result

result =(factoriel(a)/factoriel(b))
print(f"{result:.2f}")
