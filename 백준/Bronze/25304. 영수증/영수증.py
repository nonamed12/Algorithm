a=int(input())
b=int(input())
for i in range(b):
    c,d=map(int,input().split())
    a-=c*d
if a == 0:
    print('Yes')
else:
    print('No')