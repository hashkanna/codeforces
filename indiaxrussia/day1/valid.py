n=int(input())
k=int(input())
res=k**n
print("A",res)
res = res - ( k**(n-1) )
print("B",res)
for i in range(2,n):
    res = res - ( (n-i) * k**(n-i) )
    print("C" + str(i), res)
    res = res + (n-i+1)
    print("D" + str(i), res)
print(res)
