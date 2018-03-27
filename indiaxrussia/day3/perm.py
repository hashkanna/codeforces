def factorial(n):
    m=1
    while(n>1):
        m*=n
        n-=1
    return m

n=int(input())
l=list(map(int, input().split(' ')))
s=sorted(l)
# print(l,s)

res=0
for i in range(n-1):
    z=sorted(l[i:]).index(l[i])
    res+=(z*factorial(n-i-1))
res+=1
print(res)
