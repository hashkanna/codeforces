n=int(input())
from collections import defaultdict
d=defaultdict(int)

for i in range(n):
    s=input()
    count=0
    valid=0
    for i in s:
        if i=='(':
            count+=1
        else:
            count-=1
        if count<0:
            valid=-1
            # return False
    # print(valid, count)
    if valid==0 and count==0:
        d[0]+=1
    if count>0 and s[0]=='(':
        d[count]+=1
    if count<0 and s[-1]==')':
        d[count]+=1

res=0
for i in d:
    if i==0:
        res+=d[0]*d[0]
    elif i>0:
        if -i in d:
            res+=d[i]*d[-i]
print(d)
print(res)
