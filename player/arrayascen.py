 def play_25():
	a=int(input())
	b=[]
	for i in range(a):
		b.append(input('Enter :'))
	for i in range(a):
		p=i
		for j in range(i+1,a):
			if b[p]>l[j] and len(b[p])==len(b[j]):
				p=j
		if p!=i:
			t=l[i]
			b[i]=b[p]
			b[p]=t
	print(*b)
  
play_25()
