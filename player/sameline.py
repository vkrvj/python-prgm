 def play_21():
	a,b=[],[]
	for i in range(3):
		a.append(int(input('Enter a'+str(i))))
		b.append(int(input('Enter b'+str(i))))
	if ((b[1]-y[0]) * (a[2]-x[1])) == ((b[2]-y[1]) * (a[1]-x[0])) :
		print ('Yes')
	else :
		print('No')
play_21()
