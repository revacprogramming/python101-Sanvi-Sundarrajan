# Loops & Iterators

def comparision():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done": 
            break
        try:
            num = int(num)
            if largest is None or largest < num:
                largest = num
            if smallest is None or smallest > num: 
                smallest = num
        except:
            print ("Invalid input")
            continue
    maximum=largest
		minimum=smallest
return maximum,minimum
def output(max,min):
	print("Maximum and minimum are"max,min)


def main():
    max,min=comparision()    


main()
#used try and except keywords