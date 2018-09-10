def findrepn(lin):
	lin.sort()
	rept=[]
	n=len(lin)
	for i in range(1,n):
			if lin[i]==lin[i-1] :
				if lin[i] in rept :
					continue
				rept.append(lin[i])
	print(rept)

def main():
	try:
		lin=[]
		n=int(input())
		for i in range(n):
			lin.append(int(input()))
		findrepn(li)
	except:
		print('invalid')

main()
