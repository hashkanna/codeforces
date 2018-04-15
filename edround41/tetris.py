from collections import Counter
n,m=list(map(int, input().split()))
a=list(map(int, input().split()))
d=Counter(a)
if len(d)!=n:
    print(0)
else:
    print(min(d.values()))
