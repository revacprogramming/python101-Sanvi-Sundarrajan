# Regular Expressions
# https://www.py4e.com/lessons/regex
# Regular Expressions
# https://www.py4e.com/lessons/regex
'''Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
'''
# You will extract all the numbers in the file and compute the sum of the numbers.
import re
count = 0
sum_ = 0
#with open('dataset/regex.txt','r') as f: 
f = open('dataset/regex.txt')
f=f.read()
numbers = re.findall('[0-9]+',f)
for n in numbers:
	number = float(n) 
	count = count + 1
	sum_ += number
print(count)
print(sum_)# sum is not correct 
