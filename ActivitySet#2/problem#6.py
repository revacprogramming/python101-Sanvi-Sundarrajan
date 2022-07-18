

class Menu:
	def add (self,name,price):
		self.name = name
		self.price = price
	def show (self):
		print(self.name,self.price)
		


m = Menu()  # Menu is a class
m.add("idly", 10)
m.show()
m.add("vada", 20)
m.show()
