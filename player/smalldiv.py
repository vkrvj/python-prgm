def ip(string):
	a=0
	r=[]
	l=list(string)
	for i in range(len(l)):
		if a==3:
			a=0
			r.append('.')
		r.append(l[i])
		a+=1
	return(''.join(r))
	
 def f():
	fin=[]
	st=input('Enter your address:\n')
	str=list(st)
	str.insert(3,".")
	str.insert(7,".")
	str.insert(10,".")
	fin.append( (''.join(str)))
	fin.append(ip(st))
	print(fin)
	
f()
