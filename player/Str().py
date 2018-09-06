st=input("Enter the brackets:")
ab=[]
if st[0]==')' or st[len(st1)-1]=='(':
	print("Not valid")
elif st.count('(')!=st.count(')'):
      print("Not valid")
else:
    l=len(st)
    for x in range(l):
        if st[x]=='(':
            ab.append(st[x])
        elif st[x]==')' and len(ab)!=0:
            if ab[len(ab)-1]=='(':
                ab.pop()
    if len(ab)==0:
        print("Valid")
    else:
        print("Invalid")
