shedule=input().split(", ")
command=""
def add(title):
    if title not in shedule:
        shedule.append(title)

def insert(title, index):
    if title not in shedule:
        shedule.insert(int(index),title) 

def remove(title):
    index=shedule.index(title)
    
    if shedule[index]!=shedule[-1]:
        if title in shedule and shedule[index+1].split("-")[0]==title:
            ex=shedule[index+1]
            shedule.remove(title)
            shedule.remove(ex)
    if title in shedule:
        shedule.remove(title)

def swap(title, sec_title):
    if title in shedule and sec_title in shedule:
    	ex1=""
    	ex2=""
    	if f"{title}-Exercise" in shedule:
        	ex1=f"{title}-Exercise"
        	shedule.remove(ex1)
    	if f"{sec_title}-Exercise" in shedule:
        	ex2=f"{sec_title}-Exercise"
        	shedule.remove(ex2)

    
    	index=shedule.index(title)
    	index2=shedule.index(sec_title)
    
    	shedule[index],shedule[index2]=shedule[index2],shedule[index]
    	index=shedule.index(title)
    	index2=shedule.index(sec_title)
    	if ex1!="":
        	shedule.insert(index+1,ex1)
   

    	if ex2!="":
        	shedule.insert(index2+1,ex2)
  
    
def exercise(title):
    
    if title in shedule:
        lesson_index=shedule.index(title)
        if shedule[lesson_index]!=shedule[-1]:
            if title in shedule and shedule[lesson_index+1].split("-")[0]!=title:
                shedule.insert(lesson_index+1,f"{title}-Exercise")
        else:
            shedule.append(f"{title}-Exercise")
    if title not in shedule:
        shedule.append(title)
        shedule.append(f"{title}-Exercise")


while True:
    command=input()  
    if command=="course start":
        break
    event=command.split(":")[0]
    title=command.split(":")[1]
    if len(command.split(":"))==3:
        sec_criteria=command.split(":")[2]
    
    choices={
        "add":lambda: add(title),
        "insert":lambda: insert(title, sec_criteria),
        "remove":lambda: remove(title),
        "swap":lambda: swap(title, sec_criteria),
        "exercise":lambda: exercise(title)
    }.get(event.lower())
    choices()

for i in shedule:
    print(f"{shedule.index(i)+1}.{i}")
