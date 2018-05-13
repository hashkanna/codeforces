n=int(input())
a=list(input().split())
res=[]
for i in a[::-1]:
    if i not in res:
        res.append(i)
result=' '.join(res[::-1])
print(len(res))
print(result)
