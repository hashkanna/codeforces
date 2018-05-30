import math
x,y=list(map(int, input().split()))

a=(math.log(x))/x
b=(math.log(y))/y

# print(a,b)

if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')
