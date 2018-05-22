n=int(input())
a=list(map(int, input().split(' ')))
a=sorted(a)
b=[x for x in range(1,n,2)]
c=[x for x in range(2,n+1,2)]
# print(a, b, c)

s1=0
s2=0
for i, j in zip(a,b):
    s1+=abs(i-j)

for i, j in zip(a,c):
    s2+=abs(i-j)

print(min(s1,s2))
