lst=[int(input()) for _ in range(3)]
result=""

negative_count=len(list(filter(lambda item: item<0,lst)))
positive_count=len(list(filter(lambda item: item>0,lst)))

if positive_count==3:
    result="positive"
elif negative_count==3:
    result="negative"
elif 0 in lst:
    result="zero"
elif positive_count>negative_count:
    result="negative"
elif positive_count<negative_count:
    result="positive"


print(result)
