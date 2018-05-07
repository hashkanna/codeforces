n,k=list(map(int, input().split()))
a=list(map(int, input().split()))
a=sorted(a)

res=a[k-1]
if n==k:
    print(a[-1])
elif k==0 and a[0]!=1:
    print(1)
elif k!=0 and res<a[k]:
    print(res)
else:
    print(-1)
