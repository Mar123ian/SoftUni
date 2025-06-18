def find_paths(l, r,c,unique_paths):
	
	if r<0 or c<0 or r>len(l)-1 or c>len(l[0])-1 or l[r][c]=="#":
		return unique_paths
	
	if r==len(l)-1 and c==len(l[0])-1:				
		return unique_paths+1
		
	else:
		l[r][c]="#"
		
		unique_paths=find_paths(l,r+1,c,unique_paths)		
		unique_paths=find_paths(l,r,c+1,unique_paths)
		
		l[r][c]="0"
		
	return unique_paths
				
m=int(input())
n=int(input())

l=[[0 for i in range(n)] for j in range(m)]

print(find_paths(l,0,0,0))
