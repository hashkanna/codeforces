n,k=list(map(int,input().split(' ')))

from functools import reduce
def factors(n):
    #return set(reduce(list.__add__,
    #            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    for i in range(int(n**0.5), 0, -1):
        if n%i==0:
            return n//i, i

if n<k:
    print(n+k)
else:
    val=factors(n)
    if (val[0]==val[1]) and (val[0]>=k):
        res=(n*k)+1
    else:
        res=val[0]*k+val[1]
    print(res)
