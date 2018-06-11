n,m,a,b=list(map(int,input().split(' ')))
if n%m==0:
    res=0
elif n<m:
    res=min((n)*b,a*((m-(n%m))))
else:
    res=min((n-m)*b,a*((m-(n%m))))
print(res)
