l=list(map(int, input().split(' ')))
c=l[:2]
a=l[2:4]
b=l[4:6]
res=((b[0] - a[0]) * (c[1]- a[1])) - ((c[0] - a[0]) * (b[1] - a[1]))
# print(res)
if res==0:
    if a[0]!=b[0]:
        if a[0] <= c[0] <= b[0] or b[0] <= c[0] <= a[0]:
            print('YES')
        else:
            print('NO')
    else:
        if a[1] <= c[1] <= b[1] or b[1] <= c[1] <= a[1]:
            print('YES')
        else:
            print('NO')
else:
    print("NO")
