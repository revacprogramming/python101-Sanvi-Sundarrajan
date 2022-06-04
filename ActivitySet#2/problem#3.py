

def get_cs():
  cs=input("Enter the string :")
  return cs


def cs_to_lot(cs):
  lst1=[]
  splt1=cs.split(';')
  for i in splt1:
    splt2=i.split('=')
    lst1.append((splt2[0],splt2[1]))#appending tuple to list 
	return lst

def main():
  lst2=[]
    for a in lot:
      lst2.append("=".join(a))
    return(";".join(lst2))


if __name__ == '__main__':
  main()
