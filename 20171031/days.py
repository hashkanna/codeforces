import math
n=int(input())

if n==0:
    print(0, 0)
elif n==1:
    print(0, 1)
elif n==2:
    print(0, 2)
else:
    print( (int(n%7==6) + n//7),2*(math.ceil(n/7))+(1 if n%7==1 else 2))
