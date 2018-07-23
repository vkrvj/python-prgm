def lastjump(l,n):
	a=0
	while a<n:
		a+=l[a]
		try:
			if a==l[a]:
				return True
		except:
			return False
      
def main():
	l=[]
	n=int(input())
	for a in range(n):
		l.append(int(input()))
	print(lastjump(l,n))

main()
