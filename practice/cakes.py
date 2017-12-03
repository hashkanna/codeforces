import math
n,t,k,d = list(map(int, input().split()))

print(math.ceil(n/k)*t)
c=((n>k)*t)+d
c+=math.ceil((n-k)/(k+k)) if n>k else 0
print(c)
