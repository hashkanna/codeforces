from collections import defaultdict
from math import ceil
dp=defaultdict(list)
help=defaultdict(list)

# def helper(x,y,dp,help):
#     l=[]
#     for i in dp[x]:
#         for j in dp[y]:
#             # print(i+j)
#             # if len(set(i+j)) == len(i+j):
#             #     l.append(i+j)
#             if i[-1] < j[0]:
#                 l.append(i+j)
#     if (x,y) not in help:
#         help[(x,y)]=l
#     return l
#
# def dp(i):
#     if i==1:
#         return [[1]]
#     elif i==2:
#         return [[2]]
#     else:
#         tmp=[]
#         for j in range(1,ceil(i/2)):
#             # dp[i].append([j,i-j])
#             print(j,i-j)
#             print(helper(dp(j), dp(i-j)))
#             tmp.append(helper(dp(j), dp(i-j)))
#             tmp1=[]
#             for x in tmp:
#                 if sorted(x) not in tmp:
#                     tmp1.append(sorted(x))
#         return tmp1+[[i]]
#
# print(dp(5))
dp[1]=[[1]]
dp[2]=[[2]]
dp[3]=[[3],[1,2]]
dp[4]=[[4],[1,3]]

memo=defaultdict(list)

def help1(l,dp):
    # count+=0
    tmp=[]
    for i in range(len(l)-1):
        if l[i+1]-l[i]>1:
            tmp.append(l[:i]+[l[i]+1]+l[i+1:])
    if l[-1]-l[i-2]>1:
        tmp.append(l[:-1]+[l[-1]+1])
    for y in tmp:
        if 1 not in y:
            tmp.append([1]+y)

    tmp1=[]
    for x in tmp:
        if sorted(x) not in tmp1:
            tmp1.append(sorted(x))
    memo[tuple(l)]=tmp1
    return tmp1

for i in range(5,20+1):
    for x in dp[i-1]:
        if len(x)==1:
            dp[i].append([i])
        else:
            if tuple(x) not in memo:
                dp[i]+=help1(x,dp)
            else:
                print('he;')
                dp[i]+=memo[tuple(x)]
print(dp[7])

# for i in range(5,100+1):
#     dp[i].append([i])
#     for j in range(1,ceil(i/2)):
#         # dp[i].append([j,i-j])
#         # dp[i]+=helper(dp[j], dp[i-j],help)
#         if (j,i-j) not in help:
#             # print(j,i-j)
#             dp[i]+=helper(j, i-j,dp,help)
#         else:
#             dp[i]+=help(j,i-j)
#         tmp=[]
#         for x in dp[i]:
#             if sorted(x) not in tmp:
#                 tmp.append(sorted(x))
#         dp[i]=tmp
#         # print(dp[i])
#
# # print(dp[11])
# print([len(dp[i]) for i in range(101)])
