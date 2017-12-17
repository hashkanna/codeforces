from math import gcd

# def div1(n,a,b):
#     for i in range(1,10000001):
#         for j in range(1,10000001//i):
#             if (i*a)+(j*b)==n:
#                 print("YES")
#                 return(str(i) + ' ' + str(j))
#     return "NO"

n=int(input())
a=int(input())
b=int(input())

# if n%a==0:
#     print("YES")
#     print(str(n//a) + ' 0')
# elif n%b==0:
#     print("YES")
#     print('0 ' + str(n//b))
# elif n%gcd(a,b)==0:
#     print(div1(n,a,b))
# else:
#     print("NO")
#

for i in range(1,1+(n//a)):
    c = n - i * a
    if (c % b == 0):
        print("YES")
        print(str(i) + ' ' + str(c//b))
        break

if n%gcd(a,b)!=0:
    print("NO")
