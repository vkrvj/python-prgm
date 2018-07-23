w=list(input())
for i in range(len(w)):
    if w[i].islower():
        w[i]=w[i].upper()
    else:
        w[i]=w[i].lower()
print("".join(str(x) for x in w))
