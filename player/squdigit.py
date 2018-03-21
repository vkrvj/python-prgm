def sumdigsqr(n):
	sum=0
	while(a!=0):
		b=a%10
		sum+=b*b
		a//=10
	return sum
def happy(a):
	while(a>0):
		a=sumdigsqr(n)
		if a==1:
			print('happy number')
			return
	print('not happy number')
def main():
	try:
		a=int(input())
		happy(a)
	except:
		print('invalid')
main()
