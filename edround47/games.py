n,m=list(map(int,input().split(' ')))
c=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))

i=0
j=0
res=0
while i<n and j<m:
    if c[i]<=a[j]:
        res+=1
        j+=1
    i+=1
print(res)
