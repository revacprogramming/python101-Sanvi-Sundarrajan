

def get_cs():
    
	cs=input("Enter a string")
	return cs

def cs_to_lot(cs):
  lot=cs.split()
		return lot

def lot_to_cs(lot):
  return ''.join(lot)


def main():
  cs=get_cs()

  lot=cs_to_lot(cs)  # convert connect string to list of tuples
  print(lot)

  cs=lot_to_cs(lot)  # convert list of strings to connect string
  print(cs)


if __name__ == '__main__':
  main()
