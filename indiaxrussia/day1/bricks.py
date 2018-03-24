from collections import defaultdict
from math import ceil
dp=defaultdict(list)

def helper(x,y):
    l=[]
    for i in x:
        for j in y:
            # print(i+j)
            if len(set(i+j)) == len(i+j):
                l.append(i+j)
    return l

dp[1]=[[1]]
dp[2]=[[2]]
dp[3]=[[3],[1,2]]
dp[4]=[[4],[1,3]]
for i in range(5,11+1):
    dp[i].append([i])
    for j in range(1,ceil(i/2)):
        # dp[i].append([j,i-j])
        dp[i]+=helper(dp[j], dp[i-j])
        tmp=[]
        for x in dp[i]:
            if sorted(x) not in tmp:
                tmp.append(sorted(x))
        dp[i]=tmp

print(dp[10])
