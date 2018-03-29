from operator import mul
from math import acos
from math import radians
from math import degrees
import math

# eps=1e-9

x=list(map(int, input().split(' ')))
y=list(map(int, input().split(' ')))
z=list(map(int, input().split(' ')))

# x = [yyy[0]-xxx[0], yyy[1]-xxx[1]]
# y = [zzz[0]-yyy[0], zzz[1]-yyy[1]]
# z = [xxx[0]-zzz[0], xxx[1]-zzz[1]]

def norm(xx):
    return math.sqrt(sum( comp**2 for comp in xx ))

def dot_product(a,b):
    return sum(map(mul, a, b))

AB = [y[0]-x[0], y[1]-x[1]]
CB = [y[0]-z[0], y[1]-z[1]]
A=dot_product(AB,CB)

BC = [z[0]-y[0], z[1]-y[1]]
AC = [z[0]-x[0], z[1]-x[1]]
B=dot_product(BC,AC)

CA = [x[0]-z[0], x[1]-z[1]]
BA = [x[0]-y[0], x[1]-y[1]]
C=dot_product(CA,BA)

# Y = [y[0]-z[0], y[1]-z[1]]
# Z = [z[0]-x[0], z[1]-x[1]]
# A=dot_product([x[0]-y[0],x[1]-y[1]])
# B=dot_product([y[0]-z[0],y[1]-z[1]])
# C=dot_product([z[0]-x[0],z[1]-x[1]])
# A=dot_product(X,Y)
# B=dot_product(Y,Z)
# C=dot_product(Z,X)

# A=dot_product(x,y)
# B=dot_product(y,z)
# C=dot_product(z,x)

# print(A,B,C)

if A<0 or B<0 or C<0:
    print('OBTUSE')
elif A==0 or B==0 or C==0:
    print('RIGHT')
else:
    print('ACUTE')

# A = (sum(map(mul, x, y))) / (eps+(norm(x)*norm(y)))
# B = (sum(map(mul, x, z))) / (eps+(norm(x)*norm(z)))
# C = (sum(map(mul, y, z))) / (eps+(norm(y)*norm(z)))
#
# AA=degrees(acos(A))
# BB=degrees(acos(B))
# CC=degrees(acos(C))
# print(AA,BB,CC)

# if abs(AA-90) <= eps or abs(BB-90) <= eps or abs(CC-90) <= eps:
#     print('RIGHT')
# elif AA>90 or BB>90 or CC>90:
#     print('OBTUSE')
# else:
#     print('ACUTE')

# if A+B > C and A+C > B and B+C > A:
#     print('ACUTE')
#
# if A==0 or B==0 or C==0:
#     print('RIGHT')
