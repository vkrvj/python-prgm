def remvowels(string):
	m=len(string)
	outstr=''
	v=['a','e','i','o','u','A','E','I','O','U']
	for i in range(m):
		if string[i] in v:
			continue
		outstr+=string[i]
	print(outstr)

def main():
	try:
		str=input()
		remvowels(str)
	except:
		print('invalid')
main()
