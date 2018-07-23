def mul(n1,n2):
	mul=int(n1)*int(n2)
	return(str(mul))

def main():
	try:
		i=input()
		j=input()
		print(mul(i,j))
	except:
		print('invalid')
main()
