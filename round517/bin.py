from collections import defaultdict
d=defaultdict(list)

for i in range(4):
    for j in range(4):
        d[(i|j,i&j)].append((i,j))
# for k in d:
#     print(k,d[k])
n=int(input())
a=list(map(int, input().split(' ')))
b=list(map(int, input().split(' ')))

res=[]
flag=0
for i in range(n-2):
    if a[i]<b[i]:
        flag=-1
        print('NO')
        break
    if a[i]==b[i]:
        res.append(a[i])
        res.append(b[i])
        if a[i]!=a[i+1] and a[i]!=b[i+1]:
            flag=-1
            print('NO')
            break
