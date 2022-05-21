# Files
# Use the file name mbox-short.txt as the file name
def filehandle(fname):
	fhand = open(fname)
	count = 0
	average = 0
	for line in fhand:
	    line=line.rstrip()
	    if not line.startswith("X-DSPAM-Confidence:") : 
	        continue
	    average += float(line[20:])
	    count = count + 1
	final=average/count
	return final


def output(final):		
	print("Average spam confidence:", final)


def main():
	fname = input("Enter file name: ")
	final=filehandle(fname)
	output(final)


main()	
