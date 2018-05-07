def wrong_number(n):
    if n%10==0:
        return n//10
    else:
        return n-1
n,k=list(map(int, input().split(' ')))

for i in range(k):
    n=wrong_number(n)

print(n)
