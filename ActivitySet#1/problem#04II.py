# Conditional Execution(II)
def scores():
	score = input("Enter Score: ")
	s =  float(score)
	x = "NULL"
	if s >= 0.9:
		x = 'A'
	elif s >=0.8:
		x='B'
	elif s >=0.7:
		x='C'
	elif s >= 0.6:
		x='D'
	elif s < 0.6:
		x ='F'
	else:
		x ="Out of Range"
	print (x) 
def main():
	scores()
main()
