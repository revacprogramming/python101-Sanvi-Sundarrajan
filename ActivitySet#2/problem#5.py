

def get_cs():
	cs = input("Enter the the string ")
	return cs


def cs_to_dict(cs):
	d={}
	splt1 = cs.split(';') 
	for i in splt1:
		splt2=i.split('=')
		d[splt2[0]]=splt2[1]
	return d 	
	'''d_= iter(splt2)
	d = dict(zip(d,d)) # zip method 
	return d'''    


def dict_to_cs(d): 
	cs=str()
	for i in d:
		cs = cs+(i+"="+d[i]+";")
	return cs

def main():
  cs = get_cs()

  d = cs_to_dict(cs) # convert connect string to a dictionary
  print(d)

  cs = dict_to_cs(d)
  print(cs)


if __name__ == '__main__':
  main()

#for my reference to understand logic 
'''Enter the the string system=s;database=d;username=u;password=p
['system', 's']
{'system': 's'}
['database', 'd']
{'system': 's', 'database': 'd'}
['username', 'u']
{'system': 's', 'database': 'd', 'username': 'u'}
['password', 'p']
{'system': 's', 'database': 'd', 'username': 'u', 'password': 'p'}
{'system': 's', 'database': 'd', 'username': 'u', 'password': 'p'}
system=s;database=d;username=u;password=p;'''

