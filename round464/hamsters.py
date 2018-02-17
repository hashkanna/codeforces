import math
n,k = list(map(int,input().split()))
a = list(map(int,input().split()))

min_val=int(1+math.pow(10,18))
for i in range(k):
    if (n%a[i] < min_val):
        min_val=n%a[i]
        ind_val=i

print(ind_val+1,n//a[ind_val])
