def play_22():
	a=int(input())
	b=int(input())
	while(a!=b):
		if a>b:
			a-=b
		else :
			b-=a
	print(a)
play_22()
