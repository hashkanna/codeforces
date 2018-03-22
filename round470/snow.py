n=int(input())
v=list(map(int, input().split()))
t=list(map(int, input().split()))

res=[0 for x in range(n)]
for i in range(n):
    for j in range(i,n):
        if v[i]>0:
            res[j]+=min(v[i],t[j])
            v[i]-=t[j]
        else:
            break
print(*res, sep=' ')
#
# res=[]
# for i in range(n):
#     r=0
#     for j in range(i):
#         r+=max(0,)
#         v[j]-=t[i]
#     res.append(r)
