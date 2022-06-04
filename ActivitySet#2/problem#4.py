

def get_cs():
  cs=input("Enter a string")
  return cs

def cs_to_lot(cs):
  lst1=[]
  splt1=cs.split(';')
  for i in splt1:
    splt2=i.split('=')
    lst1.append((splt2[0],splt2[1]))#appending tuple to list 
	return lst


def lot_to_cs(lot):
  lst2=[]
  for a in lot:
  	lst2.append("=".join(a))
	return(";".join(lst2))


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
  main()
