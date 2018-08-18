n=int(input())
a=list(map(int,input().split(' ')))
aa=[]

from collections import defaultdict
d=defaultdict(int)
for i in range(n):
    d[i+1]=a[i]
# print(d)

def check_cycle(val,cycles):
    for cycle in cycles:
        if val in cycle[1]:
            return cycle[0]
    return -1

ans=[]
cycles=[]
for j in range(n):
    aa=[]
    tmp=j+1
    cycle=[]
    while tmp not in aa and check_cycle(tmp,cycles)==-1:
        aa.append(tmp)
        cycle.append(tmp)
        tmp=d[tmp]
        # aa.append(t)
        # # print(j,aa)
        # tmp=t
    if check_cycle(tmp,cycles)==-1:
        cycles.append((tmp, cycle))
        ans.append(check_cycle(tmp,cycles))
    else:
        ans.append(j+1)

# print(cycles)
print(*ans)
