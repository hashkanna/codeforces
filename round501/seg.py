n,m=list(map(int, input().split(' ')))

inp=range(1,m+1)
l=[]
for i in range(n):
    a,b=list(map(int, input().split(' ')))
    l+=range(a,b+1)
res=set(inp)-set(l)
print(len(res))
if len(res)!=0:
    print(*res)
