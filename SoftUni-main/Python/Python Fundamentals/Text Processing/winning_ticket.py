input=input().split(", ")
winning_sumb=['@', '#', '$', '^' ]
def check_ticket(ticket):
    ticket=ticket.strip()
    if len(ticket)!=20:
        return "invalid ticket"
    
    for sumb in winning_sumb:
        if sumb*20==ticket:
            return f'ticket "{ticket}" - 10{sumb} Jackpot!'
        
    first, second=ticket[0:10], ticket[10:21]
    
    for sumb in winning_sumb:
        sumbols=0
        for i in range(6,20):
            if first.count(sumb*i)==1 and second.count(sumb*i)==1:
                sumbols=i
        if first.count(sumb*sumbols)==1 and second.count(sumb*sumbols)==1:
            return f'ticket "{ticket}" - {sumbols}{sumb}'
        
    return f'ticket "{ticket}" - no match'
    
    
   
    
for item in input:
    print(check_ticket(item))
