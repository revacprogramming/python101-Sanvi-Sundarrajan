# Conditional Execution
def computation():
	hours=input("Enter Hours:")
	h=float(hours)
	rate= input("Enter the Rate:")
	r=float(rate)
	if h <= 40:
	 	print(h*r)
	elif h > 40:
		print(40*r+(h-40)*1.5*r)
def main():
	computation()
main()	
