N,M=map(int,input().split())
basket=[]
for i in range(1,N+1):
    basket.append(i)
for i in range(M):
    i,j=map(int,input().split())
    temp=basket[i-1:j]
    temp.reverse()
    basket[i-1:j]=temp
for i in range(N):
    print(basket[i],end=' ')