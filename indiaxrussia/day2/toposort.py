from collections import defaultdict
from collections import Counter

def dfs(u,p):
    # visited[u]=True
    global timer
    global cycle
    colors[u]=1
    parents[u]=p
    tin[u]=timer
    timer+=1
    # cc[u]=cc_num
    # print(u)
    for v in g[u]:
        # if not visited[v]:
        if colors[v]==1:
            cycle=True
            return
        if colors[v]==0:
            dfs(v,u)
    colors[u]=2
    tout[u]=timer
    timer+=1

g=defaultdict(list)
n,m=map(int, input().split(' '))
for edge in range(m):
    a,b=map(int, input().split(' '))
    g[a].append(b)
    # g[inp[1]-1].append(inp[0]-1)
# visited=[False]*n
colors=[0]*n
tin=[-1]*n
tout=[-1]*n
parents=[-1]*n
# cc=[-1]*n
# cc_num=0
timer=0
cycle=False
for i in range(n):
    if colors[i]==0:
    # if not visited[i]:
        # cc_num+=1
        dfs(i,i)
        if cycle==True:
            break
# dfs(0,0)
# cc_size=Counter(cc)
# print(*[cc_size[cc[i]] for i in range(n)])
# for i in range(n):
#     print(i, tin[i],tout[i])
# print(tout)
# for ind,num in enumerate(sorted(tout)):
#     print(ind, end=' ')
if cycle==True:
    print('NO')
else:
    print('YES')
    print(*[i[0] for i in sorted(enumerate(tout), key=lambda x:-x[1])])
