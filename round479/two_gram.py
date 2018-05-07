from collections import defaultdict
n=int(input())
s=input()
d=defaultdict(int)
max=0
for i in range(n-1):
    d[s[i]+s[i+1]]+=1
    if d[s[i]+s[i+1]] > max:
        max=d[s[i]+s[i+1]]
        res=s[i]+s[i+1]
print(res)
