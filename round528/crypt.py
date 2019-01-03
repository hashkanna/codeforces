import math

s=input()
n=len(s)

if n==1:
    print(s)
else:
    m=math.ceil(n/2)-1
    res=s[m]+s[m+1]

    for i in range(1,1+((n-2)//2)):
        res+=s[m-i]
        res+=s[m+i+1]

    if n%2!=0:
        res+=s[0]
    print(res)
