k=int(input())
a=[]
b=[]
for i in range(k):
    n=int(input())
    if n!=0:
        L=list(map(int, input().split(' ')))
        L_sum=sum(L)
        L1=[L_sum-x for x in L]
        a.append(L1)
        b.append(set(L1))
    else:
        a.append([])
        b.append(set([]))
# print(a)

flag=-1
for i in range(k):
    if flag==1:
        break
    for j in range(i+1,k):
        inter = list(b[i].intersection(b[j]))
        if len(inter) > 0:
            flag=1
            print('YES')
            print(i+1, 1+a[i].index(inter[0]))
            print(j+1, 1+a[j].index(inter[0]))
            break
            # for ind, x in enumerate(a[i]):
            #     try:
            #         res=a[j].index(x)
            #         print('YES')
            #         print(i+1, ind+1)
            #         print(j+1, res+1)
            #         break
            #     except:
            #         pass
if flag==-1:
    print('NO')
