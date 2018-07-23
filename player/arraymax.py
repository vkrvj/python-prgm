def main():
    n,k=map(int,input().split())
    a=[]
    a=list(map(int,input().split()))
    k=map(int,input().split())
    for i in k:
        if i not in a:
            a.append(i)
    print(n,len(a))

if __name__ == '__main__':
    main()
