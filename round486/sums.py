from collections import defaultdict
k=int(input())

d=defaultdict(list)
flag=-1

for i in range(k):
    if flag==1:
        break
    else:
        n=int(input())
        if n!=0:
            L=list(map(int, input().split(' ')))
            L_sum=sum(L)
            for ind,x in enumerate(L):
                val = L_sum-x
                if val not in d:
                    d[val] = [i,ind]
                else:
                    if i!=d[val][0]:
                        flag=1
                        print('YES')
                        print(1+d[val][0], 1+d[val][1])
                        print(1+i, 1+ind)
                        break

if flag==-1:
    print('NO')
