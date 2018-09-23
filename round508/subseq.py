n,k=list(map(int,input().split(' ')))
s=input()

from collections import Counter
d=Counter(s)
if len(d) < k:
    print(0)
elif len(d) == k:
    ans=min([d[x] for x in d])
    print(ans*k)
