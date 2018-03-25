from collections import defaultdict

def dfs(u,p):
    # visited[u]=True
    global timer
    colors[u]=1
    parents[u]=p
    tin[u]=timer
    timer+=1
    print(u)
    for v in g[u]:
        # if not visited[v]:
        if colors[v]==0:
            dfs(v,u)
    colors[u]=2
    tout[u]=timer
    timer+=1

g=defaultdict(list)
g[0]=[1,2]
g[1]=[0,3,4]
g[2]=[0]
g[3]=[1]
g[4]=[1]
n=len(g)
visited=[False]*n
colors=[0]*n
tin=[-1]*n
tout=[-1]*n
parents=[-1]*n
timer=0
cycle=False
dfs(0,0)
for i in g:
    print(i, tin[i],tout[i])

# tree edge gray to white
# Backward edge gray to gray - cycles
# forward edge gray to black
# cross edge gray to black

# topological sort
# only if graph is directed and acyclic
# sort vertices in decreasing order of tout values

# bridges
# check if a tree is a bridge
# forward up value of a vertex

# cut vertices
