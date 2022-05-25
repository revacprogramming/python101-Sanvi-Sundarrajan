# Tuples
filename = "dataset/mbox-short.txt"
filehandle=open(filename)
counts{}


for line in filehandle:
	if line.startswith("From "):
		time=line.split()[5].split[":"]
		counts [time] = counts.get(time, 0) + 1


