# Files
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fhand = open(fname)
count = 0
average = 0
for line in fhand:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    average += float(line[20:])
    count = count + 1
    
print("Average spam confidence:", (average/count))