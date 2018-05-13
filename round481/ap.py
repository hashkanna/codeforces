n=int(input())
a=list(map(int, input().split(' ')))
aa=[a[x]-a[x+1] for x in range(n-1)]
aaa=[aa[x]-aa[x+1] for x in range(len(aa)-1)]
d=[abs(x) for x in aaa]

if n==1 or n==2:
    print(0)
elif len(set(aa))==1:
    print(0)
elif max(d)>4:
    print(-1)
else:
    print(len(set(d))-d.count(0)+1)
