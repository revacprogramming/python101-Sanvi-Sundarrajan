

class Menu:
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def __add__(self,o):
		return self.name + o.name, self.price + o.price

m = Menu()
m = m + ("idly", 10) + ("vada", 20)  # Hint: operator overloading special methods (__add__, __sub__, etc.)

print(m)  # should print the menu properly
