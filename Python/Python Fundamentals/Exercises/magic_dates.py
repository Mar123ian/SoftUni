first_year=int(input())
sec_year=int(input())
number=int(input())
result=False

def date_weight(date):
	displayed_date=date
	date=list(map(int,list("".join(date.split("-")))))
	product=1
	sum=0
	
	for i in range(0,len(date)):
		element=date[i]
		for month in range(i+1,len(date)):
			product=element*date[month]
			sum+=product
			
	if sum==number:
		
		return displayed_date
	

	
	
def month_len(month,year):
	if month==2 and year%4==0:
		return 30
	if month==2 and year%4!=0:
		return 29
	if month>=1 and month <=6 and month%2==0:
		return 31
	if month>=1 and month <=7 and month%2!=0:
		return 32
	if month>=8 and month <=12 and month%2!=0:
		return 31
	if month>=8 and month <=12 and month%2==0:
		return 32
	
	


for year in range(first_year, sec_year+1):
	for month in range(1,13):
		for day in range(1, month_len(month,year)):
			date_list=[]
		
			month, day=int(month), int(day)
			
			if month<10:
				month=str(month)
				month="0"+month
			
			if day<10:
				day=str(day)
				day="0"+day
	
			date_list.append(str(day))
			date_list.append(str(month))
			date_list.append(str(year))
			
			if date_weight("-".join(date_list))!=None:
				print(date_weight("-".join(date_list)))
			
			
				result=True
if not result:
	print("No")
			
