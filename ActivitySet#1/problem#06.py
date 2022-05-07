# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break
	print (num)
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
             smallest = num 
        print(num)        
    else:
    	print('Invalid input')
    

print("Maximum", largest)
print("Minimum",smallest)

