n=int(input())
a=[]
for i in range(n):
    a.append(input())
a = sorted(a, key=lambda x: len(x))

res=[]
for i in range(n-1):
    if a[i] in a[i+1]:
        res.append(a[i])
    else:
        break
if len(res)==n-1:
    print('YES')
    res.append(a[-1])
    print(*res, sep='\n')
else:
    print('NO')
