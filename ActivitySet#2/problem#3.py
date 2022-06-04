

def get_cs():
  cs=input("Enter the string :")
  return cs


def cs_to_lot(cs):
  lst=[]
  splt1=cs.split(';')
  for i in splt1:
    splt2=i.split('=')
    lt.append((splt2[0],splt2[1]))


def main():
  cs = get_cs()
  lot = cs_to_lot(cs)
  print(lot)


if __name__ == '__main__':
  main()
