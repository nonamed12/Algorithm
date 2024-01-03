a, n = map(int, input().split())
lst = []
q = a
while q != 0:
    r = q % n
    q = q // n
    if r<10:
        lst.append(str(r))
    else:
        lst.append(chr(r+55))
[print(s, end='') for s in lst[::-1]]