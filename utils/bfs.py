from collections import defaultdict
from collections import deque

def bfs(u,p):
    

g=defaultdict(list)
g[0]=[1,2]
g[1]=[0,3,4]
g[2]=[0]
g[3]=[1]
g[4]=[1]
n=len(g)
# visited=[False]*n
# colors=[0]*n
# tin=[-1]*n
# tout=[-1]*n
# timer=0
q=deque()
bfs(0,0)

# for i in g:
#     print(i, tin[i],tout[i])
