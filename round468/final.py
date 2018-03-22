n,a,b=list(map(int, input().split(' ')))
# m=n//2
# if (a<=m and b>m) or (b<=m and a>m):
#     print("Final!")
# else:
#     # x=(a+1)//2
#     # y=(b+1)//2
#     res=abs(a-b)
#     c=a if a>b else b
#     if c%2==1:
#         print(len(bin(res))-1)
#     else:
#         print(len(bin(res))-2)

# res=abs(len(bin(a-1)) - len(bin(b-1)))
a-=1
b-=1
n-=1
res=len(bin(a^b))-2
if res==len(bin(n))-2:
    print("Final!")
else:
    print(res)
