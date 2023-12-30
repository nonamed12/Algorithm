x = []
for i in range(0,5):
    x.append([])
    a = input() 
    l = len(a)
    for k in range(0,l):
        x[i].append(a[k])
    for z in range(l,15):
        x[i].append('')
z = ''
for i in range(0,15):
    z += x[0][i] + x[1][i] + x[2][i] + x[3][i] + x[4][i]
print(z)