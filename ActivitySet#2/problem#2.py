
def add(a, b):
    c = float(a)+float(b) 
    return c
def output(a, b, sum_):
  print("The sum of ",a ,"and", b ,"is",sum_)  


def main():
    a, b = input_two_numbers()
    sum_ = add(a, b)
		output(a, b, sum)

if __name__ == '__main__':
    main()

