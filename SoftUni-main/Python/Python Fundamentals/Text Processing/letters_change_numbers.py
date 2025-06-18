import re

alp="abcdefghijklmnopqrstuvwxyz"

input=input()
pattern=r"(\w)(\d+)(\w)"

commands=re.finditer(pattern, input)
total=0

def calculate(f_letter,num,s_letter, f_letter_pos, s_letter_pos):
    result=0
    if f_letter.isupper():
        result=num/f_letter_pos
    else:
        result=num*f_letter_pos
        
    if s_letter.isupper():
        result-=s_letter_pos
    else:
        result+=s_letter_pos
        
    return result
for command in commands:
    f_letter=command.group(1)
    num=int(command.group(2))
    s_letter=command.group(3)
    f_letter_pos=alp.index(f_letter.lower())+1
    s_letter_pos=alp.index(s_letter.lower())+1
    
    total+=calculate(f_letter,num,s_letter, f_letter_pos, s_letter_pos)

print(f"{total:.2f}")
