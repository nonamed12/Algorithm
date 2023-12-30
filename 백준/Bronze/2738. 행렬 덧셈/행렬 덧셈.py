n, m = map(int, input().split())
a_list, b_list = [], []
for i in range(n):
    a = list(map(int, input().split()))
    a_list.append(a)
for i in range(n):
    b = list(map(int, input().split()))
    b_list.append(b)
for i in range(n):
    for j in range(m):
        print(a_list[i][j] + b_list[i][j], end=' ')
    print()