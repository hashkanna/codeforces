k=int(input())
a=[]
b=[]

for i in range(k):
    n=int(input())
    if n!=0:
        L=list(map(int, input().split(' ')))
        # L_sum=sum(L)
        # L1=[L_sum-x for x in L]
        a.append(L)
        b.append(set(L))
    else:
        a.append([])
        b.append(set([]))

flag=-1
for i in range(k):
    if flag==1:
        break
    for j in range(i+1,k):
        if b[i]==b[j] and len(b[i])==1 and sum(a[i])==sum(a[j]):
            flag=1
            print('YES')
            print(i+1, 1)
            print(j+1, 1)
            break
        x=b[i]-b[j]
        y=b[j]-b[i]
        inter=list(b[i].intersection(b[j]))
        if len(b[i]) > 0 and len(x)==0 and sum(a[i])==sum(a[j]):
            flag=1
            print('YES')
            print(i+1, 1+a[i].index(inter[0]))
            print(j+1, 1+a[j].index(inter[0]))
            break
        x_sum=sum(x)
        y_sum=sum(y)
        x_new=[x_sum-w for w in x]
        y_new=[y_sum-w for w in y]
        new_inter = list(set(x_new).intersection(set(y_new)))
        if len(new_inter) > 0:
            flag=1
            print('YES')
            print(i+1, 1+a[i].index(new_inter[0]))
            print(j+1, 1+a[j].index(new_inter[0]))
            break


            # print(i+1, 1+a[i].index(inter[0]))
            # print(j+1, 1+a[j].index(inter[0]))
            # break

if flag==-1:
    print('NO')
