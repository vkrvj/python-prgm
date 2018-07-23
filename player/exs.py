def play_26():
	t=input()
	a=""
	p=" "
	for i in t :
		if not (p==" " and i==p ):
			a+=i
		p=i
	print(a)
  
play_26()
