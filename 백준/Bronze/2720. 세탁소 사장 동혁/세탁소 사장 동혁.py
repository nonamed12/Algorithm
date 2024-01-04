N = int(input())
def change(money):
    lst = [25, 10, 5, 1]
    for s in lst:
        print(money//s, end = ' ')
        money = money%s
    return print()
for i in range(N):
    change(int(input()))