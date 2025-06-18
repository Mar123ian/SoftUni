import re

pattern=r"-|,|\.|!|\?"

with open("text.txt") as file:
	
	lines=re.sub(pattern,"@",file.read()).split("\n")	
	matrix_lines_and_words=[" ".join(line.split()[::-1]) for line in lines]

	print(*matrix_lines_and_words[::2],sep="\n")
	
