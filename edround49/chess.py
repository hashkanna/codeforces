n,q=list(map(int,input().split(' ')))
import math

# arr = [[0 for i in range(n)] for j in range(n)]
#
# if n%2==0:
#     for a in range(n):
#         for b in range(n):
#             # if a%2==0:
#             #     if b%2==0:
#             if a==0 and b==0:
#                 arr[a][b]=1
#             elif a==0 and b==1:
#                 arr[a][b]=1+math.ceil((n*n)/2)
#             else:
#                 if b==0:
#                     arr[a][b]=1+arr[a-1][n-1]
#                 elif b==1:
#                     arr[a][b]=1+arr[a-1][n-2]
#                 else:
#                     arr[a][b]=1+arr[a][b-2]
# else:
#     for a in range(n):
#         for b in range(n):
#             # if a%2==0:
#             #     if b%2==0:
#             if a==0 and b==0:
#                 arr[a][b]=1
#             elif a==0 and b==1:
#                 arr[a][b]=1+math.ceil((n*n)/2)
#             else:
#                 if b==0:
#                     arr[a][b]=1+arr[a-1][n-2]
#                 elif b==1:
#                     arr[a][b]=1+arr[a-1][n-1]
#                 else:
#                     arr[a][b]=1+arr[a][b-2]

# for t in range(q):
#     i,j=list(map(int,input().split(' ')))
#     print(arr[i-1][j-1])

if n%2==0:
    for i in range(q):
        a,b=list(map(int,input().split(' ')))
        if (a+b)%2==0:
            res=(a-1)*(n//2)
            res+=(b-1)//2
            res+=1
            print(res)
        else:
            res=(a-1)*(n//2)
            res+=(b-1)//2
            res+=(n*2)+1
            print(res)
else:
    for i in range(q):
        a,b=list(map(int,input().split(' ')))
        if (a+b)%2==0:
            res=(a//2)*math.ceil(n/2)
            res+=((a-1)//2)*(n//2)
            res+=(b-1)//2
            res+=1
            print(res)
        else:
            res=(a//2)*(n//2)
            res+=((a-1)//2)*math.ceil(n/2)
            res+=(b-1)//2
            res+=math.ceil((n*n)/2)+1
            print(res)
