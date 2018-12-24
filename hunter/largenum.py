def f(a):
	a.sort(reverse=True)
	x=''
	y=0
	new=''
	for i in a:
		x+=str(i)
		y+=1
	print(x)
	y=0
	for i in range(len(x)-1,-1,-1):
		if y==3:
			y=0
			new+=','
		new+=x[i]
		y=y+1
	print(new[::-1])
	
def main():
	try:
		n=int(input())
		a=[]
		for i in range(n):
			l.append(int(input()))
		f(a)
	except:
		print('invalid')
main()
