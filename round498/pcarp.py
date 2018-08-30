n,k=list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))


res=sorted(sorted(range(len(a)), key=lambda i: a[i])[-k:])
# print(res)
r1=0
r2=[]
tmp=-1
for i in res:
    r1+=a[i]
    r2.append(i-tmp)
    tmp=i
if k>1: r2[-1]=(n-1-res[-2])
if k==1: r2=[n]
print(r1)
print(*r2)
