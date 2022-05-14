# Lists
fname = "dataset/romeo.txt"
fhand=open(fname)
mylist=list()
for line in fhand:
    l=line.split()
    for i in l:
    	if i not in l:
        	mylist.append(i)
mylist.sort()
print(mylist)
    
    