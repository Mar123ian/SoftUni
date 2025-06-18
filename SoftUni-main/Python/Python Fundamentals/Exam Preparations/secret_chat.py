word=input()

while True:
    com=input()
    
    if com=="Reveal":
        break
    else:
        com=com.split(":|:")
    
    if com[0]== "InsertSpace":
        word=word[:int(com[1])] + " " + word[int(com[1]):]
        print(word)
        
    if com[0]== "Reverse":
        if com[1] in word:
            word=word.replace(com[1],"",1)
            word+=com[1][::-1]
            print(word)
        else:
            print("error")
            
    if com[0]== "ChangeAll":
        old_str=com[1]
        new_str=com[2]
        word=word.replace(old_str, new_str)
        print(word)
        
print(f"You have a new text message: {word}")
