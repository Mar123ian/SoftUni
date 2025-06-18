users={}
messages=[]
sides={}

while True:
    command=input()
    
    if command=="Lumpawaroo":
        break
    
    new=command.split(" | ")
    change=command.split(" -> ")
    
    if len(new)==2:
        force_side=new[0]
        force_user=new[1]

        if force_user not in users.keys():
            users[force_user]=force_side
        
        if force_user in users.keys():
            pass
 
 
 
    if len(change)==2:
        force_user=change[0]
        force_side=change[1]
        
        if force_user in users.keys():
            del users[force_user]
            users[force_user]=force_side
            
        if force_user not in users.keys():
            users[force_user]=force_side
            
        messages.append(f"{force_user} joins the {force_side} side!")

for item in messages:
    print(item)
    
for v in users.values():
    sides[v]=0



for item in sides:
    for v in users.values():
        if v==item:
            sides[v]+=1
            
for k,v in sides.items():
    print(f"Side: {k}, Members: {v}")
    for key in users.keys():
        if users[key]==k:
            print(f"! {key}")

    
    
