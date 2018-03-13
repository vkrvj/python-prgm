try :
	x=raw_input("time (hh:mm) : ")
	y=raw_input("time (hh:mm) : ")
	z=0
	a=x.split(':')
	b=y.split(':')
	c=int(a[0])*60+int(a[1])
	d=int(b[0])*60+int(b[1])
	if(c>d):
		z=c-d
	else:
		z=d-c
	print z
except :
	print "Invalid"
