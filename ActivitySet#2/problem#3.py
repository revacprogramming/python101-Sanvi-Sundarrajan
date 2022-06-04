

def get_cs():
  cs=input("Enter the string :")
  return cs


def cs_to_lot(cs):
  lst=[]
  x=cs.split(';')
  for i in x:
    y=i.split('=')
    lt.append((y[0],y[1]))


def main():
  cs = get_cs()
  lot = cs_to_lot(cs)
  print(lot)


if __name__ == '__main__':
  main()
