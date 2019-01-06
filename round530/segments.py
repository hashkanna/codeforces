import math
n=int(input())

val=int(math.sqrt(n))
if val*val==n:
    print(2*val)
elif n-(val*val)<=val:
    print(1+(2*val))
else:
    print(2+(2*val))
