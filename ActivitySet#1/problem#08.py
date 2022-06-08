# Files
# Use the file name mbox-short.txt as the file name
def averagespam(fname):
	fhand = open(fname)
	count = 0
	average = 0
	for line in fhand:
	    line=line.rstrip()
	    if not line.startswith("X-DSPAM-Confidence:") : 
	        continue
	    total += float(line[20:])
	    count = count + 1
	average=total/count
	return average


def output(average):		
	print("Average spam confidence:", average)


def main():
	fname = input("Enter file name: ")
	average=filehandle(fname)
	output(average)


main()	
# use with to open files