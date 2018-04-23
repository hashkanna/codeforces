n,A,B,C,T=list(map(int, input().split(' ')))
a=list(map(int, input().split(' ')))

res=n*A
if C-B<=0:
    print(res)
else:
    res+=sum([(C-B)*(T-x) for x in a])
    print(res)
