# Conditional Execution(II)
def myinput():
    score = float(input("Enter Score: "))
    return score

	
def scores(s):
    if s>1:
        return 'Out of range'
    elif s<0:
        return 'Score cannot be negative'
    elif s>=0.9:
        return 'A'
    elif s>=0.8:
        return 'B'
    elif s>=0.7:
        return 'C'
    elif s>=0.6:
        return 'D'
    elif s<0.6:
        return 'F'

			
def output(res): 
	print(res)	

	
def main():
    s=myinput()
    res=scores(s)
    output(res)


main()
