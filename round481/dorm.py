n,m=list(map(int, input().split(' ')))
aa=list(map(int, input().split(' ')))
k=list(map(int, input().split(' ')))
tot=0
aa=[0]+aa
a=[]
for x in aa:
    tot+=x
    a.append(tot)

# print(a)
i=1
j=0
while j<m:
    # if k[j] <= a[i]:
    #     res=k[j]-a[i-1]
    # else:
    while k[j] > a[i]:
        i+=1
    res=k[j]-a[i-1]
        # i+=1
    print(i,res)
    j+=1
a=[0]+a
i=1
