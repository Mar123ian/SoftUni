
records={}
subm={}

def print_results():
    print("Results:")
    
    for k,v in records.items():
        print(f"{k} | {v}")
    print("Submissions:")
    for k,v in subm.items():
        print(f"{k} - {v}")
    
def ban(name):
    name=name
    del records[name]
    
    
def add(command):
    command=command.split("-")
    
    name, lang, points=command[0], command[1], command[2]
    
    if lang not in subm.keys():
        subm[lang]=1
    else:
        subm[lang]+=1
    
    if name not in records.keys():
        records[name]=0
    if name in records.keys() and int(points)>int(records[name]):
        
        records[name]=points
while True:
    command=input()
    if command=="exam finished":
        print_results()
        break
    elif len(command.split("-"))==2:
        name=command.split("-")[0]
        ban(name)
    elif len(command.split("-"))==3:
        add(command)
    

    
        
    
