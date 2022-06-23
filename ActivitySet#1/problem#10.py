# Dictionaries
def myinput():
	filename = "dataset/mbox-short.txt"
	return filename
def emailcount(filename):
	filehandle =open(filename)
	count={}
	
	for line in filehandle :
		if line.startswith("From "):
			email=line.split()[1]
			count[email]=count.get(email,0)+1
	max_count=0
	max_emails=0
	for email in count:
		if count[email]>max_count:
			max_count=count[email]
			max_emails=email
	return max_count,max_emails
def output(max_count,max_emails):	
	print(max_emails,max_count)			 		

def main():
	filename=myinput()
	max_emails,max_count=emailcount(filename)
	output(max_count,max_emails)
main()