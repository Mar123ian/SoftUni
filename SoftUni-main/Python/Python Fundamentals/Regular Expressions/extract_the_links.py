import re
output=[]

text=input()
while text:
    
    regex=r"(www\.)([a-zA-Z0-9-]+)(\.[a-z]+){1,}"
    matches=re.finditer(regex, text)

    for match in matches:
        output.append(match.group())
    text=input()
print("\n".join(output))
