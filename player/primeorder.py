def anagram(str1,str2):
	str1.sort()
	str2.sort()
	a=''.join(str1)
	t=''.join(str2)
	if a==t:
		return True
	return False

def main():
	(l1,l2)=([],[])
	s1=input()
	a=input()
	l1=list(s1)
	l2=list(a)
	l1.sort()
	l2.sort()
	print(anagram(l1,l2))
  
main()  
