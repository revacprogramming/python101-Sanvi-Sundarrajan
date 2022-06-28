import re
count = 0
fhand = open('dataset/regex.txt')

	numbers = re.findall('[0-9]+',f)
for n in numbers:
	number = float(n) 
	count = count + number
print(count)