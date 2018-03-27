n=int(input())
# n=(n-5)+1
# print(120*n*n)
res=(n-5+1)*(n-5+1)

for i in range((n-5+2),n+1):
    res*=i

print(res)
