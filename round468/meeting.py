m=int(input())
n=int(input())
mid=(m+n)//2
a=abs(mid-m)
b=abs(mid-n)
res=(a*(a+1))//2
res+=(b*(b+1))//2
print(res)
