

def get_cs():
	cs = input("Enter the the string ")
	return cs


def cs_to_dict(cs):
	splt1 = cs.split(';')                   
	for i in splt1:
		splt2=i.split('=')
	#for i in splt2:
		#for i in range(0, len(splt2)):
			#d={splt2[i] : splt2[i + 1]}
	d_= iter(splt2)
	d = dict(zip(d,d)) 
	return d 


def dict_to_cs(d):
    """convert a dictionary to connect string"""


def main():
  cs = get_cs()

  d = cs_to_dict(cs) # convert connect string to a dictionary
  print(d)

  cs = dict_to_cs(d)
  print(cs)


if __name__ == '__main__':
  main()
