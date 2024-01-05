a,b,c=map(int,input().split())
k=(c-a)/(a-b)+1
if k%1==0:
    k=int(k)
    print(k)
else:
    k=int(k)
    print(k+1)