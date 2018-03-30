def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

n,k=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))

print((factorial(n) // (factorial(k) * factorial(n-k))%1000000000))
