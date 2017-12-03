from math import gcd
from functools import reduce

n=int(input())
s=list(map(int, input().split()))
res = {s[-1]}


if reduce(gcd,s)!=s[0]:
    print(-1)
else:
    for i in range(n-1, -1, -1):
        for j in range(i):
            # print(i,j)
            res.add(gcd(s[i],s[j]))
        if len(res)==4000:
            break
    print(len(res))
    print(*res)
